all:
	Rscript -e 'rmarkdown::render("hwk3.Rmd", output_format=c("html_document", "pdf_document", "word_document"))'

html:
	Rscript -e 'rmarkdown::render("hwk3.Rmd", output_format="html_document")'

pdf:
	Rscript -e 'rmarkdown::render("hwk3.Rmd", output_format="pdf_document")'

word:
	Rscript -e 'rmarkdown::render("hwk3.Rmd", output_format="word_document")'

clean:
	rm hwk3.html hwk3.pdf hwk3.docx hwk3.tex
