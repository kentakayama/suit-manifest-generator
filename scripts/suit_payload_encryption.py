#!/usr/bin/env python3

import sys
import base64
from cwt import COSE, COSEMessage, COSEKey, Recipient

def save_to_files(encoded, encryption_info, encrypted_payload):
    if isinstance(encrypted_payload, str):
        msg, payload = COSEMessage.loads(encoded).detach_payload()
        with open(encryption_info, "wb") as f:
            f.write(msg.dumps())
        with open(encrypted_payload, "wb") as f:
            f.write(payload)
        print(f"Saved to {encryption_info} and {encrypted_payload}")
    else:
        with open(encryption_info, "wb") as f:
            f.write(encoded)
        print(f"Saved to {encryption_info}")


def encrypt_aeskw(plaintext: bytes, kek_alg: str, cek_alg: str, encryption_info: str, encrypted_payload: str):
    cek = COSEKey.from_symmetric_key(alg=cek_alg)
    kek = COSEKey.from_symmetric_key("a" * 16, alg=kek_alg, kid="kid-1")

    # care deterministic encoding before consuming protected header
    p = {}
    u = {}
    if cek_alg in ["A128CTR", "A192CTR", "A256CTR", "A128CBC", "A192CBC", "A256CBC"]:
        # non-AEAD
        u["alg"] = cek_alg
    else:
        # AEAD (default)
        p["alg"] = cek_alg
    u["iv"] = cek.generate_nonce()

    r = Recipient.new(unprotected={"alg": kek_alg, "kid": kek.kid}, sender_key=kek)
    sender = COSE.new()
    encoded = sender.encode_and_encrypt(
        plaintext,
        cek,
        protected=p,
        unprotected=u,
        recipients=[r],
    )
    save_to_files(encoded, encryption_info, encrypted_payload)


def encrypt_esdh_hkdf(plaintext: bytes, kek_alg: str, cek_alg: str, encryption_info: str, encrypted_payload: str):
    receiver_public_key_jwk = {
        "kty": "EC2",
        "crv": "P-256",
        "x": base64.b64encode(bytes.fromhex('5886CD61DD875862E5AAA820E7A15274C968A9BC96048DDCACE32F50C3651BA3')).decode(),
        "y": base64.b64encode(bytes.fromhex('9EED8125E932CD60C0EAD3650D0A485CF726D378D1B016ED4298B2961E258F1B')).decode(),
        #"d": base64.b64encode(bytes.fromhex('60FE6DD6D85D5740A5349B6F91267EEAC5BA81B8CB53EE249E4B4EB102C476B3')).decode(),
    }

    t = kek_alg.rsplit("+")
    if 1 == len(t):
        print(f"Unknown KEK alg: {kek_alg}")
        sys.exit(1)

    context = {
        "alg": cek_alg,
        "supp_pub": {
            "key_data_length": 128,
            "protected": {"alg": kek_alg}, # e.g. ECDH-ES+HKDF-256
            "other": "SUIT Payload Encryption",
        }
    }
    r = Recipient.new(
        protected={"alg": kek_alg},
        recipient_key=COSEKey.from_jwk(receiver_public_key_jwk),
        context=context
    )

    cek = COSEKey.from_symmetric_key(alg=cek_alg)
    sender = COSE.new()
    encoded = sender.encode_and_encrypt(
        plaintext,
        cek,
        protected={"alg": cek_alg},
        unprotected={"iv": cek.generate_nonce()},
        recipients=[r],
        enable_non_aead=True,
    )
    save_to_files(encoded, encryption_info, encrypted_payload)


def encrypt_esdh_aeskw(plaintext: bytes, kek_alg: str, cek_alg: str, encryption_info: str, encrypted_payload: str):
    print(f"{plaintext}, {kek_alg}, {cek_alg}, {encryption_info}, {encrypted_payload}")

    sender_private_key_jwk = {
        "kty": "EC2",
        "crv": "P-256",
        "x": base64.b64encode(bytes.fromhex('8496811AAE0BAAABD26157189EECDA26BEAA8BF11B6F3FE6E2B5659C85DBC0AD')).decode(),
        "y": base64.b64encode(bytes.fromhex('3B1F2A4B6C098131C0A36DACD1D78BD381DCDFB09C052DB33991DB7338B4A896')).decode(),
        "d": base64.b64encode(bytes.fromhex('0296588D909418B339D150420A3612B57FB4F631A69F224FAE90CB4F3FE18973')).decode(),
        "kid": "kid-2",
    }

    receiver_public_key_jwk = {
        "kty": "EC2",
        "crv": "P-256",
        "x": base64.b64encode(bytes.fromhex('5886CD61DD875862E5AAA820E7A15274C968A9BC96048DDCACE32F50C3651BA3')).decode(),
        "y": base64.b64encode(bytes.fromhex('9EED8125E932CD60C0EAD3650D0A485CF726D378D1B016ED4298B2961E258F1B')).decode(),
        #"d": base64.b64encode(bytes.fromhex('60FE6DD6D85D5740A5349B6F91267EEAC5BA81B8CB53EE249E4B4EB102C476B3')).decode(),
    }

    kek_alg_id, kw_alg, key_len = \
        (-29, "A128KW", 128) if "ECDH-ES+A128KW" == kek_alg else \
        (-30, "A192KW", 192) if "ECDH-ES+A192KW" == kek_alg else \
        (-31, "A256KW", 256) if "ECDH-ES+A256KW" == kek_alg else \
        (0, "Unknown", 0)
    if key_len == 0:
        print(f"Unknown KEK alg: {kek_alg}")
        sys.exit(1)

    cek = COSEKey.from_symmetric_key(alg=cek_alg)
    is_aead = cek_alg in ("A128GCM", "A192GCM", "A256GCM")

    if is_aead:
        outer_protected_header = {"alg": cek_alg}
        outer_unprotected_header = {"iv": cek.generate_nonce()}
    else:
        outer_protected_header = {}
        outer_unprotected_header = {"alg": cek_alg, "iv": cek.generate_nonce()}

    inner_protected_header = {"alg": kek_alg}
    inner_unprotected_header = {} # ephemeral key will be added

    context = {
        "alg": kw_alg, # e.g. A128KW
        "supp_pub": {
            "key_data_length": key_len, # e.g. 128
            "protected": inner_protected_header,
            "other": "SUIT Payload Encryption",
        }
    }

    # should we need to remove the side-effect on
    # python-cwt/cwt/utils.py
    #
    # comment out?
    # if recipient_alg:
    #     protected[1] = recipient_alg
    #     supp_pub[1] = cbor2.dumps(protected)
    r = Recipient.new(
        protected=inner_protected_header,
        unprotected=inner_unprotected_header,
        sender_key=COSEKey.from_jwk(sender_private_key_jwk),
        recipient_key=COSEKey.from_jwk(receiver_public_key_jwk),
        context=context
    )

    sender = COSE.new()
    encoded = sender.encode(
        plaintext,
        cek,
        protected=outer_protected_header,
        unprotected=outer_unprotected_header,
        recipients=[r],
        enable_non_aead=True,
    )
    save_to_files(encoded, encryption_info, encrypted_payload)

def print_usage():
    print("[Usage] ./suit_payload_encryption.py plaintext KEK-alg CEK-alg encryption_info [encrypted_payload]")
    print("    plaintext: filename of input plaintext")
    print("    KEK-alg: A128KW, ECDH-ES+HKDF-256, ECDH-ES+A128KW, ...")
    print("    CEK-alg: A128GCM, A128CTR, ...")
    print("    encryption_info: filename of output SUIT_Encryption_Info")
    print("    encrypted_payload(Optional): filename of output ciphertext (detached)")

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 5 or 6 < len(args):
        print_usage()
        sys.exit(1)

    plaintext_filename = args[1]
    kek_alg = args[2]
    cek_alg = args[3]
    encryption_info_filename = args[4]
    encrypted_payload_filename = args[5] if len(args) == 6 else None

    with open(plaintext_filename, "rb") as f:
        plaintext = f.read()

    if "A128KW" == kek_alg:
        encrypt_aeskw(plaintext, kek_alg, cek_alg, encryption_info_filename, encrypted_payload_filename)
    elif "ECDH-ES+HKDF-256" == kek_alg:
        encrypt_esdh_hkdf(plaintext, kek_alg, cek_alg, encryption_info_filename, encrypted_payload_filename)
    elif "ECDH-ES+A128KW" == kek_alg:
        encrypt_esdh_aeskw(plaintext, kek_alg, cek_alg, encryption_info_filename, encrypted_payload_filename)
    else:
        print_usage()
        sys.exit(1)
