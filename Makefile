.DEFAULT_GOAL := serve
# enable ** for recursive
SHELL:=/bin/bash -O globstar
serve:
	google-chrome http://127.0.0.1:8000/; \
	mkdocs serve;

install:
	./install.sh;

process-images:
	python bin/process-images.py;

format:
	pre-commit run --all-files;
