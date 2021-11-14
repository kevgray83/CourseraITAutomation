#!/usr/bin/env python3

import requests
import os

url = "http:// /upload/"


image_dir = "~/supplier-data/images"

files = os.listdir(image_dir)

for file in files:
    ext = os.path.splittext(file)[-1].lower()
    if ext == ".jpeg":
        with open(file, "rb") as opened:
            r = requests.post(url, files={"file":opened})
    else:
        continue
        

  