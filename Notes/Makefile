all:
	Rscript -e 'rmarkdown::render("DeltaHedging.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("DeltaHedging.Rmd", output_format="beamer_presentation")'


ioslides:
	Rscript -e 'rmarkdown::render("DeltaHedging.Rmd", output_format="ioslides_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("DeltaHedging.Rmd", output_format="slidy_presentation")'


clean:
	rm DeltaHedging.pdf DeltaHedging.html
