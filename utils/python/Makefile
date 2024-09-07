TARGETS = qnl.tcolor \
		  qnl.get-bash-PS4

all: $(TARGETS)

.phony: clean clobber cl

%: %.py
	expand -t4 $< > $@
	cp $@ $<
	pep8 $<
	chmod +x $@

clean:

clobber: clean
	rm -f $(TARGETS)

cl: clobber
