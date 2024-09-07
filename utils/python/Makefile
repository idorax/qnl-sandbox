TARGETS = qnl.tcolor

all: $(TARGETS)

.phony: clean clobber cl

%: %.py
	expand -t4 $< > $@
	cp $@ $<
	chmod +x $@

clean:

clobber: clean
	rm -f $(TARGETS)

cl: clobber
