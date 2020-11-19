all:
	Rscript -e 'rmarkdown::render("Binomial-Annotated.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Binomial-Annotated.Rmd", output_format="beamer_presentation")'


ioBinomial-Annotated:
	Rscript -e 'rmarkdown::render("Binomial-Annotated.Rmd", output_format="ioBinomial-Annotated_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Binomial-Annotated.Rmd", output_format="slidy_presentation")'


clean:
	rm Binomial-Annotated.pdf Binomial-Annotated.html
