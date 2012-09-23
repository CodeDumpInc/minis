CC = gcc
CFLAGS=-Wall -g
LIBS=-lglut

OBJ = glVersion.o
BIN = glVersion

all: $(OBJ)
	$(CC) $(CFLAGS) -o glVersion $(OBJ) $(LIBS)

%.o: %.c
	$(CC) -Wall -c $<

.PHONY: clean
clean:
	rm -rf $(OBJ)

.PHONY: fullclean
fullclean:
	rm -rf $(BIN)
	
