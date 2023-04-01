# SUIT Manifest and TEEP Message Generator
suit-manifest-generator creates SUIT Manifests and TEEP Messages respectively.  
They can be used as test vector to your implementation.  

## Install with docker
```
$ cd /path/to/your/temporary/dir/
$ git clone https://github.com/kentakayama/suit-manifest-generator.git
$ cd suit-manifest-generator/
$ sudo docker build -t suit-gen .
```

## Run in docker
```
$ sudo docker run -v $PWD:/root/suit-manifest-generator -t suit-gen
$ ls -la teep/ suit/ # signed cbor binaries
```

## How it works
``` mermaid
graph TD

TM[TEEP Message Update]
SUM[SUIT Untagged Manifest]

SM[SUIT Manifest w/ Authentication]
S0[SUIT Manifest w/o Authentication]
DSM[CBOR Diagnostic SUIT Manifest]
DTM[CBOR Diagnostic TEEP Message]
EDSM[Extended CBOR Diagnostic SUIT Manifest]
EDTM[Extended CBOR Diagnostic TEEP Message]

subgraph suit-manifest-generator
    subgraph Generating SUIT Manifest
        subgraph Extended CBOR Diagnostic Processor
            EDSM --> DSM
        end

        subgraph cbor-diag-cli
            DSM --> S0
        end

        subgraph suit-tool
            S0 --> SM
        end
    end

    subgraph Generating TEEP Message
        subgraph Extended CBOR Diagnostic Processor
            EDTM --> DSM
        end

        subgraph cbor-diag-cli
            SM --> SUM
        end

        subgraph libteep TAM sign
            SUM --> TM
        end
    end
end
```

## License and Copyright
BSD 2-Clause License

Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.

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
