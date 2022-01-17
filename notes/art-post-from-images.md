# Art Post From Images

This describes how to generate the [art](art.md) note from images.

The purpose is to simplify the creation of art note.

## Requirements

1. generate markdown file based on image names without other information
1. group images by artist name or an arbitrary string under markdown header
1. if it is an artist name, generate a link to [Who Is This Artist](https://whoisthisartist.netlify.app/gallery/zadok-ben-david) with slugified artist name, if there is no artist name, don't generate link to Who Is This Artist
1. order art works with name first

## Implementation

To distinguish whether it contains an artist name, we need to include this information in the image names.

I decided to use prefix `name_` to indicate when it is an artist name. The artwork name will be after the last underscore. So the format is like `name_foo_bar.jpg`, where `name_` is optional.

For example:

```
name_Zadok Ben-David_0.jpg
name_Isamu Noguchi_0.jpg
name_Isamu Noguchi_1.jpg
Staring - City of London_dark.jpg
Staring - City of London_light.jpg
```

So the python script read the filenames and generate the following markdown.

```markdown
# Art
## Zadok Ben-David
[Who is this artist?](https://whoisthisartist.netlify.app/gallery/zadok-ben-david)
![Zadok Ben-David_0](images/art/name_Zadok Ben-David_0.jpg)
## Isamu Noguchi
[Who is this artist?](https://whoisthisartist.netlify.app/gallery/isamu-noguchi)
![Isamu Noguchi_0](images/art/name_Isamu Noguchi_0.jpg)
![Isamu Noguchi_1](images/art/name_Isamu Noguchi_1.jpg)
## Staring - City of London
![Staring - City of London_dark](images/art/Staring - City of London_dark.jpg)
![Staring - City of London_light](images/art/Staring - City of London_light.jpg)
```

I also have a Make script to generate this art post.

```
compile-art:
	. .venv/bin/activate; \
	./bin/compile-art.py > ./notes/art.md;
```

You can see the final implementation [here](https://github.com/ynotstartups/notes/blob/main/bin/compile-art.py).

## Workflow

1. add images with **correct names** to `./notes/images/art`
1. run `make compile-art` to generate art note
1. git commit and git push to publish
