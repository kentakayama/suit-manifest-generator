# suit-manifest-generator with Extended Diagnostic Notation (EDN)

The suit-manifest-generator supports manifest Authors to create SUIT Manifest for firmware image(s),
based on the internet drafts below.
* [A Concise Binary Object Representation (CBOR)-based Serialization Format for the Software Updates for Internet of Things (SUIT) Manifest](https://datatracker.ietf.org/doc/html/draft-ietf-suit-manifest)
* [Update Management Extensions for Software Updates for Internet of Things (SUIT) Manifests](https://datatracker.ietf.org/doc/html/draft-ietf-suit-update-management)
* [SUIT Manifest Extensions for Multiple Trust Domains](https://datatracker.ietf.org/doc/html/draft-ietf-suit-trust-domains)
* [Encrypted Payloads in SUIT Manifests](https://datatracker.ietf.org/doc/html/draft-ietf-suit-firmware-encryption)

The sample materials use CBOR diagnostic notation with `e''` and `ref''` representations defined in [External References to Values in CBOR Diagnostic Notation (EDN)](https://datatracker.ietf.org/doc/html/draft-ietf-cbor-edn-e-ref) for better readability and modifiability.
Note that this tool generates CBOR binaries with canonical encoding which is required in the [Section 8.1 of draft-ietf-suit-manifest](https://datatracker.ietf.org/doc/html/draft-ietf-suit-manifest#section-8.1).

## Samples
| Sample | Used features |
|--|--|
| [Hello World](./hello) | uri-fetch, integrated payload |
| [Encrypted Payload with AES-KW + AES-CTR](./aeskw) | uri-fetch, integrated payload, encryption info (symmetric AES-KW) |
| [Encrypted Payload with ECDH-ES+AES-KW + AES-CTR](./esdh) | uri-fetch, integrated payload, encryption info (asymmetric ECDH-ES+AES-KW) |
| [Update Management](./update) | uri-fetch, minimum-battery, update-priority, wait-info |
| [Component Metadata](./component-metadata) | uri-fetch, severed element, component metadata (RWX modes) |

## Install & Preparataion
On Debian/Ubuntu environment, run commands below.
```bash
sudo apt-get install -y git
git clone https://github.com/kentakayama/suit-manifest-generator
cd suit-manifest-generator/edn
sudo apt-get -y install curl musl-tools make ruby ruby-dev python3 python3-pip
pip3 install --user -r requirements.txt
sudo gem install cbor-diag cbor-diag-e cddlc cbor-diag-ref cddl
make -C cddl
```
