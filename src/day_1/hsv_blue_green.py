import cv2 as cv
import numpy as np
import sys

def convert_blue_to_green(img_path):
    img = cv.imread(img_path, cv.IMREAD_COLOR_RGB)
    
    if img is None:
        print(f"Image not found in {img_path}")
        sys.exit(0)

    img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

    print(f"shape of data {img_hsv.shape}")
    max_hue = np.max(img_hsv[:,:,0])
    print(f"max hue of the img is {max_hue}")

    hue = img_hsv[:,:,0]

    blue_mask = (hue > 100) & (hue <131)

    hue[blue_mask] = hue[blue_mask] - 65

    img_hsv[:,:,0] = hue 

    return img_hsv
