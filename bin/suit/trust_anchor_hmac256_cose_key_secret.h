/*
 * Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.
 *
 * SPDX-License-Identifier: BSD-2-Clause
 *
 */

#ifndef TRUST_ANCHOR_HMAC256_COSE_KEY_SECRET_H
#define TRUST_ANCHOR_HMAC256_COSE_KEY_SECRET_H
const unsigned char trust_anchor_hmac256_cose_key_secret_buf[] = {
    0xA2,                                   //# map(2)
       0x01,                                //# unsigned(1) / 1 = key /
       0x04,                                //# unsigned(4) / 4 = Symmetric /
       0x20,                                //# negative(0) / -1 = k /
       0x58, 0x20,                          //# bytes(32)
          0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
          0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
          0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
          0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
}; // "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
const UsefulBufC trust_anchor_hmac256_cose_key_secret = {
    .ptr = trust_anchor_hmac256_cose_key_secret_buf,
    .len = sizeof(trust_anchor_hmac256_cose_key_secret_buf)
};
#endif /* TRUST_ANCHOR_HMAC256_COSE_KEY_SECRET_H */
