TARGETS = colordiff

all: $(TARGETS)

.phony: clean clobber cl

%: %.pl
	cp $< $@
	chmod +x $@

clean:

clobber: clean
	rm -f $(TARGETS)

cl: clobber
