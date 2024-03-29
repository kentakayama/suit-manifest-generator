# SUIT Manifest and TEEP Message Generator
This tool creates SUIT Manifests and TEEP Messages respectively.  
They can be used as test vector to your implementation.  

## Install into a Docker Container
```
$ cd /path/to/your/temporary/dir/
$ git clone --recursive https://github.com/kentakayama/suit-manifest-generator.git
$ cd suit-manifest-generator/
$ sudo docker build -t suit-gen .
```

## Run in the Docker Container
```
$ sudo docker run -v $PWD:/root/github.com/kentakayama/suit-manifest-generator -t suit-gen
$ ls -la teep/ suit/ # signed cbor binaries
```

## How it works
``` mermaid
graph TD

TM[TEEP Message Update with Security Wrapper]
TM0[TEEP Message Update w/o Security Wrapper]
SUM[SUIT Untagged Manifest with Security Wrapper]

SM[SUIT Manifest with Authentication Wrapper]
SM0[SUIT Manifest w/o Authentication Wrapper]
DSM[CBOR Diagnostic SUIT Manifest w/o Authentication Wrapper]
DTM[CBOR Diagnostic TEEP Message w/o Security Wrapper]
EDSM[Extended CBOR Diagnostic SUIT Manifest]
EDTM[Extended CBOR Diagnostic TEEP Message]

subgraph "`$ make -C suit`"
  EDSM -- ediag-to-diag.py --> DSM
  DSM -- cbor-diag-cli --> SM0
  SM0 -- "sign with Trust Anchor key (libcsuit)" --> SM
  SM --> SUM
end

subgraph "`$ make -C teep`"
  EDTM -- ediag-to-diag.py --> DTM
  SUM -- ediag-to-diag.py --> DTM

  DTM -- cbor-diag-cli --> TM0
  TM0 -- "sign with TAM key (libteep)" --> TM
end
```

## Directly Depending Libraries&Tools
- [QCBOR](https://github.com/laurencelundblade/QCBOR)
- [t_cose](https://github.com/laurencelundblase/t_cose)
- [libteep](https://github.com/kentakayama/libteep)
- [libcsuit](https://github.com/kentakayama/libcsuit)
- [cbor-diag-cli](https://crates.io/crates/cbor-diag-cli)

## License and Copyright
BSD 2-Clause License

Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
