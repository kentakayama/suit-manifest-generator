#!/usr/bin/env python3

import argparse
import json
from cwt import COSE, COSEKey, COSEMessage

parser = argparse.ArgumentParser(description="Generate COSE_Mac0 binary without payload")
parser.add_argument("plaintext_payload", help="input filename to be MACed")
parser.add_argument("mac_jwk",           help="jwk filename of MAC key")
parser.add_argument("cose",              help="output filename of COSE_Mac0 binary")
args = parser.parse_args()

with open(args.plaintext_payload, "rb") as f:
    input_bin = f.read()

with open(args.mac_jwk, "r") as f:
    mac_key_jwk = json.loads(f.read())
mac_key = COSEKey.from_jwk(mac_key_jwk)

sender = COSE.new(alg_auto_inclusion=True, kid_auto_inclusion=True)
encoded = sender.encode(
    input_bin,
    mac_key,
    protected={"alg": mac_key_jwk["alg"]}
)
cose_mac0 = COSEMessage.loads(encoded)
encoded, detached_payload = cose_mac0.detach_payload()

# Verify that the library has produced valid COSE_Mac0 binary
recipient = COSE.new()
assert input_bin == recipient.decode(encoded.dumps(), mac_key, detached_payload=detached_payload)

with open(args.cose, "wb") as f:
    f.write(encoded.dumps())
