#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

LIBCSUIT_DIR := ~/github.com/kentakayama/libcsuit/
SUIT_MULTIPLE_TRUST_DOMAIN_DIR := ~/github.com/suit-wg/suit-multiple-trust-domains/
SUIT_FIRMWARE_ENCRYPTION_DIR := ~/github.com/suit-wg/suit-firmware-encryption/
SUIT_UPDATE_MANAGEMENT_DIR := ~/github.com/suit-wg/suit-update-management/

UNTAGGED_DIAGS := \
	suit_manifest_exp0.diag \
	suit_manifest_exp1.diag \
	suit_manifest_exp2A.diag \
	suit_manifest_exp2B.diag \
	suit_manifest_exp3.diag \
	suit_manifest_exp4.diag \
	suit_manifest_exp5.diag \
	suit_uri.diag \
	suit_integrated.diag \
	suit_personalization.diag \
	suit_manifest_raw.diag \
	suit_manifest_dependency.diag \
	suit_manifest_aes_kw.diag \
	suit_manifest_aes_kw_slot.diag \
	suit_manifest_aes_kw_content.diag \
	suit_manifest_aes_kw_config.diag \
	suit_manifest_esdh_content.diag \
	suit_manifest_esdh_dependency.diag \
	suit_manifest_dependency_decrypt.diag \
	suit_manifest_esdh_config.diag \
	suit_manifest_expS0.diag \
	suit_manifest_expS2.diag \
	suit_manifest_expS3.diag \
	suit_manifest_expS4.diag \
	suit_manifest_expU0.diag \
	suit_manifest_expU1.diag \
	suit_manifest_run_sequence.diag

UNTAGGED_DIAGS_IETF116_HACKATHON := \
	suit_helloworld.diag
ifeq ($(suit-ietf116), 1)
UNTAGGED_DIAGS += $(UNTAGGED_DIAGS_IETF116_HACKATHON)
endif


.PHONY: all
all: $(UNTAGGED_DIAGS)

.PRECIOUS: ../suit/%.suit
../suit/%.suit:
	$(MAKE) -C ../suit $(notdir $@)

.PRECIOUS: ../diag/%.diag
../diag/%.diag:
	$(MAKE) -C ../diag $(notdir $@)


# track dependency files
suit_manifest_esdh_dependency.diag: ../ediag/${@:.diag=.ediag} ../teep/suit_delegation.cwt ../libcsuit/testfiles/encrypted_image_esdh.bin ../libcsuit/testfiles/encryption_info_esdh.cose ../ediag/suit_manifest_dependency_decrypt.ediag ../ediag/suit_manifest_dependency_decrypt.ediag

# use COSE_Mac0
suit_manifest_aes_kw_content.diag: ../suit/suit_manifest_aes_kw_content.suit
suit_manifest_aes_kw.diag: ../suit/suit_manifest_aes_kw.suit
suit_manifest_aes_kw_slot.diag: ../suit/suit_manifest_aes_kw_slot.suit
suit_manifest_aes_kw_config.diag: ../suit/suit_manifest_aes_kw_config.suit

suit_manifest_aes_kw.diag suit_manifest_aes_kw_slot.diag suit_manifest_aes_kw_content.diag suit_manifest_aes_kw_config.diag:
	sed -e "s?/ AUTHENTICATION-WRAPPER /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / SHA256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 13 -l 32 $<)'\n    ] >>,\n    << / COSE_Mac0_Tagged / 17\([\n      / protected: / << {\n        / algorithm-id / 1: 5 / HMAC256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / tag: / h'$(shell xxd -p -u -c 64 -s 57 -l 32 $<)'\n    ]\) >>\n  ] >>,?" ../diag/$@ > $@


# do not use delegation chain
%.diag: ../suit/%.suit
	sed -e "s?/ AUTHENTICATION-WRAPPER /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / SHA256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 13 -l 32 $<)'\n    ] >>,\n    << / COSE_Sign1_Tagged / 18\([\n      / protected: / << {\n        / algorithm-id / 1: -7 / ES256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / signature: / h'$(shell xxd -p -u -c 64 -s 57 -l 64 $<)'\n    ]\) >>\n  ] >>,?" ../diag/$@ > $@

.PHONY: install
install: install_manifest install_multiple install_encryption install_update

.PHONY: install_manifest
install_manifest: suit_manifest_exp0.diag suit_manifest_exp1.diag suit_manifest_exp2A.diag suit_manifest_exp2B.diag suit_manifest_exp3.diag suit_manifest_exp4.diag suit_manifest_exp5.diag 
	@echo Example 0
	$(eval SOURCE := suit_manifest_exp0)
	$(eval TARGET := suit_manifest_exp0)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## B.1. Example 0: Secure Boot\nhttps://tools.ietf.org/html/draft-ietf-suit-manifest-27#appendix-B.1\n\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Example 1
	$(eval SOURCE := suit_manifest_exp1)
	$(eval TARGET := suit_manifest_exp1)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## B.2. Example 1: Simultaneous Download and Installation of Payload\nhttps://tools.ietf.org/html/draft-ietf-suit-manifest-27#appendix-B.2\n\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Example 2
	$(eval SOURCE := suit_manifest_exp2)
	$(eval TARGET := suit_manifest_exp2)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET)B.md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## B.3. Example 2: Simultaneous Download, Installation, Secure Boot, Severed Fields\nhttps://tools.ietf.org/html/draft-ietf-suit-manifest-27#appendix-B.3\n\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE)B.diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE)B.suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE)B.suit $(LIBCSUIT_DIR)/testfiles/$(TARGET)B.cbor
	cp ../suit/$(SOURCE)A.suit $(LIBCSUIT_DIR)/testfiles/$(TARGET)A.cbor
	@echo Example 3
	$(eval SOURCE := suit_manifest_exp3)
	$(eval TARGET := suit_manifest_exp3)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## B.4. Example 3: A/B images\nhttps://tools.ietf.org/html/draft-ietf-suit-manifest-27#appendix-B.4\n\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Example 3
	$(eval SOURCE := suit_manifest_exp4)
	$(eval TARGET := suit_manifest_exp4)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## B.5. Example 4: Load from External Storage\n\nhttps://tools.ietf.org/html/draft-ietf-suit-manifest-27#appendix-B.5\n\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Example 3
	$(eval SOURCE := suit_manifest_exp5)
	$(eval TARGET := suit_manifest_exp5)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## B.6. Example 5: Two Images\n\nhttps://tools.ietf.org/html/draft-ietf-suit-manifest-27#appendix-B.6\n\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor

.PHONY: install_multiple
install_multiple: suit_manifest_expS0.diag suit_manifest_expS2.diag suit_manifest_expS3.diag suit_manifest_expS4.diag
	@echo Simple Example
	$(eval SOURCE := suit_manifest_expS0)
	$(eval TARGET := suit_manifest_expS0)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 0: Basic Content+Write Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Simple Example
	$(eval SOURCE := suit_manifest_expS2)
	$(eval TARGET := suit_manifest_expS2)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 2: Basic Dependency Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Integrated Dependency Example
	$(eval SOURCE := suit_manifest_expS3)
	$(eval TARGET := suit_manifest_expS3)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 3: Integrated Dependency Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo Integrated Dependency Example
	$(eval SOURCE := suit_manifest_expS4)
	$(eval TARGET := suit_manifest_expS4)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 4: Is Dependency Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor

.PHONY: install_encryption
install_encryption: suit_manifest_aes_kw_content.diag suit_manifest_aes_kw.diag suit_manifest_aes_kw_slot.diag suit_manifest_esdh_content.diag suit_manifest_esdh_dependency.diag suit_manifest_dependency_decrypt.diag
	@echo AES-KW content Example
	$(eval SOURCE := suit_manifest_aes_kw_content)
	$(eval TARGET := suit-manifest-aes-kw-content)
	$(eval CSUITNAME := suit_manifest_expAW)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 0: Write and Decrypt AES-KW + Encrypted Payload\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).hex.signed
	@echo AES-KW fetch Example
	$(eval SOURCE := suit_manifest_aes_kw)
	$(eval TARGET := suit-manifest-aes-kw)
	$(eval CSUITNAME := suit_manifest_expAF)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: Fetch and Decrypt AES-KW + Encrypted Payload\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).hex.signed
	$(eval SOURCE := suit_manifest_aes_kw_slot)
	$(eval TARGET := suit-manifest-aes-kw-slot)
	$(eval CSUITNAME := suit_manifest_expAFS)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: Fetch and Decrypt AES-KW + Encrypted Payload\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).hex.signed
	@echo ES-ECDH content Example
	$(eval SOURCE := suit_manifest_esdh_content)
	$(eval TARGET := suit-manifest-es-ecdh-content)
	$(eval CSUITNAME := suit_manifest_expEW)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 2: Write and Decrypt ES-ECDH + AES-KW + Encrypted Payload\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).hex.signed
	@echo ES-ECDH + Process Dependency Example
	$(eval SOURCE := suit_manifest_esdh_dependency)
	$(eval TARGET := suit-manifest-es-ecdh-dependency)
	$(eval CSUITNAME := suit_manifest_expED)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 3: ES-ECDH + AES-KW + Process Dependency\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit $(SUIT_FIRMWARE_ENCRYPTION_DIR)/examples/$(TARGET).hex.signed

.PHONY: install_update
install_update: suit_manifest_expU0.diag suit_manifest_expU1.diag
	@echo SUIT Update Management Example 0
	$(eval SOURCE := suit_manifest_expU0)
	$(eval TARGET := suit_manifest_expU0)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 0: Copy Params Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor
	@echo SUIT Update Management Example 1
	$(eval SOURCE := suit_manifest_expU1)
	$(eval TARGET := suit_manifest_expU1)
	$(eval MD := $(LIBCSUIT_DIR)/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: Override Multiple Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit $(LIBCSUIT_DIR)/testfiles/$(TARGET).cbor

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS) $(UNTAGGED_DIAGS_IETF116_HACKATHON)
