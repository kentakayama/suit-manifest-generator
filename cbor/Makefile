#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

DIAG2CBOR := cbor-diag # https://github.com/Nullus157/cbor-diag-rs

FIXED_CBORS := \
	suit_manifest_exp1.cbor \
	suit_manifest_exp3.cbor

ifeq ($(suit),1)
GENERATED_CBORS += \
	suit_uri.cbor \
	suit_integrated.cbor \
	suit_personalization.cbor \
	suit_unlink.cbor \
	suit_manifest_raw.cbor \
	suit_manifest_dependency.cbor \
	suit_manifest_aes_kw.cbor \
	suit_manifest_aes_kw_dependent.cbor
endif

ifeq ($(teep),1)
GENERATED_CBORS += \
	teep_update_example1.cbor \
	teep_update_example3.cbor
endif

ifeq ($(suit-ietf116),1)
GENERATED_CBORS += \
	suit_helloworld.cbor
endif

ifeq ($(teep-ietf116),1)
GENERATED_CBORS += \
	teep_update_helloworld.cbor
endif

.PHONY: all
all: $(GENERATED_CBORS)

%.cbor: ../diag/%.diag
	$(DIAG2CBOR) --to bytes --from diag < $< > $@

.PHONY: clean
clean:
	$(RM) $(GENERATED_CBORS)
