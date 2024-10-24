#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TARGET=hello.envelope.cbor
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

# generate SUIT_Envelope_Tagged cbor binary
hello.envelope.cbor: \
	hello.envelope.rediag \
	hello.manifest.rediag \
	hello.manifest.digest.rediag \
	hello.c

# generate SUIT_Envelope_Tagged
hello.envelope.gdiag: \
	hello.envelope.rediag \
	hello.manifest.digest.gdiag \
	hello.manifest.digest.mac.cose.gdiag \
	hello.manifest.gdiag \
	hello.bin.hdiag

# generate SUIT_Manifest
hello.manifest.gdiag: \
	hello.manifest.rediag \
	hello.digest.hdiag \
	hello.size.gdiag

# generate SUIT_Digest of SUIT_Manifest
hello.manifest.digest.gdiag: hello.manifest.digest.hdiag
hello.manifest.digest.hdiag: hello.manifest.cbor

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
	@echo ${TEST_COMMAND} ${TARGET}
	@if ${TEST_COMMAND} ${TARGET}; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'hello.envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'hello.envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean: common-clean
	$(RM) hello hello.o
