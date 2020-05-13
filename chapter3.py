import cv2

# Basic functions - resizing image, need to know current image size first
img = cv2.imread("images/profile.jpg")
print(img.shape) # ex output: (1364, 1364, 3) (height, width, # for channel so VGR)
imgResize = cv2.resize(img, (1000, 500))


# Crop image
imgCropped = img[0:200, 200:500] # dont need to use cv function (note height first than width, opencv functions is swapped)


cv2.imshow("Image", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
