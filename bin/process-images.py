#!/usr/bin/env python3.10

"""
- Convert images to webp
- remove geo locations and other meta data
- delete original image file
"""

from pathlib import Path
from glob import glob
from PIL import Image

note_images_path = Path("./notes/images/")

if __name__ == "__main__":
    image_paths = list(note_images_path.glob("**/*.jpg"))
    image_paths.extend(note_images_path.glob("**/*.png"))

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
