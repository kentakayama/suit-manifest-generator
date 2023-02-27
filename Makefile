DIAG2CBOR := cbor-diag # https://github.com/Nullus157/cbor-diag-rs
TEEP_PROTOCOL_CBOR_DIR := ~/github.com/ietf-teep/teep-protocol/cbor
SUIT_TOOL_DIR := ~/gitlab.arm.com/research/ietf-suit/suit-tool
SUIT_TOOL := $(SUIT_TOOL_DIR)/bin/suit-tool
PRIVATE_KEY := $(SUIT_TOOL_DIR)/private_key.pem

# outputs
MANIFESTS += \
	suit-manifest-dependency.suit.signed \
	suit-manifest-aes-kw.suit.signed \
	suit-manifest-raw.suit.signed \
	suit-manifest-aes-kw-dependent.suit.signed

MANIFESTS_FOR_TEEP := \
	suit_uri.diag.signed.untagged \
	suit_integrated.diag.signed.untagged \
	suit_personalization.diag.signed.untagged \
	suit_unlink.diag.signed.untagged

MANIFESTS_FOR_IETF116 := \
	suit-enclave-hello.diag.signed.untagged

MANIFESTS_FOR_TEEP += $(MANIFESTS_FOR_IETF116)

MANIFEST_CBORS_FOR_TEEP := $(MANIFESTS_FOR_TEEP:.diag.signed.untagged=.suit.signed.untagged)
MANIFESTS += $(MANIFESTS_FOR_TEEP)

.PHONY: all install-teep clean

all: $(MANIFESTS) $(MANIFEST_CBORS_FOR_TEEP)

%.diag: %.ediag
	python3 pre.py $< > $@

%.suit: %.diag
	$(DIAG2CBOR) --to bytes < $< > $@

%.suit.signed: %.suit
	$(SUIT_TOOL) sign -m $< -k $(PRIVATE_KEY) -o $@

%.diag.signed: %.suit.signed
	sed -e "s?/ authentication-wrapper /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / cose-alg-sha256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 13 -l 32 $<)'\n    ] >>,\n    << / COSE_Sign1_Tagged / 18\([\n      / protected: / << {\n        / algorithm-id / 1: -7 / ES256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / signature: / h'$(shell xxd -p -u -c 64 -s 57 -l 64 $<)'\n    ]\) >>\n  ] >>,?" $(<:.suit.signed=.diag) > $@

%.diag.signed.untagged: %.diag.signed
	sed -e "s?/ SUIT_Envelope_Tagged / 107(?/ SUIT_Envelope / ?" -e "s/})$$/}/" $< > $@

%.suit.signed.untagged: %.diag.signed.untagged
	$(DIAG2CBOR) --to bytes < $< > $@

install-teep: $(MANIFESTS_FOR_TEEP)
	$(foreach mfst,$^,cp $(mfst) $(TEEP_PROTOCOL_CBOR_DIR)/$(mfst:.diag.signed.untagged=.diag.txt);)
	$(foreach mfst,$^,xxd -p -u $(mfst:.diag.signed.untagged=.suit.signed.untagged) $(TEEP_PROTOCOL_CBOR_DIR)/$(mfst:.diag.signed.untagged=.hex.txt);)

.PHONY: clean
clean:
	$(RM) $(MANIFESTS)
