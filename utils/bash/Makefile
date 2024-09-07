TARGETS = qnl.clvt \
		  qnl.lsgen

all: $(TARGETS)

.phony: clean clobber cl

%: %.sh
	expand -t4 $< > $@
	cp $@ $<
	chmod +x $@

clean:

clobber: clean
	rm -f $(TARGETS)

cl: clobber
