import cv2
import numpy as np


img = cv2.imread("images/profile.jpg")

# This will not work if the color channels are not the same
# horizontal = np.hstack((img,img)) # this is a numpy function, after all a picture is just a 2D array
# vertical = np.vstack((img,img))
#
# cv2.imshow("Horizontal", horizontal)
# cv2.imshow("Vertical", vertical)
cv2.waitKey(0)