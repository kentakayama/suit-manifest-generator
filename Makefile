#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: bin suit teep

.PHONY: bin
bin:
	$(MAKE) -C bin

.PHONY: teep
teep:
	$(MAKE) -C teep
	#$(MAKE) -C untagged_suit
	#$(MAKE) -C untagged_diag

.PHONY: suit
suit:
	$(MAKE) -C signed_diag
	#$(MAKE) -C suit

.PHONY: install
install: suit teep
	$(MAKE) -C signed_diag install
	$(MAKE) -C untagged_diag install

.PHONY: bin_clean
bin_clean:
	$(MAKE) clean -C bin

.PHONY: clean
clean:
	$(MAKE) clean -C diag
	$(MAKE) clean -C cbor
	$(MAKE) clean -C untagged_suit
	$(MAKE) clean -C untagged_diag
	$(MAKE) clean -C signed_diag
	$(MAKE) clean -C suit
	$(MAKE) clean -C teep

.PHONY: test
test:
	$(MAKE) -C suit test
