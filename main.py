import cv2 as cv
from src.phase_1.delete_channel import delete_channel
from src.phase_1.to_gray import convert_to_greyscale
from src.phase_1.hsv_blue_green import convert_blue_to_green
from src.utils import show_image
from src.phase_1.metadata import show_metadata
from src.phase_1.histogram import show_color_histogram
from src.phase_1.resize import half_the_image, shorten_image, resize_to_fixed_width
from src.phase_1.thresholding import global_thresholding

if __name__=="__main__":
    image_path = "images/asphalt_road_white_mark.jpg"
    # img = convert_blue_to_green("images/IMG_20220722_130847.jpg")
    # img_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    # show_image("hsv blue to green", img_bgr)

    #show_metadata("images/IMG_20220722_130847.jpg")

    #show_color_histogram(image_path)

    #img = shorten_image(image_path, percent=10)
    # img = resize_to_fixed_width(image_path, new_width=640)
    img = global_thresholding(image_path)
    show_image("resized image", img)
