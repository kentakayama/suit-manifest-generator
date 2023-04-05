#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

UNTAGGED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
	suit_personalization.diag \
	suit_unlink.diag \
	suit_manifest_raw.diag \
	suit_manifest_dependency.diag \
	suit_manifest_aes_kw.diag \
	suit_manifest_aes_kw_content.diag \
	suit_manifest_aes_kw_dependent.diag \
	suit_manifest_expD00.diag \
	suit_manifest_expD01.diag \
	suit_manifest_expID01.diag

ifeq ($(suit-ietf116), 1)
UNTAGGED_DIAGS += \
	suit_helloworld.diag
endif


.PHONY: all
all: $(UNTAGGED_DIAGS)

.PRECIOUS: ../suit/%.suit
../suit/%.suit:
	$(MAKE) -C ../suit $(notdir $@)

%.diag: ../suit/%.suit
	sed -e "s?/ authentication-wrapper /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / SHA256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 13 -l 32 $<)'\n    ] >>,\n    << / COSE_Sign1_Tagged / 18\([\n      / protected: / << {\n        / algorithm-id / 1: -7 / ES256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / signature: / h'$(shell xxd -p -u -c 64 -s 57 -l 64 $<)'\n    ]\) >>\n  ] >>,?" ../diag/$@ > $@

.PHONY: install
install:
	@echo AES-KW content Example
	cp suit_manifest_aes_kw_content.diag ../../../suit-wg/suit-firmware-encryption/examples/suit-manifest-aes-kw-content.diag.signed
	cp ../suit/suit_manifest_aes_kw_content.suit ../../libcsuit/testfiles/suit_manifest_expEW.cbor
	xxd -p -u ../suit/suit_manifest_aes_kw_content.suit ../../../suit-wg/suit-firmware-encryption/examples/suit-manifest-aes-kw-content.hex.signed
	@echo AES-KW fetch Example
	cp suit_manifest_aes_kw.diag ../../../suit-wg/suit-firmware-encryption/examples/suit-manifest-aes-kw.diag.signed
	cp ../suit/suit_manifest_aes_kw.suit ../../libcsuit/testfiles/suit_manifest_expEF.cbor
	xxd -p -u ../suit/suit_manifest_aes_kw.suit ../../../suit-wg/suit-firmware-encryption/examples/suit-manifest-aes-kw.hex.signed

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS)
