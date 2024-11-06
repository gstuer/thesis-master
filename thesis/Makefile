sources = thesis

compile:
	latexmk -pdf $(sources).tex

clean:
	rm -f $(sources).pdf
	latexmk -c $(sources).tex

cleancompile: clean compile
