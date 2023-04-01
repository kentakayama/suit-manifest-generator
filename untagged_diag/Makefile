#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

UNTAGGED_DIAGS := \
	suit_uri.untagged.diag \
	suit_integrated.untagged.diag \
	suit_personalization.untagged.diag \
	suit_unlink.untagged.diag

ifeq ($(suit-ietf116),1)
UNTAGGED_DIAGS += \
	suit_helloworld.untagged.diag
endif

.PHONY: all
all: $(UNTAGGED_DIAGS)

%.untagged.diag: ../signed_diag/%.diag
	sed -e "s?/ SUIT_Envelope_Tagged / 107(?/ SUIT_Envelope / ?" -e "s/})$$/}/" $< > $@

.PHONY: clean
clean:
	$(RM) $(UNTAGGED_DIAGS)
