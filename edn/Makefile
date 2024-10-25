#
# Copyright (c) 2024 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all:
	$(MAKE) -C hello
	$(MAKE) -C aeskw
	$(MAKE) -C esdh

.PHONY: test
test:
	$(MAKE) -C hello test
	$(MAKE) -C aeskw test
	$(MAKE) -C esdh test

.PHONY: clean
clean:
	$(MAKE) -C hello clean
	$(MAKE) -C aeskw clean
	$(MAKE) -C esdh clean
