source = core.c
target = core
optimization_default = 0

compile: $(target)

$(target): $(source)
	g++ $(source) -lpcap -std=c++23 -O$(optimization_default) -o $(target)

clean:
	rm -f $(target)

run: $(target)
	sudo ./$(target)

