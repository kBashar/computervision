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

## Miscellinious 

* PNG, webp format has transparency data, Jpeg does not support transparency


## Numpy  

* we can use boolean masking to select a range of values like 
    ```python
    mask=arr>110 & arr<120
    arr[mask] = arr[mask] - 10
    ``` 
    in above example we will subtract 10 from every element that has a value in range of 110-120.