import cv2 as cv
from src.day_1.delete_channel import delete_channel
from src.day_1.hsv_blue_green import convert_blue_to_green
from src.utils import show_image

if __name__=="__main__":
    img = convert_blue_to_green("images/IMG_20220722_130847.jpg")
    img_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    show_image("hsv blue to green", img_bgr)