#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

SUIT_TOOL_DIR := ~/gitlab.arm.com/research/ietf-suit/suit-tool
SUIT_TOOL := $(SUIT_TOOL_DIR)/bin/suit-tool
PRIVATE_KEY := $(SUIT_TOOL_DIR)/private_key.pem

SUIT_MANIFESTS := \
	suit_uri.suit \
	suit_integrated.suit \
	suit_personalization.suit \
	suit_unlink.suit \
	suit_manifest_raw.suit \
	suit_manifest_dependency.suit \
	suit_manifest_aes_kw.suit \
	suit_manifest_aes_kw_dependent.suit

ifeq ($(suit-ietf116),1)
SUIT_MANIFESTS += \
	suit_helloworld.suit
endif

.PHONY: all
all: $(SUIT_MANIFESTS)

../cbor/%.cbor:
	$(MAKE) -C ../cbor $(notdir $@)

%.suit: ../cbor/%.cbor
	$(SUIT_TOOL) sign -m $< -k $(PRIVATE_KEY) -o $@

.PHONY: clean
clean:
	$(RM) $(SUIT_MANIFESTS)
