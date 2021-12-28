#!/usr/bin/env python3.10
import os

PATH_TO_NOTES_IMAGES = "./notes/images/art/"

PATH_FROM_NOTES_TO_ART_IMAGES = "images/art/"

test_image_names = [
    "name_Zadok Ben-David_0.jpg",
    "name_Isamu Noguchi_0.jpg",
    "name_Isamu Noguchi_1.jpg",
    "Staring - City of London_dark.jpg",
    "Staring - City of London_light.jpg"
]

def _slugify(string):
    return string.replace(" ", "-").lower()

def convert_to_markdown(image_names):
    art_markdown = "# Art\n"

    seen_artist_names = set()

    for raw_image_name in image_names:
        name_is_a_person = raw_image_name.startswith("name_")

        if name_is_a_person:
            image_name = raw_image_name.removeprefix("name_")
        else:
            image_name = raw_image_name

        splited_image_name = image_name.split("_")

        assert len(splited_image_name) == 2

        artist_name = splited_image_name[0]
        # remove filename extension
        image_caption = os.path.splitext(image_name)[0]
        image_path = os.path.join(PATH_FROM_NOTES_TO_ART_IMAGES, raw_image_name)

        # Only include header and link to WhoIsThisArtist once
        if artist_name not in seen_artist_names:
            seen_artist_names.add(artist_name)

            # start writing to markdown
            art_markdown += f"## {artist_name}\n"

            if name_is_a_person:
                art_markdown += f"[Who is this artist?](https://whoisthisartist.netlify.app/gallery/{_slugify(artist_name)})\n"
                pass

        art_markdown += f"![{image_caption}]({image_path})\n"

    return art_markdown

assert convert_to_markdown(test_image_names) == """# Art
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
"""

if __name__ == "__main__":
    from os import listdir
    from os.path import isfile, join

    # Sorted by reverse otherwise art work without artist will rank higher
    print(convert_to_markdown(sorted(listdir(PATH_TO_NOTES_IMAGES), reverse=True)))
