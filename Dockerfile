# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
# SPDX-License-Identifier: BSD-2-Clause
FROM rust:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install git gcc make python3 python3-pip
RUN cargo install cbor-diag-cli

WORKDIR /root/github.com/
RUN git clone --recursive https://github.com/kentakayama/suit-manifest-generator.git kentakayama/suit-manifest-generator

RUN make -j $(nproc) -C Mbed-TLS/mbedtls install
RUN make -j $(nproc) -C laurencelundblade/QCBOR libqcbor.a install
RUN make -j $(nproc) -C kentakayama/t_cose -f Makefile.psa libt_cose.a install
RUN make -j $(nproc) -C kentakayama/libteep -f Makefile.cose MBEDTLS=1
RUN make -j $(nproc) -C kentakayama/libcsuit Makefile install

WORKDIR /root/github.com/kentakayama

CMD make -C suit-manifest-generator
