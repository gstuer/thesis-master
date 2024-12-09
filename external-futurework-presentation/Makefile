sources = presentation

cleancompile: clean compile

compile:
	latexmk -pdf $(sources).tex

clean:
	rm -f $(sources).pdf
	latexmk -c $(sources).tex
