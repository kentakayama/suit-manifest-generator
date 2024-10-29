#!/usr/bin/env python3

import argparse
import json
from cwt import COSE, COSEKey, COSEMessage

parser = argparse.ArgumentParser(description="Generate COSE_Mac0 or COSE_Sign1 binary without payload")
parser.add_argument("plaintext_payload", help="input filename to be MACed/signed")
parser.add_argument("jwk",               help="jwk filename of MAC/sign key")
parser.add_argument("cose",              help="output filename of COSE_Mac0 or COSE_Sign1 binary")
args = parser.parse_args()

with open(args.plaintext_payload, "rb") as f:
    input_bin = f.read()

with open(args.jwk, "r") as f:
    key_jwk = json.loads(f.read())
key = COSEKey.from_jwk(key_jwk)

sender = COSE.new(alg_auto_inclusion=True, kid_auto_inclusion=True)
encoded = sender.encode(
    input_bin,
    key
)
cose = COSEMessage.loads(encoded)
encoded, detached_payload = cose.detach_payload()

# Verify that the library has produced valid COSE_Mac0 or COSE_Sign1 binary
recipient = COSE.new()
assert input_bin == recipient.decode(encoded.dumps(), key, detached_payload=detached_payload)

with open(args.cose, "wb") as f:
    f.write(encoded.dumps())
