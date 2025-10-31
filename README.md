## Image Channels  

A channel of an image represents a layer of color information. 

* Single channel: only contains the darkness and brightness information.
* 3 cahnnels: Contains all three colors (Blue, Green, Red) information, so, one channel contains, red color values per pixel, another channel would have green color values per pixel and so on.
* 4 channles: Apart from containing 3 color channels, contains another extra layer named `alpha` channel. This channel contains transparency value per pixel. 


## HSV color space  
The HSV color space, also known as HSB (Hue, Saturation, Brightness), is a cylindrical representation of colors derived from the RGB color model.
 It is designed to be more intuitive for human perception, separating color information from intensity.
 In this model, Hue represents the color type and is measured as an angle around a color cylinder, typically ranging from 0° to 360°, where 0° and 360° correspond to red.
 Saturation indicates the purity or intensity of the color, ranging from 0% (a shade of gray) to 100% (fully saturated).
 Value (or Brightness) represents the maximum intensity of the color components, ranging from 0 (black) to 100% (white or a saturated color depending on saturation).

## Miscellinious 

* PNG, webp format has transparency data, Jpeg does not support transparency


## Numpy  

* we can use boolean masking to select a range of values like 
    ```python
    mask=arr>110 & arr<120
    arr[mask] = arr[mask] - 10
    ``` 
    in above example we will subtract 10 from every element that has a value in range of 110-120.