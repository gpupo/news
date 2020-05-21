# Build docs index
.SILENT:
CURRENT_DIR := $(shell pwd)

## build
build:
	git checkout master;
	git reset --hard ab70f518eeb6c0ace5f6fec4a6455c0f6c0ae11d;
	git rebase develop;
	python3 ./start.py > docs/index.md;
	git commit -am 'Updated news';
	git push -f;
	git checkout develop;
