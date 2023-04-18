#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

UNTAGGED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
	suit_personalization.diag \
	suit_unlink.diag \
	suit_manifest_raw.diag \
	suit_manifest_dependency.diag \
	suit_manifest_aes_kw.diag \
	suit_manifest_aes_kw_content.diag \
	suit_manifest_aes_kw_dependent.diag \
	suit_manifest_expS0.diag \
	suit_manifest_expS1.diag \
	suit_manifest_expS2.diag \
	suit_manifest_expS3.diag \
	suit_manifest_expS4.diag

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

suit_manifest_expS1.diag: ../suit/suit_manifest_expS1.suit
	sed -e "s?/ authentication-wrapper /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / SHA256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 174 -l 32 $<)'\n    ] >>,\n    << / COSE_Sign1_Tagged / 18\([\n      / protected: / << {\n        / algorithm-id / 1: -7 / ES256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / signature: / h'$(shell xxd -p -u -c 64 -s 218 -l 64 $<)'\n    ]\) >>\n  ] >>,?" ../diag/$@ > $@

%.diag: ../suit/%.suit
	sed -e "s?/ authentication-wrapper /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / SHA256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 13 -l 32 $<)'\n    ] >>,\n    << / COSE_Sign1_Tagged / 18\([\n      / protected: / << {\n        / algorithm-id / 1: -7 / ES256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / signature: / h'$(shell xxd -p -u -c 64 -s 57 -l 64 $<)'\n    ]\) >>\n  ] >>,?" ../diag/$@ > $@

.PHONY: install
install:
	@echo Simple Example
	$(eval SOURCE := suit_manifest_expS0)
	$(eval TARGET := suit_manifest_expS0)
	$(eval MD := ../../libcsuit/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 0: Basic Content+Write Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(TARGET).cbor
	@echo SUIT Delegation
	$(eval SOURCE := suit_manifest_expS1)
	$(eval TARGET := suit_manifest_expS1)
	$(eval MD := ../../libcsuit/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: SUIT Delegation Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(TARGET).cbor
	@echo Simple Dependency Example
	$(eval SOURCE := suit_manifest_expS2)
	$(eval TARGET := suit_manifest_expS2)
	$(eval MD := ../../libcsuit/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 2: Basic Dependency Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(TARGET).cbor
	@echo Integrated Dependency Example
	$(eval SOURCE := suit_manifest_expS3)
	$(eval TARGET := suit_manifest_expS3)
	$(eval MD := ../../libcsuit/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 3: Integrated Dependency Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(TARGET).cbor
	@echo Integrated Dependency Example
	$(eval SOURCE := suit_manifest_expS4)
	$(eval TARGET := suit_manifest_expS4)
	$(eval MD := ../../libcsuit/testfiles/$(TARGET).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 4: Is Dependency Example\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(TARGET).cbor
	@echo AES-KW content Example
	$(eval SOURCE := suit_manifest_aes_kw_content)
	$(eval TARGET := suit-manifest-aes-kw-content)
	$(eval CSUITNAME := suit_manifest_expEW)
	$(eval MD := ../../libcsuit/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 0: Write and Decrypt Encrypted Payload\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag ../../../suit-wg/suit-firmware-encryption/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit ../../../suit-wg/suit-firmware-encryption/examples/$(TARGET).hex.signed
	@echo AES-KW fetch Example
	$(eval SOURCE := suit_manifest_aes_kw)
	$(eval TARGET := suit-manifest-aes-kw)
	$(eval CSUITNAME := suit_manifest_expEF)
	$(eval MD := ../../libcsuit/testfiles/$(CSUITNAME).md)
	echo "<!--\n Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.\n\n SPDX-License-Identifier: BSD-2-Clause\n-->\n\n## Example 1: Fetch and Decrypt Encrypted Payload\n{: numbered='no'}\n\n### CBOR Diagnostic Notation of SUIT Manifest\n{: numbered='no'}\n\n~~~~" > $(MD)
	cat $(SOURCE).diag >> $(MD)
	echo "~~~~\n\n\n### CBOR Binary in Hex\n{: numbered='no'}\n\n~~~~" >> $(MD)
	xxd -u -p ../suit/$(SOURCE).suit >> $(MD)
	echo "~~~~" >> $(MD)
	cp $(SOURCE).diag ../../../suit-wg/suit-firmware-encryption/examples/$(TARGET).diag.signed
	cp ../suit/$(SOURCE).suit ../../libcsuit/testfiles/$(CSUITNAME).cbor
	xxd -p -u ../suit/$(SOURCE).suit ../../../suit-wg/suit-firmware-encryption/examples/$(TARGET).hex.signed

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS) $(UNTAGGED_DIAGS_IETF116_HACKATHON)
