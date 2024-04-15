#
# Copyright (c) 2023 SECOM CO., LTD. All Rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause
#

SUIT_ENCRYPTION_INFO = \
	encryption_info_image_aeskw_gcm.cose \
	encryption_info_image_esdh_gcm.cose \
	encryption_info_config_aeskw_gcm.cose \
	encryption_info_config_esdh_gcm.cose \
	encryption_info_config_esdh_ctr.cose

SUIT_ENCRYPT := ../scripts/suit_payload_encryption.py

.PHONY: all
all: $(SUIT_ENCRYPTION_INFO)

.PRECIOUS: encrypted_image_aeskw_gcm.bin
encryption_info_image_aeskw_gcm.cose: ../plaintext/raw_image.bin
	$(SUIT_ENCRYPT) $< A128KW         A128GCM $@ encrypted_image_aeskw_gcm.bin

.PRECIOUS: encrypted_image_esdh_gcm.bin
encryption_info_image_esdh_gcm.cose: ../plaintext/raw_image.bin
	$(SUIT_ENCRYPT) $< ECDH-ES+A128KW A128GCM $@ encrypted_image_esdh_gcm.bin

.PRECIOUS: encrypted_config_aeskw_gcm.bin
encryption_info_config_aeskw_gcm.cose: ../plaintext/config.json
	$(SUIT_ENCRYPT) $< A128KW         A128GCM $@ encrypted_config_aeskw_gcm.bin

.PRECIOUS: encrypted_config_esdh_gcm.bin
encryption_info_config_esdh_gcm.cose: ../plaintext/config.json
	$(SUIT_ENCRYPT) $< ECDH-ES+A128KW A128GCM $@ encrypted_config_esdh_gcm.bin

.PRECIOUS: encrypted_config_esdh_ctr.bin
encryption_info_config_esdh_ctr.cose: ../plaintext/config.json
	$(SUIT_ENCRYPT) $< ECDH-ES+A128KW A128CTR $@ encrypted_config_esdh_ctr.bin
