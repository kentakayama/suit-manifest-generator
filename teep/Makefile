#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TEEP_COSE_DIR := ~/github.com/kentakayama/libteep
TEEP_COSE := $(TEEP_COSE_DIR)/bin/teep_cose_tam
TRUST_ANCHOR_COSE := $(TEEP_COSE_DIR)/bin/teep_cose_trust_anchor

TEEP_UPDATE_MESSAGES := \
	teep_update_uri.teep \
	teep_update_integrated.teep \
	teep_update_personalization.teep \
	teep_update_unlink.teep

TEEP_IETF116_HACKATHON := \
	teep_update_helloworld.teep

SUIT_DELEGATIONS := \
	suit_delegation.cwt

ifeq ($(teep-ietf116),1)
TEEP_UPDATE_MESSAGES += $(TEEP_IETF116_HACKATHON)
endif

.PHONY: all
all: $(TEEP_UPDATE_MESSAGES)

teep_update_uri.teep: ../untagged_suit/suit_uri.suit
teep_update_integrated.teep: ../untagged_suit/suit_integrated.suit
teep_update_personalization.teep: ../untagged_suit/suit_manifest_aes_kw_config.suit
teep_update_unlink.teep: ../untagged_suit/suit_unlink.suit
teep_update_helloworld.teep: ../untagged_suit/suit_helloworld.suit
suit_delegation.cwt: ../cbor/suit_delegation.cbor

.PRECIOUS: ../untagged_suit/%.suit
../untagged_suit/%.suit:
	$(MAKE) -C ../untagged_suit $(notdir $@)

.PRECIOUS: ../cbor/%.cbor
	$(MAKE) -C ../cbor $(notdir $@)

%.teep:
	$(eval FILENAME := $(shell echo $@ | sed -r 's/teep_update_([a-z]+)\.teep/suit_\1.suit/'))
	$(TEEP_COSE) ../untagged_suit/$(FILENAME) $@

%.cwt:
	$(TRUST_ANCHOR_COSE) ../cbor/$(@:.cwt=.cbor) $@

.PHONY: clean
clean:
	$(RM) $(TEEP_UPDATE_MESSAGES) $(TEEP_IETF116_HACKATHON) $(SUIT_DELEGATIONS)
