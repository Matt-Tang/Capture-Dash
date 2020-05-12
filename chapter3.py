import cv2

# Basic functions - resizing image, need to know current image size first
img = cv2.imread("images/profile.jpg")
print(img.shape) # ex output: (1364, 1364, 3) (height, width, # for channel so VGR)
imgResize = cv2.resize(img, (300, 200))
cv2.imshow("Image", imgResize)
cv2.waitKey(0)
