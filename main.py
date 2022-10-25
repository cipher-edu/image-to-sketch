import cv2
image = cv2.imread('gril.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = cv2.bitwise_not(gray_image)
blur_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blur = cv2.bitwise_not(blur_image)
sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
cv2.imwrite("sketch.jpg", sketch)