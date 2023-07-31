#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

UNTAGGED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
	suit_personalization.diag \
	suit_manifest_aes_kw_config.diag \
	suit_manifest_esdh_config.diag

UNTAGGED_DIAGS_IETF116_HACKATHON := \
	suit_helloworld.diag

ifeq ($(suit-ietf116),1)
UNTAGGED_DIAGS += $(UNTAGGED_DIAGS_IETF116_HACKATHON)
endif

.PRECIOUS: $(UNTAGGED_DIAGS)

.PHONY: all
all: $(UNTAGGED_DIAGS)

../signed_diag/%.diag:
	@echo make $@
	$(MAKE) -C ../signed_diag $(notdir $@)

suit_manifest_aes_kw_config.diag: ../libcsuit/testfiles/encrypted_config_aes.bin ../libcsuit/testfiles/encryption_info_config_aes.cose
suit_manifest_esdh_config.diag: ../libcsuit/testfiles/encrypted_config_esdh.bin ../libcsuit/testfiles/encryption_info_config_esdh.cose

.PRECIOUS: ../signed_diag/%.diag
%.diag: ../signed_diag/%.diag
	@echo $@ depends $<
	sed -e "s?/ SUIT_Envelope_Tagged / 107(?/ SUIT_Envelope / ?" -e "s/})$$/}/" $< > $@

.PHONY: install
install: $(UNTAGGED_DIAGS)
	@echo Example 1
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expU.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: SUIT Manifest pointing to URI of the Trusted Component Binary {#suit-uri}\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(FILENAME)
	cat suit_uri.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_uri.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_uri.suit $(FILENAME:.md=.cbor)
	$(eval FILENAME := ../../../ietf-teep/teep-protocol/cbor/suit_uri.diag.txt)
	cp ../untagged_diag/suit_uri.diag $(FILENAME)
	xxd -u -p ../untagged_suit/suit_uri.suit > $(FILENAME:.diag.txt=.hex.txt)
	@echo Example 2
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expI.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 2: SUIT Manifest including the Trusted Component Binary {#suit-integrated}\n\n~~~~" > $(FILENAME)
	cat suit_integrated.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_integrated.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_integrated.suit $(FILENAME:.md=.cbor)
	$(eval FILENAME := ../../../ietf-teep/teep-protocol/cbor/suit_integrated.diag.txt)
	cp ../untagged_diag/suit_integrated.diag $(FILENAME)
	xxd -u -p ../untagged_suit/suit_integrated.suit > $(FILENAME:.diag.txt=.hex.txt)
	@echo Example 3
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expD.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 3: Supplying Personalization Data for Trusted Component Binary {#suit-personalization}\n\n~~~~" > $(FILENAME)
	cat suit_personalization.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_personalization.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_personalization.suit $(FILENAME:.md=.cbor)
	$(eval FILENAME := ../../../ietf-teep/teep-protocol/cbor/suit_personalization.diag.txt)
	cp ../untagged_diag/suit_manifest_aes_kw_config.diag $(FILENAME)
	xxd -u -p ../untagged_suit/suit_manifest_aes_kw_config.suit > $(FILENAME:.diag.txt=.hex.txt)

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS) $(UNTAGGED_DIAGS_IETF116_HACKATHON)

