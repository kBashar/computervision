import cv2 as cv
import sys

def show_image(title: str, img):
    cv.imshow(title, img)

    # Wait for key press and ensure clean exit
    while True:
        if cv.waitKey(1) & 0xFF == 27:  # ESC key
            break
        if cv.getWindowProperty(title, cv.WND_PROP_VISIBLE) < 1:
            break

    cv.destroyAllWindows()
    cv.waitKey(1)  # Extra waitKey to ensure window closes