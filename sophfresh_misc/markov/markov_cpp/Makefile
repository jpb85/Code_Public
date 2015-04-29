CC=g++
CFLAGS=-O0
TARGET=./markov_cpp
INFILE=../alice30.txt
OUTFILE=markov_cpp_out.txt

$(TARGET): markov.o 
	$(CC) $(CFLAGS) -o $(TARGET) markov.o
markov.o: markov.cpp
	$(CC) $(CFLAGS) -c markov.cpp
clean:
	rm -f *.o $(TARGET) $(OUTFILE)
run: $(TARGET)
	$(TARGET) <$(INFILE) >$(OUTFILE)
