#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: $(GENERATED_DIAGS)

teep_update_uri.diag: ../untagged_suit/suit_uri.suit
teep_update_integrated.diag: ../untagged_suit/suit_integrated.suit
teep_update_personalization.diag: ../untagged_suit/suit_manifest_esdh_config.suit
teep_update_helloworld.diag: ../untagged_suit/suit_helloworld.suit
suit_manifest_expS2.diag: ../suit/suit_manifest_expS0.suit
suit_manifest_expS3.diag: ../suit/suit_manifest_expS0.suit
suit_manifest_expS4.diag: ../suit/suit_manifest_expS0.suit
suit_personalization.diag: ../untagged_suit/suit_uri.suit
suit_manifest_aes_kw.diag: ../libcsuit/testfiles/encrypted_image_aes.bin ../libcsuit/testfiles/encryption_info_aes.cose
suit_manifest_aes_kw_content.diag: ../libcsuit/testfiles/encrypted_image_aes.bin ../libcsuit/testfiles/encryption_info_aes.cose
suit_manifest_aes_kw_config.diag: ../libcsuit/testfiles/encrypted_config_aes.bin ../libcsuit/testfiles/encryption_info_config_aes.cose
suit_manifest_esdh_content.diag: ../libcsuit/testfiles/encrypted_image_esdh.bin ../libcsuit/testfiles/encryption_info_esdh.cose
suit_manifest_esdh_config.diag: ../ciphertext/encryption_info_config_esdh_ctr.cose ../ciphertext/encrypted_config_esdh_ctr.bin
suit_manifest_esdh_dependency.diag: ../suit/suit_manifest_dependency_decrypt.suit ../signed_diag/suit_manifest_dependency_decrypt.diag
suit_manifest_dependency_decrypt.diag: ../libcsuit/testfiles/raw_image.bin

%.diag: ../ediag/%.ediag
	$(PYTHON3) ../scripts/ediag-to-diag.py $< > $@

#../ciphertext/%.cose:
#	$(MAKE) -C ../ciphertext $(notdir $@)

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
