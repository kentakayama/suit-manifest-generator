DATA_FLOW := flow.png

.PHONY: all
all: $(DATA_FLOW)

%.svg: %.aasvg
	aasvg < $< > $@

%.png: %.svg
	inkscape -b FFFFFF $< -e $@

.PHONY: clean
clean:
	$(RM) *.svg