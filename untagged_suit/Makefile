DIAG2CBOR := cbor-diag # https://github.com/Nullus157/cbor-diag-rs

UNTAGGED_SUIT_MANIFESTS := \
	suit_uri.suit \
	suit_integrated.suit \
	suit_personalization.suit \
	suit_unlink.suit \
	suit_helloworld.suit

.PHONY: all
all: $(UNTAGGED_SUIT_MANIFESTS)

%.suit: ../untagged_diag/%.untagged.diag
	$(DIAG2CBOR) --to bytes --from diag < $< > $@

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_SUIT_MANIFESTS)
