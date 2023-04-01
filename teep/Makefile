#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TEEP_COSE_DIR := ~/github.com/kentakayama/libteep
TEEP_COSE := $(TEEP_COSE_DIR)/bin/teep_cose_tam

TEEP_UPDATE_MESSAGES := \
	teep_update_uri.teep \
	teep_update_integrated.teep \
	teep_update_personalization.teep \
	teep_update_unlink.teep

ifeq ($(teep-ietf116),1)
TEEP_UPDATE_MESSAGES += \
	teep_update_helloworld.teep
endif

.PHONY: all
all: $(TEEP_UPDATE_MESSAGES)

teep_update_uri.teep: ../untagged_suit/suit_uri.suit
teep_update_integrated.teep: ../untagged_suit/suit_integrated.suit
teep_update_personalization.teep: ../untagged_suit/suit_personalization.suit
teep_update_unlink.teep: ../untagged_suit/suit_unlink.suit
teep_update_helloworld.teep: ../untagged_suit/suit_helloworld.suit

%.teep:
	$(eval FILENAME := $(shell echo $@ | sed -r 's/teep_update_([a-z]+)\.teep/suit_\1.suit/'))
	$(TEEP_COSE) ../untagged_suit/$(FILENAME) $@

.PHONY: clean
clean:
	$(RM) $(TEEP_UPDATE_MESSAGES)
