# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
# SPDX-License-Identifier: BSD-2-Clause
FROM rust:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get -y install git gcc make python3 python3-pip xxd
RUN cargo install cbor-diag-cli

COPY . /root/github.com/kentakayama/suit-manifest-generator/

WORKDIR /root/github.com/kentakayama/suit-manifest-generator
RUN make -j $(nproc) -C mbedtls install
RUN make -j $(nproc) -C QCBOR libqcbor.a install
RUN make -j $(nproc) -C t_cose -f Makefile.psa libt_cose.a install
RUN make -j $(nproc) -C libteep MBEDTLS=1 install
RUN make -j $(nproc) -C libcsuit Makefile MBEDTLS=1 install

CMD make
