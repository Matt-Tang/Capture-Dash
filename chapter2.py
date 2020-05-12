import cv2
import numpy as np

# Basic functions - convert RGB to Gray and other color spaces
img = cv2.imread("images/profile.jpg")
kernel = np.ones((5,5), np.uint8) # Set 5x5 matrix as 1's, values range from 0-255

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts image to different color space
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0) # ksize means kernal size and has to be odd#
imgCanny = cv2.Canny(img, 150, 200) # Edge detection , if we want smaller edges increase the threshold values
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) # Kernel is a matrix, increasing iteration while make the lines much thicker
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) # Makes lines thinner
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
