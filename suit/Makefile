#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

SUIT_SIGN := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_sign
SUIT_PROCESS := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_process

.PHONY: all
all:

.PRECIOUS: ../cbor/%.cbor
../cbor/%.cbor:
	$(MAKE) -C ../cbor $(notdir $@)

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
