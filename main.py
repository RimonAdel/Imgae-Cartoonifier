import cv2
import numpy as np

img = cv2.imread("./test_image.jpeg")

# detecting edges
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)                                                                 # convert image to gray scale
blurred_img = cv2.medianBlur(gray, 5)                                                                       # median filter for smoothing and keeping edges
edges = cv2.Laplacian(gray, cv2.CV_8U)
_,edges = cv2.threshold(edges, 7, 255, cv2.THRESH_BINARY_INV)

# smoothing colored image
color_blured_image = cv2.bilateralFilter(img, 9, 300, 300)

#cartoon effect
cartoon = cv2.bitwise_and(color_blured_image, color_blured_image, mask=edges)

cv2.imshow("image", img)
# cv2.imshow("blur", blurred_img)
# cv2.imshow("gray", gray)
# cv2.imshow("edges", edges)
# cv2.imshow("color_blured_image", color_blured_image)
cv2.imshow("cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()