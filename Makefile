DIR_SRC := ./rplugin

.PHONY: tags
tags:
	ctags -R \
		--sort=yes \
		--totals=yes \
		--languages=Python \
		--extra=+f \
		${DIR_SRC}

.PHONY: clean
clean:
	find -type d -name '__pycache__' -exec rm -rf {} +;
	find -type d -name '.mypy_cache' -exec rm -rf {} +;
	rm -f tags
