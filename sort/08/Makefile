CC	= gcc
CFLAGS	= -g -Wall -std=gnu99
INCS	= -I../include/

TARGETS	= \
	  bts \
	  qnl-bts qnl-bts-debug \
	  runtest

all: ${TARGETS}

bucketsort: bucketsort.o
	${CC} ${CFLAGS} -o $@ $^

bucketsort.o: bucketsort.c
	${CC} ${CFLAGS} -c $< ${INCS}

bts: bts.o libsort.o
	${CC} ${CFLAGS} -o $@ $^

bts.o: bts.c
	${CC} ${CFLAGS} -c $< ${INCS}

libsort.o: ../lib/libsort.c
	${CC} ${CFLAGS} -c $< ${INCS}

qnl-bts: qnl-bts.py
	expand -t4 $< > $@
	cp $@ $<
	chmod +x $@

qnl-bts-debug: qnl-bts
	sed -e "s%#import.*pysnooper%import pysnooper%g" -e "s%#@py%@py%g" $< > $@
	chmod +x $@

runtest: runtest.sh
	expand -t4 $< > $@
	cp $@ $<
	chmod +x $@

clean:
	rm -f *.o
clobber: clean
	rm -f ${TARGETS}
cl: clobber
