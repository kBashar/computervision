
import cv2 as cv
import sys
import numpy as np

from src.utils import show_image


def delete_channel():
    img = cv.imread("images/Instagram_logo_2022.webp", cv.IMREAD_UNCHANGED)

    if img is None:
        sys.exit("Could not read the image.")

    print(f"Dimension of the image: {img.shape}")

    print(f"Data type: {img.dtype}")

    #img[:, :, 0] = np.zeros([img.shape[0], img.shape[1]])

    img[:, :, 2] = 0

    show_image("Channel Removed Image", img)