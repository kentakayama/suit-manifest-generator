#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

SUIT_SIGN_TRUSTANCHOR := ../bin/suit/suit_manifest_sign_trustanchor
SUIT_MAC_TRUSTANCHOR := ../bin/suit/suit_manifest_mac_trustanchor
SUIT_SIGN_DELEGATE := ../bin/suit/suit_manifest_sign_delegate
SUIT_PROCESS := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_process

.PHONY: all
all:

.PRECIOUS: ../cbor/%.cbor
../cbor/%.cbor:
	$(MAKE) -C ../cbor $(notdir $@)

suit_manifest_expS1.suit: ../cbor/suit_manifest_expS1.cbor
	$(SUIT_SIGN_DELEGATE) $< $@

suit_manifest_aes_kw.suit suit_manifest_aes_kw_config.suit suit_manifest_aes_kw_content.suit:
	$(SUIT_MAC_TRUSTANCHOR) $< $@

%.suit: ../cbor/%.cbor
	$(SUIT_SIGN_TRUSTANCHOR) $< $@

.PHONY: test
test: $(SUIT_MANIFESTS) $(SUIT_PROCESS)
	@for m in $(SUIT_MANIFESTS); do \
		$(SUIT_PROCESS) $$m; \
	done

.PHONY: clean
clean:
	$(RM) *.suit
