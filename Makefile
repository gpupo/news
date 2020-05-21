# Build docs index
.SILENT:
CURRENT_DIR := $(shell pwd)

## build
build:
	git checkout master;
	git reset --hard 1.0.0;
	git rebase develop;
	python3 ./start.py > docs/index.md;
	git commit -am 'Updated news';
	git push -f;
	git checkout develop;
