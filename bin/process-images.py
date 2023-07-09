#!/usr/bin/env python

"""
- Convert images to webp
- remove geo locations and other meta data
- delete original image file
"""

from pathlib import Path
import os
from PIL import Image

note_images_path = Path("./notes/images/")

if __name__ == "__main__":

    image_paths = []
    for root, dirs, files in os.walk(note_images_path):
        for file in files:
            if file.endswith(("jpg", "jpeg", "png")):
                path = Path(root,file)
                image_paths.append(path)

    if not image_paths:
        print(f"Cannot find new images with extention jpeg, jpg or png")
        exit(1)

    for image_path in image_paths:
        image_webp_path = image_path.with_suffix(".webp")

        print(f"Processing {image_path}")
        # remove image meta data, such as geolocation
        image = Image.open(image_path)
        image_data = list(image.getdata())
        image_without_metadata = Image.new(image.mode, image.size)
        image_without_metadata.putdata(image_data)
        image_without_metadata.save(image_path)

        # save to webp
        image_without_metadata.convert("RGB")
        image_without_metadata.save(image_webp_path, "webp")

        # remove image file
        image_path.unlink()
