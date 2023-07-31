#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: $(GENERATED_DIAGS)

teep_update_uri.diag: ../ediag/teep_update_uri.ediag ../untagged_suit/suit_uri.suit
teep_update_integrated.diag: ../ediag/teep_update_integrated.ediag ../untagged_suit/suit_integrated.suit
teep_update_personalization.diag: ../ediag/teep_update_personalization.ediag ../untagged_suit/suit_manifest_esdh_config.suit
teep_update_helloworld.diag: ../ediag/teep_update_helloworld.ediag ../untagged_suit/suit_helloworld.suit
suit_manifest_expS1.diag: ../ediag/suit_manifest_expS1.ediag ../teep/suit_delegation.cwt
suit_manifest_expS2.diag: ../ediag/suit_manifest_expS2.ediag ../suit/suit_manifest_expS1.suit
suit_manifest_expS3.diag: ../ediag/suit_manifest_expS3.ediag ../suit/suit_manifest_expS1.suit
suit_manifest_expS4.diag: ../ediag/suit_manifest_expS4.ediag ../suit/suit_manifest_expS1.suit
suit_personalization.diag: ../ediag/suit_personalization.ediag ../untagged_suit/suit_uri.suit
suit_manifest_aes_kw.diag: ../ediag/suit_manifest_aes_kw.ediag ../libcsuit/testfiles/encrypted_image_aes.bin ../libcsuit/testfiles/encryption_info_aes.cose
suit_manifest_aes_kw_content.diag: ../ediag/suit_manifest_aes_kw_content.ediag ../libcsuit/testfiles/encrypted_image_aes.bin ../libcsuit/testfiles/encryption_info_aes.cose
suit_manifest_aes_kw_config.diag: ../ediag/suit_manifest_aes_kw_config.ediag ../libcsuit/testfiles/encrypted_config_aes.bin ../libcsuit/testfiles/encryption_info_config_aes.cose
suit_manifest_esdh_content.diag: ../ediag/suit_manifest_esdh_content.ediag ../libcsuit/testfiles/encrypted_image_esdh.bin ../libcsuit/testfiles/encryption_info_esdh.cose
suit_manifest_esdh_config.diag: ../ediag/suit_manifest_esdh_config.ediag ../libcsuit/testfiles/encrypted_config_esdh.bin ../libcsuit/testfiles/encryption_info_config_esdh.cose
suit_manifest_esdh_dependency.diag: ../ediag/suit_manifest_esdh_dependency.ediag ../suit/suit_manifest_dependency_decrypt.suit ../teep/suit_delegation.cwt ../signed_diag/suit_manifest_dependency_decrypt.diag
suit_manifest_dependency_decrypt.diag: ../ediag/suit_manifest_dependency_decrypt.ediag ../libcsuit/testfiles/raw_image.bin
%.diag:
	$(PYTHON3) ../ediag-to-diag.py $< > $@

.PRECIOUS: ../untagged_suit/%.suit
../untagged_suit/%.suit:
	$(MAKE) -C ../untagged_suit $(notdir $@)

.PRECIOUS: ../suit/%.suit
../suit/%.suit:
	$(MAKE) -C ../suit $(notdir $@)

.PRECIOUS: ../teep/%.cwt
../teep/%.cwt:
	$(MAKE) -C ../teep $(notdir $@)

.PRECIOUS: ../signed_diag/%.diag
../signed_diag/%.diag:
	$(MAKE) -C ../signed_diag $(notdir $@)

FIXED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
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
	$(RM) \
	suit_helloworld.diag \
	suit_manifest_aes_kw_config.diag \
	suit_manifest_aes_kw_content.diag \
	suit_manifest_aes_kw.diag \
	suit_manifest_esdh_config.diag \
	suit_manifest_esdh_content.diag \
	suit_manifest_esdh_dependency.diag \
	suit_manifest_dependency_decrypt.diag \
	suit_manifest_expS1.diag \
	suit_manifest_expS2.diag \
	suit_manifest_expS3.diag \
	suit_manifest_expS4.diag \
	suit_personalization.diag \
	teep_update_example1.diag \
	teep_update_example3.diag \
	teep_update_helloworld.diag \
	teep_update_integrated.diag \
	teep_update_personalization.diag \
	teep_update_uri.diag
