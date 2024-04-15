#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

TAM_COSE := ../bin/teep/teep_cose_tam1
TRUST_ANCHOR_COSE := ../bin/teep/teep_cose_trustanchor
TEEP_AGENT_COSE := ../bin/teep/teep_cose_agent
VERIFIER_COSE := ../bin/teep/teep_cose_verifier

TEEP_UPDATE_MESSAGES := \
	teep_update_uri.teep \
	teep_update_integrated.teep \
	teep_update_personalization.teep

TEEP_ERROR_MESSAGES := \
	teep_error_agent_attestation.teep

QUERY_RESPONSE_MESSAGES := \
	query_response.teep

TEEP_IETF116_HACKATHON := \
	teep_update_helloworld.teep

SUIT_DELEGATIONS := \
	suit_delegation.cwt

ifeq ($(teep-ietf116),1)
TEEP_UPDATE_MESSAGES += $(TEEP_IETF116_HACKATHON)
endif

.PHONY: all
all: $(TEEP_UPDATE_MESSAGES) $(TEEP_ERROR_MESSAGES) $(QUERY_RESPONSE_MESSAGES)

teep_update_uri.teep: ../untagged_suit/suit_uri.suit
teep_update_integrated.teep: ../untagged_suit/suit_integrated.suit
teep_update_personalization.teep: ../untagged_suit/suit_manifest_esdh_config.suit
teep_update_helloworld.teep: ../untagged_suit/suit_helloworld.suit
	$(TAM_COSE) ../untagged_suit/$< $@

suit_delegation.cwt: ../cbor/suit_delegation.cbor

attestation_results.cwt: ../cbor/attestation_results.cbor
	$(VERIFIER_COSE) $< $@

query_response.teep: attestation_results.cwt

query_response.teep: ../cbor/query_response.cbor
	$(TEEP_AGENT_COSE) $< $@

.PRECIOUS: ../untagged_suit/%.suit
../untagged_suit/%.suit:
	$(MAKE) -C ../untagged_suit $(notdir $@)

.PRECIOUS: ../cbor/%.cbor
../cbor/%.cbor:
	$(MAKE) -C ../cbor $(notdir $@)

teep_error_agent_attestation.teep: ../cbor/teep_error_agent_attestation.cbor
	$(TEEP_AGENT_COSE) $< $@

%.teep:
	$(TAM_COSE) ../untagged_suit/$< $@

%.cwt:
	$(TRUST_ANCHOR_COSE) ../cbor/$(@:.cwt=.cbor) $@

.PHONY: clean
clean:
	$(RM) $(TEEP_UPDATE_MESSAGES) $(TEEP_ERROR_MESSAGES) $(TEEP_IETF116_HACKATHON) $(SUIT_DELEGATIONS)
