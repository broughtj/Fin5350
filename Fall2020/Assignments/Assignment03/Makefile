all:
	Rscript -e 'rmarkdown::render("Assignment03.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Assignment03.Rmd", output_format="beamer_presentation")'


ioAssignment03:
	Rscript -e 'rmarkdown::render("Assignment03.Rmd", output_format="ioAssignment03_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Assignment03.Rmd", output_format="slidy_presentation")'


clean:
	rm Assignment03.pdf Assignment03.html
