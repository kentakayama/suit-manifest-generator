#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

DIAG2CBOR := cbor-diag # https://github.com/Nullus157/cbor-diag-rs

.PHONY: all
all:

.PRECIOUS: ../diag/%.diag
../diag/%.diag:
	$(MAKE) -C ../diag $(notdir $@)

%.cbor: ../diag/%.diag
	$(DIAG2CBOR) --to bytes --from diag < $< > $@

.PHONY: clean
clean:
	ls | grep -v -e "suit_manifest_exp1.cbor" -e "suit_manifest_exp3.cbor" -e Makefile | xargs $(RM)
