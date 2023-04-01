#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all:
	$(MAKE) -C diag suit=1
	$(MAKE) -C cbor suit=1
	$(MAKE) -C suit
	$(MAKE) -C signed_diag
	$(MAKE) -C untagged_diag
	$(MAKE) -C untagged_suit
	$(MAKE) -C diag teep=1
	$(MAKE) -C cbor teep=1
	$(MAKE) -C teep

.PHONY:
clean:
	$(MAKE) clean -C diag clean suit=1 teep=1 teep-ietf116=1 suit-ietf116=1
	$(MAKE) clean -C cbor clean suit=1 teep=1 teep-ietf116=1 suit-ietf116=1
	$(MAKE) clean -C suit
	$(MAKE) clean -C signed_diag
	$(MAKE) clean -C untagged_diag
	$(MAKE) clean -C untagged_suit
	$(MAKE) clean -C teep
