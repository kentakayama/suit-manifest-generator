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

%.mac.cose: %.cbor
	python3 ../scripts/cwt-mac.py $< $@

%.mac.mdiag: %.mac.cose
	$(CBOR2DIAG) $< > $@

%.bin.hdiag:
	python3 ../scripts/bin-to-diag-hex.py $< > $@

.PHONY: common-clean
common-clean:
	$(RM) *.gdiag *.hdiag *.mdiag *.cbor *.cose
