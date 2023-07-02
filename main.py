# import required modules computer vision
import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import transform

# read the image
img = cv2.imread('data/frame.jpg')
# convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# transform the image
dst = transform(img, img.shape)

# plot the image
plt.figure(figsize=(10, 10))
plt.imshow(dst)
plt.show()
