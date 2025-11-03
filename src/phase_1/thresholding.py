import cv2 as cv

def global_thresholding(image_path: str):

    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    if img is None:
        print(f"No image found at {image_path}")
    
    img = cv.GaussianBlur(img, (3,3,), 0)

    ret, bin_img = cv.threshold(img, 200, 255, cv.THRESH_BINARY)

    return bin_img