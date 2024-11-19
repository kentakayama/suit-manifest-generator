#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TARGET=update.envelope.cbor
.PHONY: all
all: $(TARGET)

# load generic rules
include ../scripts/common.mk

# list dependencies as prerequisites here
#
# NOTE: %.hdiag files and %.size.gdiag files are special: order sensitive
#       You need to start from the direct source
#       because the common.mk cannot automatically detect the
#       first input ($<) file to be used in the recipies

# generate SUIT_Envelope_Tagged cbor binary
update.envelope.cbor: \
	update.envelope.rediag \
	update.manifest.rediag \
	update.manifest.digest.rediag

# generate SUIT_Envelope_Tagged
update.envelope.gdiag: \
	update.envelope.rediag \
	update.manifest.digest.gdiag \
	update.manifest.digest.es256.cose.gdiag \
	update.manifest.gdiag \
	raw_image.bin.hdiag

# generate SUIT_Manifest
update.manifest.gdiag: \
	update.manifest.rediag \
	update.digest.hdiag \
	update.size.gdiag

# generate SUIT_Digest of SUIT_Manifest
update.manifest.digest.gdiag: update.manifest.digest.hdiag
update.manifest.digest.hdiag: update.manifest.cbor

# generate hex file for integrated payload
raw_image.bin.hdiag: raw_image.bin

# generate parameters for the update world app
update.size.gdiag: raw_image.bin
update.digest.hdiag: raw_image.bin


.PHONY: test
test: all $(SUIT_MANIFEST_CDDL)
	@echo ${TEST_COMMAND} ${TARGET}
	@if ${TEST_COMMAND} ${TARGET}; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'update.envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'update.envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean: common-clean

