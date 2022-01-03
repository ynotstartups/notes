.DEFAULT_GOAL := serve
# enable ** for recursive
SHELL:=/bin/bash -O globstar

serve:
	. .venv/bin/activate; \
	google-chrome http://127.0.0.1:8000/; \
	mkdocs serve;

install:
	./install.sh;

generate-art-note: compile-art generate-bi-directional-links

# Don't use this, use generate-art-note instead
# Create art.md by looking at image in ./notes/images/art
compile-art:
	. .venv/bin/activate; \
	./bin/compile-art.py > ./notes/art.md;

generate-bi-directional-links:
	. .venv/bin/activate; \
	./bin/generate-bi-directional-links.py;

clean-images:
	# Remove GPS data in images
	# -d '\n' makes whitespace characters to be not delimiter
	# Otherwise, for example, for image file `./notes/images/art/name_Isamu Noguchi_1.jpg`
	# `exiv` will be executed on `./notes/images/art/name_Isamu` and then `Noguchi_1.jpg`
	find . -iregex './notes/images/.*\.\(jpg\|gif\|png\|jpeg\)$\' | xargs -d '\n' exiv2 rm
