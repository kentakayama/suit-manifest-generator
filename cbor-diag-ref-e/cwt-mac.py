#!/usr/bin/env python3

import sys
from cwt import COSE, COSEKey, COSEKeyParams, COSEMessage

if len(sys.argv) != 3:
    sys.exit(-1)

with open(sys.argv[1], "r") as f:
    input_hex = f.read()

mac_key = COSEKey.new({
    COSEKeyParams.KTY: 4, # oct
    COSEKeyParams.ALG: 5, # HMAC 256/256
    COSEKeyParams.K: bytes.fromhex("61" * 16) # aa...a (16)
})

sender = COSE.new()
encoded = sender.encode(
    bytes.fromhex(input_hex),
    mac_key,
    protected={"alg": "HMAC 256/256"}
)
cose_mac0 = COSEMessage.loads(encoded)
encoded, detached_payload = cose_mac0.detach_payload()


with open(sys.argv[2], "wb") as f:
    f.write(encoded.dumps())

