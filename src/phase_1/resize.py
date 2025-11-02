import sys

import cv2 as cv


def half_the_image(imagepath: str):
    img = cv.imread(imagepath)

    if img is None:
        print(f"Image not found at {imagepath}")
        sys.exit(0)
    
    height, width = img.shape[:2]

    new_height, new_width = int(height * 0.5), int(width * 0.5)

    halfed_image = cv.resize(img, (new_width, new_height))

    return halfed_image


def shorten_image(imagepath: str, percent=25):
    img = cv.imread(imagepath)

    if img is None:
        print(f"Image not found at {imagepath}")
        sys.exit(0)
    
    height, width = img.shape[:2]
    multiplier = percent / 100
    new_height, new_width = int(height * multiplier), int(width * multiplier)

    halfed_image = cv.resize(img, (new_width, new_height))

    return halfed_image