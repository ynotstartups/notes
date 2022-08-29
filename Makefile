.DEFAULT_GOAL := serve
# enable ** for recursive
SHELL:=/bin/bash -O globstar
serve:
	. .venv/bin/activate; \
	google-chrome http://127.0.0.1:8000/; \
	mkdocs serve;

install:
	./install.sh;

process-images:
	. .venv/bin/activate; \
	./bin/process-images.py;

format:
	. .venv/bin/activate; \
	pre-commit run --all-files;
