import numpy as np
import imageio
import scipy.ndimage
import cv2

Cyan = "\033[0;36m"
Purple = "\033[0;35m"
Green = "\033[0;32m"
Blue = "\033[0;34m"

print(Purple + """

888888ba                               
88    `8b                              
88     88 88d888b. .d8888b. dP  dP  dP 
88     88 88'  `88 88'  `88 88  88  88 
88    .8P 88       88.  .88 88.88b.88' 
8888888P  dP       `88888P8 8888P Y8P""")

img = input(
    Cyan +
    "\n\n\nPlease enter the directory and file name of the program. (Ex: C:/Users/user/Desktop/image.png)\n\n >  "
)
print(Green + "\n\nProcessing Your Image...")
print(Blue + "\n\nYour Image Should Now Be Created In The Direcotry You Entered.\n\n")


def rgb2gray(rgb):
  return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def dodge(front, back):
  final_sketch = front * 255 / (255 - back)
  final_sketch[final_sketch > 255] = 225
  final_sketch[back == 255] = 255

  return final_sketch.astype('uint8')


ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 255 - gray

blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)

r = dodge(blur, gray)

cv2.imwrite('virat-sketch.png', r)
