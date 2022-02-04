#!/usr/bin/env python3.10

"""

- Convert images to webp
- TODO: remove geo locations and other meta data
- Keep the original file to save the raw images

"""

import os
from pathlib import Path
from glob import glob
from PIL import Image

note_images_path = Path("./notes/images/")

if __name__ == "__main__":
    image_paths = list(note_images_path.glob("**/*.jpg"))
    image_paths.extend(note_images_path.glob("**/*.png"))

    for image_path in image_paths:
        # ignore favicon
        if image_path.name == "favicon.png":
            continue

        print(f"Processing {image_path}")

        image = Image.open(image_path).convert("RGB")
        image.save(image_path.with_suffix(".webp"), "webp")
