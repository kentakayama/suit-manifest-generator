/*
 * Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.
 *
 * SPDX-License-Identifier: BSD-2-Clause
 */

#include <stdio.h>
#include "csuit/suit_common.h"
#include "csuit/suit_manifest_decode.h"
#include "csuit/suit_manifest_encode.h"
#include "csuit/suit_manifest_print.h"
#include "csuit/suit_cose.h"
#include "suit_examples_common.h"
#if defined(SUIT_MANIFEST_SIGNER_TRUST_ANCHOR)
#include "trust_anchor_prime256v1_cose_key_private.h"
UsefulBufC private_key = trust_anchor_prime256v1_cose_key_private;
UsefulBufC public_key = NULLUsefulBufC;
#elif defined(SUIT_MANIFEST_SIGNER_TAM)
#include "tam_es256_cose_key_private.h"
UsefulBufC private_key = tam_es256_cose_key_private;
#include "trust_anchor_prime256v1_cose_key_public.h"
UsefulBufC public_key = trust_anchor_prime256v1_cose_key_public;
#else
#error Signing key is not specified
#endif

#define MAX_FILE_BUFFER_SIZE            (8 * 1024 * 1024)

int main(int argc,
         char *argv[])
{
    // check arguments.
    if (argc < 2) {
        printf("%s <manifest file path> [<signed manifest file path>]\n", argv[0]);
        return EXIT_FAILURE;
    }
    suit_err_t result = 0;
    int ret = EXIT_FAILURE;
    uint8_t indent = 4;
    uint8_t tabstop = 2;
    char *input_file = argv[1];
    char *output_file = (argc >= 3) ? argv[2] : NULL;
    suit_mechanism_t mechanisms[SUIT_MAX_KEY_NUM] = {0};
    uint8_t *manifest_buf = NULL;
    uint8_t *encode_buf = NULL;

    mechanisms[0].key.cose_algorithm_id = T_COSE_ALGORITHM_ES256;
    result = suit_set_suit_key_from_cose_key(private_key, &mechanisms[0].key);
    if (result != SUIT_SUCCESS) {
        printf("main : Failed to create signing key. %s(%d)\n", suit_err_to_str(result), result);
        return EXIT_FAILURE;
    }
    mechanisms[0].cose_tag = CBOR_TAG_COSE_SIGN1;
    mechanisms[0].use = true;

    if (!UsefulBuf_IsNULLOrEmptyC(public_key)) {
        mechanisms[1].key.cose_algorithm_id = T_COSE_ALGORITHM_ES256;
        result = suit_set_suit_key_from_cose_key(public_key, &mechanisms[1].key);
        if (result != SUIT_SUCCESS) {
            printf("main : Failed to create verification key of trust anchor. %s(%d)\n", suit_err_to_str(result), result);
            return EXIT_FAILURE;
        }
        mechanisms[1].cose_tag = CBOR_TAG_COSE_SIGN1;
        mechanisms[1].use = true;
    }

    // Read manifest file.
    printf("main : Read Manifest file.\n");
    manifest_buf = malloc(SUIT_MAX_DATA_SIZE);
    if (manifest_buf == NULL) {
        printf("main : Failed to allocate memory.\n");
        goto out;
    }
    size_t manifest_len = read_from_file(input_file, manifest_buf, SUIT_MAX_DATA_SIZE);
    if (manifest_len == 0) {
        printf("main : Failed to read Manifest file.\n");
        goto out;
    }
    suit_print_hex(manifest_buf, manifest_len);
    printf("\n\n");

    // Decode manifest file.
    printf("main : Decode Manifest file.\n");
    suit_decode_mode_t mode;
    mode.SKIP_AUTHENTICATION_FAILURE = 1;
    suit_envelope_t envelope = {0};
    suit_buf_t buf = {.ptr = manifest_buf, .len = manifest_len};
    result = suit_decode_envelope(mode, &buf, &envelope, mechanisms);
    if (result != SUIT_SUCCESS) {
        printf("main : Failed to parse Manifest file. %s(%d)\n", suit_err_to_str(result), result);
        return EXIT_FAILURE;
    }

    // Print manifest.
    printf("\nmain : Print Decoded Manifest.\n");
    result = suit_print_envelope(mode, &envelope, indent, tabstop);
    if (result != SUIT_SUCCESS) {
        printf("main : Failed to print Manifest file. %s(%d)\n", suit_err_to_str(result), result);
        return EXIT_FAILURE;
    }

    // Encode manifest.
    encode_buf = malloc(SUIT_MAX_DATA_SIZE);
    if (encode_buf == NULL) {
        printf("main : Failed to allocate memory.\n");
        goto out;
    }
    size_t encode_len = SUIT_MAX_DATA_SIZE;
    uint8_t *ret_pos = encode_buf;
    printf("\nmain : Encode Manifest.\n");
    result = suit_encode_envelope(mode, &envelope, mechanisms, &ret_pos, &encode_len);
    if (result != SUIT_SUCCESS) {
        printf("main : Failed to encode. %s(%d)\n", suit_err_to_str(result), result);
        return EXIT_FAILURE;
    }
    printf("main : Total buffer memory usage was %ld/%d bytes\n", ret_pos + encode_len - encode_buf, SUIT_MAX_DATA_SIZE);

    // Print manifest.
    /*
    printf("\nmain : Print Signed Manifest.\n");
    result = suit_print_envelope(mode, &envelope, indent, tabstop);
    if (result != SUIT_SUCCESS) {
        printf("main : Failed to print Manifest file. %s(%d)\n", suit_err_to_str(result), result);
        return EXIT_FAILURE;
    }
    */

    if (output_file != NULL) {
        write_to_file(output_file, ret_pos, encode_len);
    }
    ret = EXIT_SUCCESS;
out:
    if (manifest_buf != NULL) {
        free(manifest_buf);
    }
    if (encode_buf != NULL) {
        free(encode_buf);
    }
    suit_free_key(&mechanisms[0].key);
    printf("\n");
    return ret;
}
