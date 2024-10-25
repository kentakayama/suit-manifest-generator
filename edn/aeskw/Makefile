#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TARGET=aeskw.envelope.cbor
.PHONY: all
all: $(TARGET)

# load generic rules
include ../scripts/common.mk

CC=musl-gcc -static
CFLAGS=-Os -Wall

# list dependencies as prerequisites here
#
# NOTE: %.hdiag files and %.size.gdiag files are special: order sensitive
#       You need to start from the direct source
#       because the common.mk cannot automatically detect the
#       first input ($<) file to be used in the recipies

# the target depends on these materials
aeskw.envelope.cbor: \
	aeskw.envelope.rediag \
	aeskw.manifest.rediag \
	aeskw.manifest.digest.rediag \
	hello.c

# generate SUIT_Envelope_Tagged
aeskw.envelope.gdiag: \
	aeskw.envelope.rediag \
	aeskw.manifest.digest.gdiag \
	aeskw.manifest.digest.mac.cose.gdiag \
	aeskw.manifest.gdiag \
	a128ctr.bin.hdiag

# generate SUIT_Manifest
aeskw.manifest.gdiag: \
	aeskw.manifest.rediag \
	a128kw.a128ctr.cose.gdiag \
	hello.digest.hdiag \
	hello.size.gdiag

# generate SUIT_Digest of SUIT_Manifest
aeskw.manifest.digest.gdiag: aeskw.manifest.digest.hdiag
aeskw.manifest.digest.hdiag: aeskw.manifest.cbor

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
a128kw.a128ctr.cose: hello

# generate encrypted payload in hex
a128ctr.bin.hdiag: a128ctr.bin

.PHONY: test
test: all $(SUIT_MANIFEST_CDDL)
	@echo ${TEST_COMMAND} ${TARGET}
	@if ${TEST_COMMAND} ${TARGET}; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'aeskw.envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'aeskw.envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean: common-clean
	$(RM) hello hello.o *.bin
