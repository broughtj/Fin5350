all:
	Rscript -e 'rmarkdown::render("Binomial.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Binomial.Rmd", output_format="beamer_presentation")'


ioBinomial:
	Rscript -e 'rmarkdown::render("Binomial.Rmd", output_format="ioBinomial_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Binomial.Rmd", output_format="slidy_presentation")'


clean:
	rm Binomial.pdf Binomial.html
