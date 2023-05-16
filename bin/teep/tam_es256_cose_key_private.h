/*
 * Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.
 *
 * SPDX-License-Identifier: BSD-2-Clause
 *
 */

#ifndef TAM_ES256_COSE_KEY_PRIVATE_H
#define TAM_ES256_COSE_KEY_PRIVATE_H
const unsigned char tam_es256_cose_key_private_buf[] = {
    0xA5,                                 //# map(5)
       0x01,                              //# unsigned(1) / 1 = kty /
       0x02,                              //# unsigned(2) / 2 = EC2 /
       0x20,                              //# negative(0) / -1 = crv /
       0x01,                              //# unsigned(1) / 1 = P-256 /
       0x21,                              //# negative(1) / -2 = x /
       0x58, 0x20,                        //# bytes(32)
          0x0E, 0x90, 0x8A, 0xA8, 0xF0, 0x66, 0xDB, 0x1F,
          0x08, 0x4E, 0x0C, 0x36, 0x52, 0xC6, 0x39, 0x52,
          0xBD, 0x99, 0xF2, 0xA5, 0xBD, 0xB2, 0x2F, 0x9E,
          0x01, 0x36, 0x7A, 0xAD, 0x03, 0xAB, 0xA6, 0x8B,
       0x22,                              //# negative(2) / -3 = y /
       0x58, 0x20,                        //# bytes(32)
          0x77, 0xDA, 0x1B, 0xD8, 0xAC, 0x4F, 0x0C, 0xB4,
          0x90, 0xBA, 0x21, 0x06, 0x48, 0xBF, 0x79, 0xAB,
          0x16, 0x4D, 0x49, 0xAD, 0x35, 0x51, 0xD7, 0x1D,
          0x31, 0x4B, 0x27, 0x49, 0xEE, 0x42, 0xD2, 0x9A,
       0x23,                              //# negative(3) / -4 = d /
       0x58, 0x20,                        //# bytes(32)
          0x84, 0x1A, 0xEB, 0xB7, 0xB9, 0xEA, 0x6F, 0x02,
          0x60, 0xBE, 0x73, 0x55, 0xA2, 0x45, 0x88, 0xB9,
          0x77, 0xD2, 0x3D, 0x2A, 0xC5, 0xBF, 0x2B, 0x6B,
          0x2D, 0x83, 0x79, 0x43, 0x2A, 0x1F, 0xEA, 0x98,
};
const UsefulBufC tam_es256_cose_key_private = {
    .ptr = tam_es256_cose_key_private_buf,
    .len = sizeof(tam_es256_cose_key_private_buf)
};
#endif /* TAM_ES256_COSE_KEY_PRIVATE_H */
