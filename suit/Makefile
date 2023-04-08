#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

#SUIT_TOOL_DIR := ~/gitlab.arm.com/research/ietf-suit/suit-tool
#SUIT_TOOL := $(SUIT_TOOL_DIR)/bin/suit-tool
#PRIVATE_KEY := $(SUIT_TOOL_DIR)/private_key.pem

SUIT_SIGN := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_sign
SUIT_PROCESS := ~/github.com/kentakayama/libcsuit/bin/suit_manifest_process

SUIT_MANIFESTS := \
	suit_uri.suit \
	suit_integrated.suit \
	suit_personalization.suit \
	suit_unlink.suit \
	suit_manifest_raw.suit \
	suit_manifest_dependency.suit \
	suit_manifest_aes_kw.suit \
	suit_manifest_aes_kw_content.suit \
	suit_manifest_aes_kw_dependent.suit \
	suit_manifest_expS0.suit \
	suit_manifest_expS1.suit \
	suit_manifest_expS2.suit \
	suit_manifest_expS3.suit \
	suit_helloworld.suit

.PHONY: all
all: $(SUIT_MANIFESTS)

.PRECIOUS: ../cbor/%.cbor
../cbor/%.cbor:
	$(MAKE) -C ../cbor $(notdir $@)

%.suit: ../cbor/%.cbor
	$(SUIT_SIGN) $< $@
#	$(SUIT_TOOL) sign -m $< -k $(PRIVATE_KEY) -o $@

.PHONY: test
test: $(SUIT_MANIFESTS)
	@for m in $(SUIT_MANIFESTS); do \
		$(SUIT_PROCESS) $$m; \
	done

.PHONY: clean
clean:
	$(RM) $(SUIT_MANIFESTS)
