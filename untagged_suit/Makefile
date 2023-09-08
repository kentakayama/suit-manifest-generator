#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

DIAG2CBOR := cbor-diag # https://github.com/Nullus157/cbor-diag-rs

UNTAGGED_SUIT_MANIFESTS := \
	suit_uri.suit \
	suit_integrated.suit \
	suit_personalization.suit \
	suit_manifest_aes_kw_config.suit \
	suit_manifest_esdh_config.suit

UNTAGGED_SUIT_MANIFESTS_IETF116_HACKATHON := \
	suit_helloworld.diag
ifeq ($(suit-ietf116), 1)
UNTAGGED_SUIT_MANIFESTS += $(UNTAGGED_SUIT_MANIFESTS_IETF116_HACKATHON)
endif

.PHONY: all
all: $(UNTAGGED_SUIT_MANIFESTS)

%.suit: ../untagged_diag/%.diag
	$(DIAG2CBOR) --to bytes --from diag < $< > $@

.PRECIOUS: ../untagged_diag/%.diag
../untagged_diag/%.diag:
	$(MAKE) -C ../untagged_diag $(notdir $@)

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_SUIT_MANIFESTS)
