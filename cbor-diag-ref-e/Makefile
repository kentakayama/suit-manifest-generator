SUIT_MANIFEST_CDDL=./cddl/suit-manifest.cddl
RUBYDEBUG=RUBYOPT="-W0"
CFLAGS=-Os -Wall

.PHONY: all
all: hello hello.suit-envelope.cbor

hello: hello.o
	$(CC) $(CFLAGS) -o $@ $<
	strip hello

hello.o: hello.c
	$(CC) $(CFLAGS) -c -o $@ $<

%.cbor: %.gdiag # generated SUIT Manifest (cbor) files
	$(RUBYDEBUG) diag2cbor.rb $< > $@

%.gdiag: %.rediag # generated diag files
	$(RUBYDEBUG) CBOR_DIAG_CDDL=$(SUIT_MANIFEST_CDDL) diag2diag.rb -e -d -aref -ae $< > $@

hello.bin.hdiag: hello
%.bin.hdiag:
	python3 ./bin-to-diag-hex.py $< > $@

hello.size.gdiag: hello
%.size.gdiag:
	ls -s $< | awk '{printf "%s",$$1}' > $@

.PRECIOUS: hello.digest.hex hello.suit-manifest.digest.hex
hello.digest.hex: hello
hello.suit-manifest.digest.hex: hello.suit-manifest.cbor
%.digest.hex:
	sha256sum $< | awk '{printf "%s",$$1}' > $@

hello.digest.hdiag: hello.digest.hex
hello.suit-manifest.digest.hdiag: hello.suit-manifest.digest.hex
%.digest.hdiag:
	@echo -n "h'" > $@
	cat $< >> $@
	@echo "'" >> $@

hello.suit-envelope.gdiag: hello.suit-digest.gdiag hello.suit-mac.mdiag hello.suit-manifest.gdiag hello.bin.hdiag

hello.suit-digest.gdiag: hello.suit-manifest.digest.hdiag

hello.suit-manifest.gdiag: hello.digest.hdiag hello.size.gdiag

hello.suit-mac.bin: hello.suit-digest.cbor
	python3 cwt-mac.py $< $@

hello.suit-mac.mdiag: hello.suit-mac.bin
	cbor2diag.rb -e $< > $@

.PHONY: cddl
cddl: $(SUIT_MANIFEST_CDDL)

$(SUIT_MANIFEST_CDDL):
	$(MAKE) -C cddl

TEST_COMMAND := $(RUBYDEBUG) cddl $(SUIT_MANIFEST_CDDL) validate hello.suit-envelope.cbor
.PHONY: test
test: all
	@echo ${TEST_COMMAND}
	@if ${TEST_COMMAND}; then \
		echo "[SUCCESS] Generated SUIT Manifest binary 'hello.suit-envelope.cbor' matches to the CDDL of SUIT Manifest."; \
	else \
		echo "[FAIL] Generated SUIT Manifest binary 'hello.suit-envelope.cbor' doesn't match to the CDDL of SUIT Manifest."; exit 1; \
	fi

.PHONY: clean
clean:
	$(RM) *.gdiag *.hex *.hdiag *.mdiag *.cbor *.bin hello hello.o
