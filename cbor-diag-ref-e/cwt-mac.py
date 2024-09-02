#!/usr/bin/env python3

import sys
from cwt import COSE, COSEKey, COSEKeyParams, COSEMessage

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} [input cbor file] [output cose file]", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], "rb") as f:
    input_bin = f.read()

mac_key = COSEKey.new({
    COSEKeyParams.KTY: 4, # oct
    COSEKeyParams.ALG: 5, # HMAC 256/256
    COSEKeyParams.K: b'a' * 32 # '6161...61'
})

sender = COSE.new()
encoded = sender.encode(
    input_bin,
    mac_key,
    protected={"alg": "HMAC 256/256"}
)
cose_mac0 = COSEMessage.loads(encoded)
encoded, detached_payload = cose_mac0.detach_payload()

# Verify that the library has produced valid COSE_Mac0 binary
recipient = COSE.new()
assert input_bin == recipient.decode(encoded.dumps(), mac_key, detached_payload=detached_payload)

with open(sys.argv[2], "wb") as f:
    f.write(encoded.dumps())
