#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

DIAG2CBOR := cbor-diag --to bytes --from diag # https://github.com/Nullus157/cbor-diag-rs
DIAG2CBOR := diag2cbor.rb

.PHONY: all
all:

.PRECIOUS: ../diag/%.diag
../diag/%.diag:
	$(MAKE) -C ../diag $(notdir $@)

%.cbor: ../diag/%.diag
	$(DIAG2CBOR) < $< > $@

.PHONY: clean
clean:
	$(RM) *.cbor
