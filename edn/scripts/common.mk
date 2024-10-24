#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

# define generic rules
export SUIT_MANIFEST_CDDL=../../cddl/suit-manifest.cddl

RUBYDEBUG=RUBYOPT="-W0"
DIAG2CBOR=$(RUBYDEBUG) diag2cbor.rb
DIAG2DIAG=$(RUBYDEBUG) CBOR_DIAG_CDDL=$(SUIT_MANIFEST_CDDL) diag2diag.rb -e -d -aref -ae # embedded + deterministic + edn-ref + edn-e
CBOR2DIAG=$(RUBYDEBUG) cbor2diag.rb -e # embedded
TEST_COMMAND=$(RUBYDEBUG) cddl $(SUIT_MANIFEST_CDDL) validate
PAYLOAD_ENCRYPTION=../scripts/suit_payload_encryption.py
AESCTR_SEC_KEY=../scripts/aesctr-sec.jwk
AESKW_SEC_KEY=../scripts/aeskw-sec.jwk
ESDH_SENDER_PRIV_KEY=../scripts/esdh-sender-priv.jwk
ESDH_RECEIVER_PUB_KEY=../scripts/esdh-recipient-pub.jwk

# generate full suit-manifest cddl
.PHONY: cddl
cddl: $(SUIT_MANIFEST_CDDL)
$(SUIT_MANIFEST_CDDL):
	$(MAKE) -C ../../cddl


# generate cbor file from generated diag file
%.cbor: %.gdiag
	$(DIAG2CBOR) $< > $@

# generate diag file from EDN+ref+e file
%.gdiag: %.rediag
	$(DIAG2DIAG) $< > $@

# store file size as an integer
%.size.gdiag:
	stat --format=%s $< > $@

# store sha256 hash as a byte string
%.digest.hdiag:
	sha256sum $< | awk '{printf "h'\''%s'\''",$$1}' > $@

# generate COSE_Mac0 binary
%.mac.cose: %.cbor
	python3 ../scripts/cwt-mac.py $< $@

# generate COSE_Mac0 diag
%.cose.gdiag: %.cose
	$(CBOR2DIAG) $< > $@

# generate byte string diag from a binary
%.bin.hdiag:
	python3 ../scripts/bin2hdiag.py $< > $@

# generate A128KW+A128CTR encrypted payload
%.a128kw.a128ctr.encrypt.cose:
	python3 $(PAYLOAD_ENCRYPTION) -e ${@:.cose=.bin} -k ${AESKW_SEC_KEY} $< ${AESCTR_SEC_KEY} $@

%.ecdh.a128kw.a128ctr.encrypt.cose:
	python3 $(PAYLOAD_ENCRYPTION) -e ${@:.cose=.bin} -s $(ESDH_SENDER_PRIV_KEY) -r $(ESDH_RECEIVER_PUB_KEY) $< $(AESCTR_SEC_KEY) $@

.PHONY: common-clean
common-clean:
	$(RM) *.gdiag *.hdiag *.cbor *.cose
