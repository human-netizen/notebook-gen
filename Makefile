.PHONY: all clean pdf

all: clean pdf

clean:
	rm -f notebook.aux notebook.log notebook.out notebook.toc notebook.fdb_latexmk notebook.fls notebook.pdf contents.tex
	rm -rf _minted-notebook

pdf:
	python3 generate_pdf.py
