SRCS = $(wildcard *.c)
PROGS = $(patsubst %.c,%,$(SRCS))

all:$(PROGS)
% : %.c
	gcc -o $@ $^
clean : $(PROGS)
	rm -rf $^