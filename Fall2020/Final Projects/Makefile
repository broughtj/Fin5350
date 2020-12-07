all:
	Rscript -e 'rmarkdown::render("final-project.Rmd", output_format=c("html_document", "pdf_document", "word_document"))'

html:
	Rscript -e 'rmarkdown::render("final-project.Rmd", output_format="html_document")'

pdf:
	Rscript -e 'rmarkdown::render("final-project.Rmd", output_format="pdf_document")'

word:
	Rscript -e 'rmarkdown::render("final-project.Rmd", output_format="word_document")'

clean:
	rm final-project.html final-project.pdf final-project.docx final-project.tex
