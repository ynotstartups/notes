.DEFAULT_GOAL := serve
SHELL:=/bin/bash
serve:
	source .venv/bin/activate && mkdocs serve;

install:
	./install.sh;

process-images:
	python bin/process-images.py;

format:
	pre-commit run --all-files;
