# Bulk image resizer

# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

# import numpy as np
# import cv2
import os
from PIL import Image

dir_path = os.getcwd()
print(dir_path)
for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".jpg"):
        image = Image.open(filename)
        resized = image.resize((400, 400))
        resized.save(filename)
        print(resized.size)

# import cv2

# img = cv2.imread('20200905_134613.jpg', cv2.IMREAD_UNCHANGED)

# print('Original Dimensions : ', img.shape)

# scale_percent = 60  # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# # resize image
# resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# print('Resized Dimensions : ', resized.shape)

# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
