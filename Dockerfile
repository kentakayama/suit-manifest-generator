# Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.
# SPDX-License-Identifier: BSD-2-Clause
FROM rust:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install git gcc make python3 python3-pip
RUN cargo install cbor-diag-cli

WORKDIR /root/github.com/
RUN git clone --branch v3.3.0 https://github.com/Mbed-TLS/mbedtls.git Mbed-TLS/mbedtls
RUN git clone --depth 1 https://github.com/laurencelundblade/QCBOR.git laurencelundblade/QCBOR
RUN git clone --branch dev-deterministic-ecdsa https://github.com/kentakayama/t_cose.git kentakayama/t_cose
RUN git clone --depth 1 https://github.com/kentakayama/libteep.git kentakayama/libteep
RUN git clone --depth 1 https://github.com/kentakayama/libcsuit.git kentakayama/libcsuit

WORKDIR /root/github.com/
RUN make -j $(nproc) -C Mbed-TLS/mbedtls install
RUN make -j $(nproc) -C laurencelundblade/QCBOR libqcbor.a install
RUN make -j $(nproc) -C kentakayama/t_cose -f Makefile.psa libt_cose.a install
RUN make -j $(nproc) -C kentakayama/libteep -f Makefile.cose MBEDTLS=1
RUN make -j $(nproc) -C kentakayama/libcsuit -f Makefile.sign MBEDTLS=1

WORKDIR /root/github.com/kentakayama

CMD make -C suit-manifest-generator
