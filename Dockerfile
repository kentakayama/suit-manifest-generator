# Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.
# SPDX-License-Identifier: BSD-2-Clause
FROM rust:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install git gcc make python3 python3-pip libssl-dev

WORKDIR /root/github.com/laurencelundblade
RUN git clone --depth 1 https://github.com/laurencelundblade/QCBOR.git
RUN make -C QCBOR libqcbor.a install

RUN git clone --depth 1 https://github.com/laurencelundblade/t_cose.git
RUN make -C t_cose -f Makefile.ossl libt_cose.a install

RUN cargo install cbor-diag-cli

WORKDIR /root/github.com/kentakayama
RUN git clone --depth 1 https://github.com/kentakayama/libteep.git
RUN make -C libteep -f Makefile.cose

WORKDIR /root/gitlab.arm.com/research/ietf-suit/
RUN git clone --depth 1 https://gitlab.arm.com/research/ietf-suit/suit-tool.git
WORKDIR ./suit-tool
RUN python3 -m pip install --user --upgrade .
COPY ./misc/sign.diff .
RUN git apply < sign.diff

WORKDIR /root

CMD make -C suit-manifest-generator
