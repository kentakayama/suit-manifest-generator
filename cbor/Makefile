#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

DIAG2CBOR := cbor-diag # https://github.com/Nullus157/cbor-diag-rs

FIXED_CBORS := \
	suit_manifest_exp1.cbor \
	suit_manifest_exp3.cbor

GENERATED_CBORS += \
	suit_uri.cbor \
	suit_integrated.cbor \
	suit_personalization.cbor \
	suit_unlink.cbor \
	suit_manifest_raw.cbor \
	suit_manifest_dependency.cbor \
	suit_manifest_aes_kw.cbor \
	suit_manifest_aes_kw_dependent.cbor \
	suit_manifest_expD00.cbor \
	suit_manifest_expD01.cbor \
	suit_manifest_expID01.cbor \
	teep_update_example1.cbor \
	teep_update_example3.cbor \
	suit_helloworld.cbor \
	teep_update_helloworld.cbor

.PHONY: all
all: $(GENERATED_CBORS)

../diag/%.diag:
	$(MAKE) -C ../diag $(notdir $@)

%.cbor: ../diag/%.diag
	$(DIAG2CBOR) --to bytes --from diag < $< > $@

.PHONY: clean
clean:
	$(RM) $(GENERATED_CBORS)
