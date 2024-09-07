TARGETS = foo-pipe

CC	= gcc
CFLAGS = -g -Wall

.phony: clean clobber cl

foo-pipe: foo-pipe.o
	$(CC) $(CFLAGS) -o $@ $<

foo-pipe.o: foo-pipe.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o

clobber: clean
	rm -f $(TARGETS)

cl: clobber
