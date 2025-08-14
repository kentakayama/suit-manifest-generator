DATA_FLOW := flow.png manifest.png

.PHONY: all
all: $(DATA_FLOW)

%.svg: %.aasvg
	aasvg < $< > $@

%.png: %.svg
	inkscape -b FFFFFF $< -o $@

.PHONY: clean
clean:
	$(RM) *.svg