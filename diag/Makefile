#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: $(GENERATED_DIAGS)

teep_update_uri.diag: ../untagged_suit/suit_uri.suit
teep_update_integrated.diag: ../untagged_suit/suit_integrated.suit
teep_update_personalization.diag: ../untagged_suit/suit_personalization.suit
teep_update_unlink.diag: ../untagged_suit/suit_unlink.suit
teep_update_helloworld.diag: ../untagged_suit/suit_helloworld.suit
suit_manifest_expS1.diag: ../teep/suit_delegation.cwt
suit_manifest_expS2.diag: ../suit/suit_manifest_expS1.suit
suit_manifest_expS3.diag: ../suit/suit_manifest_expS1.suit
suit_manifest_expS4.diag: ../suit/suit_manifest_expS1.suit
suit_personalization.diag: ../untagged_suit/suit_uri.suit

.PRECIOUS: ../untagged_suit/%.suit
../untagged_suit/%.suit:
	$(MAKE) -C ../untagged_suit $(notdir $@)

.PRECIOUS: ../suit/%.suit
../suit/%.suit:
	$(MAKE) -C ../suit $(notdir $@)

.PRECIOUS: ../teep/%.cwt
../teep/%.cwt:
	$(MAKE) -C ../teep $(notdir $@)

%.diag: ../ediag/%.ediag
	$(PYTHON3) ../ediag-to-diag.py $< > $@

FIXED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
	suit_unlink.diag \
	suit_delegation.diag \
	suit_manifest_expS0.diag \
	suit_manifest_run_sequence.diag \
	suit_manifest_raw.diag \
	suit_manifest_dependency.diag \
	suit_manifest_aes_kw_dependent.diag \
	suit_manifest_expU0.diag \
	suit_manifest_expU1.diag

.PHONY: clean
clean:
	ls | grep -v -e Makefile \
		-e suit_uri.diag \
		-e suit_integrated.diag \
		-e suit_unlink.diag \
		-e suit_delegation.diag \
		-e suit_manifest_expS0.diag \
		-e suit_manifest_run_sequence.diag \
		-e suit_manifest_raw.diag \
		-e suit_manifest_dependency.diag \
		-e suit_manifest_aes_kw_dependent.diag \
		-e suit_manifest_expU0.diag \
		-e suit_manifest_expU1.diag | xargs $(RM)
