#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

.PHONY: all
all: teep_cose_tam0 teep_cose_tam1 teep_cose_trustanchor teep_cose_agent

CFLAGS = $(CMD_CFLAGS) #-DLIBTEEP_PSA_CRYPTO_C=1
LDFLAGS = $(CMD_LDFLAGS) -lteep -lt_cose -lcrypto -lqcbor -lm

teep_cose_tam0: teep_cose_main.c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_examples_common.o -c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_cose_tam0.o -c teep_cose_main.c -DTEEP_ACTOR_TAM0=1
	$(CC) -o $@ teep_cose_tam0.o teep_examples_common.o $(LDFLAGS)

teep_cose_tam1: teep_cose_main.c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_examples_common.o -c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_cose_tam1.o -c teep_cose_main.c -DTEEP_ACTOR_TAM1=1
	$(CC) -o $@ teep_cose_tam1.o teep_examples_common.o $(LDFLAGS)

teep_cose_trustanchor: teep_cose_main.c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_examples_common.o -c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_cose_trustanchor.o -c teep_cose_main.c -DTEEP_ACTOR_TRUST_ANCHOR=1
	$(CC) -o $@ teep_cose_trustanchor.o teep_examples_common.o $(LDFLAGS)

teep_cose_agent: teep_cose_main.c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_examples_common.o -c teep_examples_common.c
	$(CC) $(CFLAGS) -o teep_cose_agent.o -c teep_cose_main.c -DTEEP_ACTOR_AGENT=1
	$(CC) -o $@ teep_cose_agent.o teep_examples_common.o $(LDFLAGS)

.PHONY: clean
clean:
	$(RM) teep_cose_tam0 teep_cose_tam1 teep_cose_trustanchor teep_cose_agent *.o

