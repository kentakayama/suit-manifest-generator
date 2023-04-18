#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

SUIT_SIGN := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_sign
SUIT_SIGN_DELEGATE := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_sign_delegate
SUIT_PROCESS := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_process

.PHONY: all
all:

.PRECIOUS: ../cbor/%.cbor
../cbor/%.cbor:
	$(MAKE) -C ../cbor $(notdir $@)

suit_manifest_expS1.suit: ../cbor/suit_manifest_expS1.cbor
	$(SUIT_SIGN_DELEGATE) $< $@

%.suit: ../cbor/%.cbor
	$(SUIT_SIGN) $< $@

.PHONY: test
test: $(SUIT_MANIFESTS)
	@for m in $(SUIT_MANIFESTS); do \
		$(SUIT_PROCESS) $$m; \
	done

.PHONY: clean
clean:
	$(RM) *.suit
