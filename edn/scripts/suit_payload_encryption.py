#!/usr/bin/env python3

import sys
from typing import List, Tuple
import argparse
import json
from cwt import COSE, COSEMessage, COSEKey, Recipient
from cwt.const import COSE_ALGORITHMS_CEK_NON_AEAD, COSE_ALGORITHMS_KEY_WRAP, COSE_ALGORITHMS_CKDM_KEY_AGREEMENT_WITH_KEY_WRAP_ES, COSE_ALGORITHMS_CKDM_KEY_AGREEMENT_WITH_KEY_WRAP_SS, COSE_ALGORITHMS_CKDM_KEY_AGREEMENT_WITH_KEY_WRAP

def encrypt_content(plaintext: bytes, cek_jwk: dict, recipients: List[Recipient], detached_payload: bool = False) -> Tuple[bytes, bytes]:
    # care deterministic encoding before consuming protected header
    cek = COSEKey.from_jwk(cek_jwk)
    u = {"iv": cek.generate_nonce()}

    sender = COSE.new(alg_auto_inclusion=True, kid_auto_inclusion=True)
    encoded = sender.encode_and_encrypt(
        plaintext,
        key=cek,
        unprotected=u,
        recipients=recipients
    )

    if detached_payload:
        msg, payload = COSEMessage.loads(encoded).detach_payload()
        return msg.dumps(), payload
    return encoded, b""


def encrypt_aeskw(plaintext: bytes, cek_jwk: dict, key_wrap_jwk: dict, detached_payload: bool = False) -> Tuple[bytes, bytes]:
    if not key_wrap_jwk['alg'] in COSE_ALGORITHMS_KEY_WRAP:
        print(f"Unknown alg: {key_wrap_jwk['alg']}")
        sys.exit(1)

    u = {"alg": key_wrap_jwk['alg'], "kid": key_wrap_jwk['kid']} if 'kid' in key_wrap_jwk else {"alg": key_wrap_jwk['alg']}
    key_wrap = COSEKey.from_jwk(key_wrap_jwk)
    r = Recipient.new(unprotected=u, sender_key=key_wrap)
    return encrypt_content(plaintext, cek_jwk, [r], detached_payload)


def encrypt_ecdh_aeskw(plaintext: bytes, cek_jwk: COSEKey, sender_priv_jwk: COSEKey, receiver_pub_jwk: COSEKey, detached_payload: bool = False) -> Tuple[bytes, bytes]:
    kw_alg, key_len = \
        ("A128KW", 128) if sender_priv_jwk['alg'] in ["ECDH-ES+A128KW", "ECDH-SS+A128KW"] else \
        ("A192KW", 192) if sender_priv_jwk['alg'] in ["ECDH-ES+A192KW", "ECDH-SS+A192KW"] else \
        ("A256KW", 256) if sender_priv_jwk['alg'] in ["ECDH-ES+A256KW", "ECDH-SS+A256KW"] else \
        ("Unknown", 0)
    if key_len == 0:
        print(f"Unknown alg: {sender_priv_jwk['alg']}")
        sys.exit(1)

    u = {"kid": sender_priv_jwk['kid']} if 'kid' in sender_priv_jwk else {}
    inner_protected_header = {"alg": sender_priv_jwk['alg']}
    context = {
        "alg": kw_alg, # e.g. "A128KW"
        "supp_pub": {
            "key_data_length": key_len, # e.g. 128
            "protected": inner_protected_header,
            "other": "SUIT Payload Encryption",
        }
    }

    r = Recipient.new(
        protected=inner_protected_header,
        unprotected=u,
        sender_key=COSEKey.from_jwk(sender_priv_jwk),
        recipient_key=COSEKey.from_jwk(receiver_pub_jwk),
        context=context
    )
    return encrypt_content(plaintext, cek_jwk, [r], detached_payload)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate COSE_Encrypt binary and encrypted payload")
    parser.add_argument("plaintext_payload",                       help="input filename of plaintext")
    parser.add_argument("cek_jwk",                                 help="jwk filename of content encryption key")
    parser.add_argument("encryption_info",                         help="output filename of COSE_Encrypt binary")
    parser.add_argument("-e", "--encrypted_payload", default=None, help="output filename of detached payload")
    parser.add_argument("-s", "--sender_priv_jwk",   default=None, help="jwk filename of sender's private key ([receiver_pub_jwk] is required)")
    parser.add_argument("-r", "--receiver_pub_jwk",  default=None, help="jwk filename of receiver's public key ([sender_priv_jwk] is required)")
    parser.add_argument("-k", "--key_wrap_jwk",      default=None, help="jwk filename of pre-shared KEK secret key ([sender_priv_jwk] should not be set)")
    args = parser.parse_args()

    sender_priv_jwk = None
    receiver_pub_jwk = None
    key_wrap_jwk = None

    with open(args.plaintext_payload, "rb") as f:
        plaintext = f.read()
    with open(args.cek_jwk, "r") as f:
        cek_jwk = json.loads(f.read())
    if args.sender_priv_jwk:
        # asymmetric key distribution methods
        if not args.sender_priv_jwk or args.key_wrap_jwk:
            parser.print_help()
            sys.exit(1)
        with open(args.sender_priv_jwk, "r") as f:
            sender_priv_jwk = json.loads(f.read())
        with open(args.receiver_pub_jwk, "r") as f:
            receiver_pub_jwk = json.loads(f.read())
        if sender_priv_jwk['alg'] != receiver_pub_jwk['alg']:
            print(f"Algs in {args.sender_priv_jwk} and {args.receiver_pub_jwk} differ")
            sys.exit(1)
    elif args.key_wrap_jwk:
        # symmetric key distribution methods
        if args.sender_priv_jwk or args.receiver_pub_jwk:
            parser.print_help()
            sys.exit(1)
        with open(args.key_wrap_jwk, "r") as f:
            key_wrap_jwk = json.loads(f.read())
    else:
        parser.print_help()
        sys.exit(1)

    if sender_priv_jwk is not None and receiver_pub_jwk is not None:
        if sender_priv_jwk['alg'] in COSE_ALGORITHMS_CKDM_KEY_AGREEMENT_WITH_KEY_WRAP:
            encryption_info, detached_payload = encrypt_ecdh_aeskw(plaintext, cek_jwk, sender_priv_jwk, receiver_pub_jwk, args.encrypted_payload is not None)
        else:
            print(f"Unknown alg {sender_priv_jwk['alg']}")
            sys.exit(1)
    elif key_wrap_jwk is not None:
        if key_wrap_jwk['alg'] in COSE_ALGORITHMS_KEY_WRAP:
            encryption_info, detached_payload = encrypt_aeskw(plaintext, cek_jwk, key_wrap_jwk, args.encrypted_payload is not None)
        else:
            print(f"Unknown alg {key_wrap_jwk['alg']}")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    with open(args.encryption_info, "wb") as f:
        f.write(encryption_info)
    if args.encrypted_payload is not None:
        with open(args.encrypted_payload, "wb") as f:
            f.write(detached_payload)
            print(f"Saved to {args.encryption_info} and {args.encrypted_payload}")
    else:
        print(f"Saved to {args.encryption_info}")
