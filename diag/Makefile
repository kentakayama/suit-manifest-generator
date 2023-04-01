#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

FIXED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
	suit_unlink.diag \
	suit_personalization.diag \
	suit_manifest_raw.diag \
	suit_manifest_dependency.diag \
	suit_manifest_aes_kw.diag \
	suit_manifest_aes_kw_dependent.diag

ifeq ($(suit-ietf116),1)
GENERATED_DIAGS += \
	suit_helloworld.diag
endif

ifeq ($(teep),1)
GENERATED_DIAGS += \
	teep_update_example1.diag \
	teep_update_example3.diag \
	teep_update_uri.diag \
	teep_update_integrated.diag \
	teep_update_personalization.diag \
	teep_update_unlink.diag
endif

ifeq ($(teep-ietf116),1)
GENERATED_FILES += \
	teep_update_helloworld.diag
endif

.PHONY: all
all: $(GENERATED_DIAGS)

teep_update_uri.diag: ../untagged_suit/suit_uri.suit
teep_update_integrated.diag: ../untagged_suit/suit_integrated.suit
teep_update_personalization.diag: ../untagged_suit/suit_personalization.suit
teep_update_unlink.diag: ../untagged_suit/suit_unlink.suit
teep_update_helloworld.diag: ../untagged_suit/suit_helloworld.suit

%.diag: ../ediag/%.ediag
	$(PYTHON3) ./ediag-to-diag.py $< > $@

.PHONY: clean
clean:
	$(RM) $(GENERATED_DIAGS)
