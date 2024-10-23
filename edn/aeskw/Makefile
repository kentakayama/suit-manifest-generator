#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: encrypted.envelope.cbor

# load generic rules
include ../scripts/common.mk

CC=musl-gcc -static
CFLAGS=-Os -Wall

# NOTE: if one target requires multiple sources,
# list them from direct source (e.g. gdiag requires rediag directly)

# generate SUIT_Envelope_Tagged
encrypted.envelope.gdiag: \
	encrypted.envelope.rediag \
	encrypted.manifest.digest.gdiag \
	encrypted.manifest.digest.mac.cose.gdiag \
	encrypted.manifest.gdiag \
	encrypted.a128kw.a128ctr.encrypt.bin.hdiag

# generate SUIT_Manifest
encrypted.manifest.gdiag: \
	encrypted.manifest.rediag \
	encrypted.a128kw.a128ctr.encrypt.cose.gdiag \
	hello.digest.hdiag \
	hello.size.gdiag

# generate SUIT_Digest of SUIT_Manifest
encrypted.manifest.digest.gdiag: \
	encrypted.manifest.digest.hdiag
encrypted.manifest.digest.hdiag: \
	encrypted.manifest.cbor

# generate hex file for integrated payload
encrypted.bin.hdiag: hello

# generate parameters for the hello world app
hello.size.gdiag: hello
hello.digest.hdiag: hello

# compile the hello world app
hello: hello.o
	$(CC) $(CFLAGS) -o $@ $<
	strip hello

hello.o: hello.c
	$(CC) $(CFLAGS) -c -o $@ $<

# generate encryption-info (and encrypted payload)
encrypted.a128kw.a128ctr.encrypt.cose: hello

# generate encrypted payload in hex
encrypted.a128kw.a128ctr.encrypt.bin.hdiag: encrypted.a128kw.a128ctr.encrypt.bin

.PHONY: test
test: all $(SUIT_MANIFEST_CDDL)
	@echo ${TEST_COMMAND} $<
	@if ${TEST_COMMAND} $<; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'encrypted.envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'encrypted.envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean: common-clean
	$(RM) hello hello.o
