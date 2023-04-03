#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all:
	$(MAKE) -C teep
	$(MAKE) -C suit

.PHONY:
clean:
	$(MAKE) clean -C diag clean suit=1 teep=1 teep-ietf116=1 suit-ietf116=1
	$(MAKE) clean -C cbor clean suit=1 teep=1 teep-ietf116=1 suit-ietf116=1
	$(MAKE) clean -C suit
	$(MAKE) clean -C signed_diag
	$(MAKE) clean -C untagged_diag
	$(MAKE) clean -C untagged_suit
	$(MAKE) clean -C teep
