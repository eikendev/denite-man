.PHONY: all
all: tags

.PHONY: clean
clean:
	find -type d -name '__pycache__' -exec rm -rf {} +;
	find -type d -name '.mypy_cache' -exec rm -rf {} +;
	rm -f tags

.PHONY: tags
tags:
	ctags -R --extra=+f .
