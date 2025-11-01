
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

img = cv.imread("Instagram_logo_2022.webp", cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Could not read the image.")

print(f"Dimension of the image: {img.shape}")

print(f"Data type: {img.dtype}")


show_image("Channel Removed Image", img)