#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: teep_cose_tam teep_cose_trustanchor

CFLAGS = $(CMD_CFLAGS) -I./inc
LDFLAGS = $(CMD_LDFLAGS) -lteep -lt_cose -lmbedcrypto -lqcbor -lm

teep_cose_tam:
	$(CC) $(CFLAGS) -o teep_examples_common.o -c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_cose_tam.o -c teep_cose_main.c -DTEEP_ACTOR_TAM=1
	$(CC) -o $@ teep_cose_tam.o teep_examples_common.o $(LDFLAGS)

teep_cose_trustanchor:
	$(CC) $(CFLAGS) -o teep_examples_common.o -c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_cose_trustanchor.o -c teep_cose_main.c -DTEEP_ACTOR_TRUST_ANCHOR=1
	$(CC) -o $@ teep_cose_trustanchor.o teep_examples_common.o $(LDFLAGS)

.PHONY: clean
clean:
	$(RM) teep_cose_tam teep_cose_trustanchor *.o

