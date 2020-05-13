import cv2
import numpy as np

width,height = 250,350

img = cv2.imread("images/profile.jpg")
pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]]) # here is where we want to "crop"
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # here is how we define pts1 and remake into new picture
                                                               # and redefine the points for picture 2
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)