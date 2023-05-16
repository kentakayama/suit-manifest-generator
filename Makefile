#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all:
	$(MAKE) -C bin
	$(MAKE) -C teep
	$(MAKE) -C suit
	$(MAKE) -C signed_diag
	$(MAKE) -C untagged_diag

.PHONY: install
install: all
	$(MAKE) -C signed_diag install
	$(MAKE) -C untagged_diag install

.PHONY: clean
clean:
	$(MAKE) clean -C diag
	$(MAKE) clean -C cbor
	$(MAKE) clean -C untagged_suit
	$(MAKE) clean -C untagged_diag
	$(MAKE) clean -C signed_diag
	$(MAKE) clean -C suit
	$(MAKE) clean -C teep
	$(MAKE) clean -C bin

.PHONY: test
test:
	$(MAKE) -C suit test
