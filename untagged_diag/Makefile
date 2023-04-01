UNTAGGED_DIAGS := \
	suit_uri.untagged.diag \
	suit_integrated.untagged.diag \
	suit_personalization.untagged.diag \
	suit_unlink.untagged.diag \
	suit_helloworld.untagged.diag

.PHONY: all
all: $(UNTAGGED_DIAGS)

%.untagged.diag: ../signed_diag/%.diag
	sed -e "s?/ SUIT_Envelope_Tagged / 107(?/ SUIT_Envelope / ?" -e "s/})$$/}/" $< > $@

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS)
