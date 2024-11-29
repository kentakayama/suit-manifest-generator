#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TARGET=comp-meta.envelope.cbor
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
comp-meta.envelope.cbor: \
	comp-meta.envelope.rediag \
	comp-meta.manifest.rediag \
	comp-meta.manifest.digest.rediag

# generate SUIT_Envelope_Tagged
comp-meta.envelope.gdiag: \
	comp-meta.envelope.rediag \
	comp-meta.manifest.digest.gdiag \
	comp-meta.manifest.digest.es256.cose.gdiag \
	comp-meta.manifest.gdiag \
	raw_image.bin.hdiag

# generate SUIT_Manifest
comp-meta.manifest.gdiag: \
	comp-meta.manifest.rediag \
	comp-meta.digest.hdiag \
	comp-meta.size.gdiag

# generate SUIT_Digest of SUIT_Manifest
comp-meta.manifest.digest.gdiag: comp-meta.manifest.digest.hdiag
comp-meta.manifest.digest.hdiag: comp-meta.manifest.cbor

# generate hex file for integrated payload
raw_image.bin.hdiag: raw_image.bin

# generate parameters for the comp-meta world app
comp-meta.size.gdiag: raw_image.bin
comp-meta.digest.hdiag: raw_image.bin


.PHONY: test
test: all $(SUIT_MANIFEST_CDDL)
	@echo ${TEST_COMMAND} ${TARGET}
	@if ${TEST_COMMAND} ${TARGET}; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'comp-meta.envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'comp-meta.envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean: common-clean

LIBCSUIT_DIR := ~/github.com/kentakayama/libcsuit/
.PHONY: install
install: $(TARGET)
	@echo SUIT Update Management Example 3
	$(eval TARGET := suit_manifest_expU3)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2024 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 3: Component Metadata Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\nNOTE: only SUIT_Manifest part is displayed here.\n\n~~~~" > $(MD)
	cat ${<:.envelope.cbor=.manifest.rediag} >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p $< >> $(MD)
	echo "~~~~" >> $(MD)
	cp $< $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
