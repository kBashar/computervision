import sys
import cv2 as cv 
import numpy as np


from src.utils import show_image


def convert_to_greyscale(image_path: str):
    """Convert an image to greyscale manually"""
    img = cv.imread(image_path, cv.IMREAD_UNCHANGED)

    if img is None:
        print(f"No image found at {image_path}")
        sys.exit(0)
    
   # img_gray = img[:,:,0]*0.114 + img[:,:,1]*0.587 + img[:,:,2]*0.299
    img_gray = img[:,:,0] + img[:,:,1] + img[:,:,2]

    # to convert to int in a range of 0-255

    img_gray = img_gray.astype("uint8")

    return img_gray

