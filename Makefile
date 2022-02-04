.DEFAULT_GOAL := serve
# enable ** for recursive
SHELL:=/bin/bash -O globstar
serve:
	. .venv/bin/activate; \
	google-chrome http://127.0.0.1:8000/; \
	mkdocs serve;

install:
	./install.sh;

# Deprecated, doesn't work with mdformat
# generate-art-note: compile-art generate-bi-directional-links

# Don't use this, use generate-art-note instead
# Create art.md by looking at image in ./notes/images/art
# compile-art:
# 	. .venv/bin/activate; \
# 	./bin/compile-art.py > ./notes/art.md;

generate-bi-directional-links:
	. .venv/bin/activate; \
	./bin/generate-bi-directional-links.py;

process-images:
	. .venv/bin/activate; \
	./bin/process-images.py;

format:
	. .venv/bin/activate; \
	pre-commit run --all-files;
