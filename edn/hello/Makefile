#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: hello.envelope.cbor

# load generic rules
include ../scripts/common.mk

CC=musl-gcc -static
CFLAGS=-Os -Wall

# NOTE: if one target requires multiple sources,
# list them from direct source (e.g. gdiag requires rediag directly)

# generate SUIT_Envelope_Tagged
hello.envelope.gdiag: \
	hello.envelope.rediag \
	hello.manifest.digest.gdiag \
	hello.manifest.digest.mac.mdiag \
	hello.manifest.gdiag \
	hello.bin.hdiag

# generate SUIT_Manifest
hello.manifest.gdiag: \
	hello.manifest.rediag \
	hello.digest.hdiag \
	hello.size.gdiag


# generate hex file for integrated payload
hello.bin.hdiag: hello

# generate parameters for the hello world app
hello.size.gdiag: hello
hello.digest.hdiag: hello

# compile the hello world app
hello: hello.o
	$(CC) $(CFLAGS) -o $@ $<
	strip hello

hello.o: hello.c
	$(CC) $(CFLAGS) -c -o $@ $<


.PHONY: test
test: all $(SUIT_MANIFEST_CDDL)
	@echo ${TEST_COMMAND} $<
	@if ${TEST_COMMAND} $<; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'hello.envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'hello.envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean: common-clean
	$(RM) hello hello.o
