import cv2 as cv
import numpy as np


def show_metadata(imgpath: str):

    img = cv.imread(imgpath, cv.IMREAD_UNCHANGED)

    if img is None:
        print("No image found at the path: {imgpath}")
    
    print(f"image shape is {img.shape}")

    