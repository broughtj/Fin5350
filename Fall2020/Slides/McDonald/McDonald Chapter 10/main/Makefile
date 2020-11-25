all:
	Rscript -e 'rmarkdown::render("Chapter10.Rmd")'


pdf:
	Rscript -e 'rmarkdown::render("Chapter10.Rmd", output_format="beamer_presentation")'


ioChapter10:
	Rscript -e 'rmarkdown::render("Chapter10.Rmd", output_format="ioChapter10_presentation")'

slidy:
	Rscript -e 'rmarkdown::render("Chapter10.Rmd", output_format="slidy_presentation")'


clean:
	rm Chapter10.pdf Chapter10.html