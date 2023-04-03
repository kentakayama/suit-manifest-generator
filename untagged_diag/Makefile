#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

UNTAGGED_DIAGS := \
	suit_uri.untagged.diag \
	suit_integrated.untagged.diag \
	suit_personalization.untagged.diag \
	suit_unlink.untagged.diag

ifeq ($(suit-ietf116),1)
UNTAGGED_DIAGS += \
	suit_helloworld.untagged.diag
endif

.PHONY: all
all: $(UNTAGGED_DIAGS)

../signed_diag/%.diag:
	@echo make $@
	$(MAKE) -C ../signed_diag $(notdir $@)

%.untagged.diag: ../signed_diag/%.diag
	@echo $@ depends $<
	sed -e "s?/ SUIT_Envelope_Tagged / 107(?/ SUIT_Envelope / ?" -e "s/})$$/}/" $< > $@

.PHONY: install
install: $(UNTAGGED_DIAGS)
	@echo Example 1
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expU.md)
	echo "\n## Example 1: SUIT Manifest pointing to URI of the Trusted Component Binary {#suit-uri}\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(FILENAME)
	cat suit_uri.untagged.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_uri.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_uri.suit $(FILENAME:.md=.cbor)
	@echo Example 2
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expI.md)
	echo "\n## Example 2: SUIT Manifest including the Trusted Component Binary {#suit-integrated}\n\n~~~~" > $(FILENAME)
	cat suit_integrated.untagged.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_integrated.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_integrated.suit $(FILENAME:.md=.cbor)
	@echo Example 3
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expD.md)
	echo "\n## Example 3: Supplying Personalization Data for Trusted Component Binary {#suit-personalization}\n\n~~~~" > $(FILENAME)
	cat suit_personalization.untagged.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_personalization.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_personalization.suit $(FILENAME:.md=.cbor)
	@echo Example 4
	$(eval FILENAME := ../../libcsuit/testfiles/suit_manifest_expR.md)
	echo "\n## E.4. Example 4: Unlink a Trusted Component {#suit-unlink}\n\n~~~~" > $(FILENAME)
	cat suit_unlink.untagged.diag >> $(FILENAME)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(FILENAME)
	xxd -u -p ../untagged_suit/suit_unlink.suit >> $(FILENAME)
	echo "~~~~" >> $(FILENAME)
	cp ../untagged_suit/suit_unlink.suit $(FILENAME:.md=.cbor)

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS)
