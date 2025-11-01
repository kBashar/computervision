import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def show_color_histogram(imgpath: str):
    # Read the image
    img = cv.imread(imgpath, cv.IMREAD_COLOR_RGB)

    # Calculate histogram for each color channel
    colors = ('r', 'g', 'b')
    plt.figure(figsize=(10, 6))

    for i, color in enumerate(colors):
        # cv2.calcHist parameters: [image], [channel], mask, [histSize], [ranges]
        histogram = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f'{color.upper()} channel')

    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Color Histogram')
    plt.legend()
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    
    # Save instead of show
    plt.savefig('histogram.png', dpi=150, bbox_inches='tight')
    plt.close()

    print("Histogram saved as 'histogram.png'")