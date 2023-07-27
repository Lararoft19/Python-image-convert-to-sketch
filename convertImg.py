import cv2

# Specify path to image (loading image img1)
img1 = cv2.imread(r'C:\Users\amyde\Downloads\test.jpg')

# Resize the original image to the same size as the sketch image
desired_width = 800
desired_height = 600
img1 = cv2.resize(img1, (desired_width, desired_height))

window_name = 'Original Image'

# Displaying the resized original image
cv2.imshow(window_name, img1)

# Convert image from one color space to another
grey_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

# Image smoothing
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# Save the converted image to the specified path
cv2.imwrite(r'C:\Users\amyde\Downloads\result.jpg', sketch)

# Window name in which image is displayed
window_name = 'Sketch Image'

# Displaying the sketch image
cv2.imshow(window_name, sketch)

# Waits for the user to press any key
# This is necessary to avoid python kernel from crashing
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()
