import cv2

#Read the image
image = cv2.imread("isaiah.jpg")
cv2.imshow('Bird', image)
cv2.waitKey(0)

# Create new image by converting the original to greyscale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Bird", gray_image)
cv2.waitKey(0)

#invert the new greyscale image 
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

#blur the image 
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#Invert the blurred image, convert the image to a pencil sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)



