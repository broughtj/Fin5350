all:
	Rscript -e 'rmarkdown::render("TJB.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("TJB.Rmd", output_format="beamer_presentation")'


ioTJB:
	Rscript -e 'rmarkdown::render("TJB.Rmd", output_format="ioTJB_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("TJB.Rmd", output_format="slidy_presentation")'


clean:
	rm TJB.pdf TJB.html
