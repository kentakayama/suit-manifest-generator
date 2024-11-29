CONCATENATED_SUIT_CDDL       := suit-manifest.cddl
SUIT_MANIFEST_CDDL           := draft-ietf-suit-manifest.cddl
SUIT_TRUST_DOMAINS_CDDL      := draft-ietf-suit-trust-domains.cddl
SUIT_UPDATE_MANAGEMENT_CDDL  := draft-ietf-suit-update-management.cddl
SUIT_ENCRYPTED_PAYLOADS_CDDL := draft-ietf-suit-firmware-encryption.cddl
SUIT_REPORT_CDDL             := draft-ietf-suit-report.cddl
SUIT_MTI_CDDL                := draft-ietf-suit-mti.cddl
COSWID_CDDL                  := rfc-9393-coswid.cddl
COSE_XML                     := rfc-9052-cose.xml
COSE_CDDL                    := rfc-9052-cose.cddl

CDDLS := \
	$(SUIT_MANIFEST_CDDL) \
	$(SUIT_TRUST_DOMAINS_CDDL) \
	$(SUIT_UPDATE_MANAGEMENT_CDDL) \
	$(SUIT_ENCRYPTED_PAYLOADS_CDDL) \
	$(SUIT_REPORT_CDDL) \
	$(SUIT_MTI_CDDL) \
	$(COSWID_CDDL) \
	$(COSE_CDDL)

.PHONY: cat-cddl
cat-cddl: $(CONCATENATED_SUIT_CDDL)

$(CONCATENATED_SUIT_CDDL): $(CDDLS)
	cat $^ > $@

$(SUIT_MANIFEST_CDDL):
	curl https://raw.githubusercontent.com/suit-wg/manifest-spec/master/draft-ietf-suit-manifest.cddl | \
	sed -i -e 's/suit-install = 17/suit-install = 20/' $@

$(SUIT_TRUST_DOMAINS_CDDL):
	curl https://raw.githubusercontent.com/suit-wg/suit-multiple-trust-domains/main/draft-ietf-suit-trust-domains.cddl -o $@

$(SUIT_UPDATE_MANAGEMENT_CDDL):
	curl https://raw.githubusercontent.com/suit-wg/suit-update-management/main/draft-ietf-suit-update-management.cddl -o $@

$(SUIT_ENCRYPTED_PAYLOADS_CDDL):
	curl https://raw.githubusercontent.com/suit-wg/suit-firmware-encryption/main/draft-ietf-suit-firmware-encryption.cddl -o $@


$(SUIT_REPORT_CDDL):
	curl https://raw.githubusercontent.com/suit-wg/suit-report/main/draft-ietf-suit-report.cddl -o $@

$(SUIT_MTI_CDDL):
	curl https://raw.githubusercontent.com/bremoran/suit-mti/main/draft-ietf-suit-mti.cddl -o $@

$(COSWID_CDDL):
	curl https://raw.githubusercontent.com/sacmwg/draft-ietf-sacm-coswid/refs/heads/master/concise-swid-tag.cddl | sed -e 's/label /coswid-label /g' > $@

$(COSE_XML):
	curl https://www.rfc-editor.org/rfc/rfc9052.xml -o $@

$(COSE_CDDL): $(COSE_XML)
	sed -n -e '/<sourcecode type="cddl"/,/<\/sourcecode>/ p' $< | sed -e '/<sourcecode type="cddl"/ d' -e '/<\/sourcecode>/ d' -e 's/\&lt;/</g' -e 's/\&gt;/>/g' > $@

define FuncValidateCddl
	cddl $1 validate $2

endef


.PHONY: validate-cddl
validate-cddl: validate-suit-cddl $(CONCATENATED_CDDL) $(TEEP_MESSAGES)
	@echo "Checking each TEEP Protocol binary file matches TEEP Protcol CDDL"
	$(foreach msg,$(TEEP_MESSAGES),$(call FuncValidateCddl,$(CONCATENATED_CDDL),$(msg)))
	@echo "Success: Each TEEP Protocol message matches the CDDL"

.PHONY: validate-suit-cddl
validate-suit-cddl: $(CONCATENATED_UNTAGGED_SUIT_CDDL) $(SUIT_MANIFESTS)
	@echo "Checking each SUIT Manifest binary file matches SUIT Manifest CDDL"
	$(foreach mfst,$(SUIT_MANIFESTS),$(call FuncValidateCddl,$(CONCATENATED_UNTAGGED_SUIT_CDDL),$(mfst)))
	@echo "Success: Each SUIT Manifest matches the CDDL"

.PHONY: validate-teep-cddl
validate-teep-cddl: $(CONCATENATED_CDDL) ../cbor/query_request.diag.bin
	cddl $(CONCATENATED_CDDL) validate ../cbor/query_request.diag.bin
	@echo "Success: QueryRequest message matches TEEP Protocol CDDL"

.PHONY: gen-cddl
gen-cddl: cat-cddl $(CONCATENATED_CDDL)
	cddl $(CONCATENATED_CDDL) generate

.PHONY: clean
clean:
	$(RM) $(CONCATENATED_SUIT_CDDL) $(COSE_CDDL) $(COSE_XML) $(SUIT_MANIFEST_CDDL) $(SUIT_TRUST_DOMAINS_CDDL) $(SUIT_ENCRYPTED_PAYLOADS_CDDL) $(SUIT_REPORT_CDDL)
