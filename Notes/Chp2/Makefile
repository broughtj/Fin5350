tex:
	pweave -f pandoc2latex chp2.pmd

pdf:
	pweave -f pandoc2latex chp2.pmd
	pdflatex chp2.tex
	pdflatex chp2.tex
	pdflatex chp2.tex
	rm -f *.log *.aux *.out

html:
	pweave -f md2html chp2.pmd

notebook:
	pweave -f notebook chp2.pmd


clean:
	rm -f *.ipynb *.tex *.aux *.log *.html
