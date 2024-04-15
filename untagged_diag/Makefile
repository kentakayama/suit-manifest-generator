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

LIBCSUIT_DIR := ~/github.com/kentakayama/libcsuit
TEEP_PROTOCOL_DIR := ~/github.com/ietf-teep/teep-protocol

.PRECIOUS: $(UNTAGGED_DIAGS)

.PHONY: all
all: $(UNTAGGED_DIAGS)

../signed_diag/%.diag:
	@echo make $@
	$(MAKE) -C ../signed_diag $(notdir $@)

suit_manifest_aes_kw_config.diag: ../ciphertext/encrypted_config_aeskw_gcm.bin ../ciphertext/encryption_info_config_aeskw_gcm.cose
suit_manifest_esdh_config.diag: ../ciphertext/encrypted_config_esdh_ctr.bin ../ciphertext/encryption_info_config_esdh_ctr.cose

.PRECIOUS: ../signed_diag/%.diag
%.diag: ../signed_diag/%.diag
	@echo $@ depends $<
	sed -e "s?/ SUIT_Envelope_Tagged / 107(?/ SUIT_Envelope / ?" -e "s/})$$/}/" $< > $@

.PHONY: install-example1
install-example1: suit_uri.diag ../untagged_suit/suit_uri.suit
	@echo Example 1
	$(eval DIAG := suit_uri.diag)
	$(eval SUIT := ../untagged_suit/suit_uri.suit)
	$(eval FILENAME := $(LIBCSUIT_DIR)/testfiles/suit_manifest_expU.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: SUIT Manifest pointing to URI of the Trusted Component Binary {#suit-uri}\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(FILENAME)
	cat $(DIAG) >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p $(SUIT) >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp $(SUIT) $(FILENAME:.md=.cbor)
	cp $(DIAG) $(TEEP_PROTOCOL_DIR)/cbor/$(DIAG:.diag=.diag.txt)
	xxd -u -p $(SUIT) > $(TEEP_PROTOCOL_DIR)/cbor/$(DIAG:.diag=.hex.txt)

.PHONY: install-example2
install-example2: suit_integrated.diag ../untagged_suit/suit_integrated.suit
	@echo Example 2
	$(eval DIAG := suit_integrated.diag)
	$(eval SUIT := ../untagged_suit/suit_integrated.suit)
	$(eval FILENAME := $(LIBCSUIT_DIR)/testfiles/suit_manifest_expI.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 2: SUIT Manifest including the Trusted Component Binary {#suit-integrated}\n\n~~~~" > $(FILENAME)
	cat $(DIAG) >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p $(SUIT) >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp $(SUIT) $(FILENAME:.md=.cbor)
	cp $(DIAG) $(TEEP_PROTOCOL_DIR)/cbor/$(DIAG:.diag=.diag.txt)
	xxd -u -p $(SUIT) > $(TEEP_PROTOCOL_DIR)/cbor/$(DIAG:.diag=.hex.txt)

.PHONY: install-example3
install-example3: suit_manifest_esdh_config.diag ../untagged_suit/suit_manifest_esdh_config.suit
	@echo Example 3
	$(eval DIAG := suit_manifest_esdh_config.diag)
	$(eval SUIT := ../untagged_suit/suit_manifest_esdh_config.suit)
	$(eval FILENAME := $(LIBCSUIT_DIR)/testfiles/suit_manifest_expD.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 3: Supplying Personalization Data for Trusted Component Binary {#suit-personalization}\n\n~~~~" > $(FILENAME)
	cat $(DIAG) >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p $(SUIT) >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp $(SUIT) $(FILENAME:.md=.cbor)
	cp $(DIAG) $(TEEP_PROTOCOL_DIR)/cbor/suit_personalization.diag.txt
	xxd -u -p $(SUIT) > $(TEEP_PROTOCOL_DIR)/cbor/suit_personalization.hex.txt

.PHONY: install
install: $(UNTAGGED_DIAGS)
	$(MAKE) install-example1
	$(MAKE) install-example2
	$(MAKE) install-example3

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS) $(UNTAGGED_DIAGS_IETF116_HACKATHON)

