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
	suit_unlink.suit \
	suit_helloworld.suit

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
