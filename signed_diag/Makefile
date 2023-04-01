UNTAGGED_DIAGS := \
	suit_uri.diag \
	suit_integrated.diag \
	suit_personalization.diag \
	suit_unlink.diag \
	suit_helloworld.diag

.PHONY: all
all: $(UNTAGGED_DIAGS)

%.diag: ../suit/%.suit
	sed -e "s?/ authentication-wrapper /?/ authentication-wrapper / 2: << [\n    << [\n      / digest-algorithm-id: / -16 / cose-alg-sha256 /,\n      / digest-bytes: / h'$(shell xxd -p -u -c 32 -s 13 -l 32 $<)'\n    ] >>,\n    << / COSE_Sign1_Tagged / 18\([\n      / protected: / << {\n        / algorithm-id / 1: -7 / ES256 /\n      } >>,\n      / unprotected: / {},\n      / payload: / null,\n      / signature: / h'$(shell xxd -p -u -c 64 -s 57 -l 64 $<)'\n    ]\) >>\n  ] >>,?" ../diag/$@ > $@

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS)
