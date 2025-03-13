OBJF = test1.o test2.o test3.o
test : $(OBJF)
	gcc -o $@ $^
.c.o:
	gcc -c $<
clean:test $(OBJF)
	rm -rf $^
