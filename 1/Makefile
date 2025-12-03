.PHONY: all
all: pt1 pt1-full pt2 pt2-full

.PHONY: pt1
pt1:
	@perl -pe 's/INPUT_GOES_HERE/`cat sample.txt`/ge' pt1.asm > temp.asm
	@as --no-warn -g temp.asm -o pt1.o
	@ld pt1.o -o pt1
	@rm -f temp.asm
	@echo "PT1 - Sample Input:"
	@./pt1

.PHONY: pt1-full
pt1-full:
	@perl -pe 's/INPUT_GOES_HERE/`cat full_input.txt`/ge' pt1.asm > temp.asm
	@as --no-warn -g temp.asm -o pt1.o
	@ld pt1.o -o pt1
	@rm -f temp.asm
	@echo "PT1 - Full Input:"
	@./pt1

.PHONY: pt2
pt2:
	@perl -pe 's/INPUT_GOES_HERE/`cat sample.txt`/ge' pt2.asm > temp.asm
	@as --no-warn -g temp.asm -o pt2.o
	@ld pt2.o -o pt2
	@rm -f temp.asm
	@echo "PT2 - Sample Input:"
	@./pt2

.PHONY: pt2-full
pt2-full:
	@perl -pe 's/INPUT_GOES_HERE/`cat full_input.txt`/ge' pt2.asm > temp.asm
	@as --no-warn -g temp.asm -o pt2.o
	@ld pt2.o -o pt2
	@rm -f temp.asm
	@echo "PT2 - Full Input:"
	@./pt2

clean:
	@rm -f pt1 pt2 *.o temp.asm
