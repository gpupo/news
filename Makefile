# Build docs index
.SILENT:
CURRENT_DIR := $(shell pwd)

## build
build:
	python3 ./start.py > docs/index.md