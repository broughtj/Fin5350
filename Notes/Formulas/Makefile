all:
	pweave -f pandoc formulas.pmd
	pandoc formulas.md -V geometry:landscape -o formulas.pdf

clean:
	rm *.md *.pdf
