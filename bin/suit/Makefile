#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: suit_manifest_sign_trustanchor suit_manifest_sign_delegate suit_manifest_mac_trustanchor

CRYPTO_LIB = -lmbedcrypto

CFLAGS = $(CMD_CFLAGS) -I./inc -g -DLIBCSUIT_PSA_CRYPTO_C=1
LDFLAGS = $(CMD_LDFLAGS) -lcsuit -lt_cose $(CRYPTO_LIB) -lqcbor -lm

suit_manifest_sign_trustanchor:
	$(CC) $(CFLAGS) -o suit_examples_common.o -c suit_examples_common.c
	$(CC) $(CFLAGS) -o suit_manifest_sign_trustanchor.o -c suit_manifest_sign_main.c -DSUIT_MANIFEST_SIGNER_TRUST_ANCHOR=1
	$(CC) -o $@ suit_manifest_sign_trustanchor.o suit_examples_common.o $(LDFLAGS)

suit_manifest_sign_delegate:
	$(CC) $(CFLAGS) -o suit_examples_common.o -c suit_examples_common.c
	$(CC) $(CFLAGS) -o suit_manifest_sign_delegate.o -c suit_manifest_sign_main.c -DSUIT_MANIFEST_SIGNER_TAM=1
	$(CC) -o $@ suit_manifest_sign_delegate.o suit_examples_common.o $(LDFLAGS)

suit_manifest_mac_trustanchor:
	$(CC) $(CFLAGS) -o suit_examples_common.o -c suit_examples_common.c
	$(CC) $(CFLAGS) -o suit_manifest_mac_trustanchor.o -c suit_manifest_mac_main.c -DSUIT_MANIFEST_SIGNER_TRUST_ANCHOR=1
	$(CC) -o $@ suit_manifest_mac_trustanchor.o suit_examples_common.o $(LDFLAGS)

.PHONY: clean
clean:
	$(RM) suit_manifest_sign_trustanchor suit_manifest_sign_delegate suit_manifest_mac_trustanchor *.o

