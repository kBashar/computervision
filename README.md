## Image Channels  

A channel of an image represents a layer of color information. 

* Single channel: only contains the darkness and brightness information.
* 3 cahnnels: Contains all three colors (Blue, Green, Red) information, so, one channel contains, red color values per pixel, another channel would have green color values per pixel and so on.
* 4 channles: Apart from containing 3 color channels, contains another extra layer named `alpha` channel. This channel contains transparency value per pixel. 


## HSV color space  
The HSV color space, also known as HSB (Hue, Saturation, Brightness), is a cylindrical representation of colors derived from the RGB color model.
* Hue (H): Represents the color type (e.g., red, blue, green), measured in degrees (0–360°).
* Saturation (S): Represents the intensity or purity of the color (0–1 or 0–100%).
* Value (V): Represents brightness or lightness of the color (0–1 or 0–100%).


## Histogram  
A histogram visualizes the distribution of values in a dataset. To create a histogram, values are grouped into intervals called "bins" (or "buckets") based on ranges, and the frequency of values in each bin is counted and displayed as bars.


## Aspect Ratio  
Aspect ratio is the proportional relationship between width and height of an image. 
By maintaining the aspect ratio when scaling down or up an image we keep the objects within the image in correct propotionate.

Tasks requiring spatial accuracy (object detection, pose estimation, segmentation), maintaining aspect ratio is critical because the exact shape and proportions matter.

## Bluring  
Blurring is technique that can help smooth out anomalies or rough edges in an image and to remove noises.

When a pixel is blurred, it works by substituting its value with an averaged out value from its neighbouring pixel values.

The amount of neighbouring pixels that will be considered is defined through a matrix named kernel. This kernel also holds the weight of each pixel's impact on the blurring.

OpenCV docs: [Filtering and Blurring](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)

## Thresholding  
Thresholding technique is used for segmentation when object or area to be detected has clear intensity gap with surroundings.

For example:
1. Written text on a paper.
2. A road marker on asphalt road.

Thresholding converts a grayscale image to a binary image where pixels having value lower than threshold value has 0(zero/black) and pixels having higher than threshold value has 255 (white/bright) value. As a result areas with high intensity is clearly segmented from low intensity area.

This value assignment can be inverted too.

OpenCV docs: [What is thresholding and related theories](https://docs.opencv.org/4.x/db/d8e/tutorial_threshold.html)

## Miscellinious 

* PNG, webp format has transparency data, Jpeg does not support transparency


## Numpy  

* we can use boolean masking to select a range of values like 
    ```python
    mask=arr>110 & arr<120
    arr[mask] = arr[mask] - 10
    ``` 
    in above example we will subtract 10 from every element that has a value in range of 110-120.