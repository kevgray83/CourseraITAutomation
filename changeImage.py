#!/usr/bin/env python3

from PIL import Image
import os

image_dir = "supplier-data/images/"

files = os.listdir(image_dir)
size - (600,400)

for file in files:
	im = Image.open(image_dir + file)
	im.convert("RGB")
	im.resize(size)
	im.save(file +".jpeg")


	
