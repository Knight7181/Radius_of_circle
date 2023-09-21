import cv2
import numpy as np
import math

# Load the image
image = cv2.imread('circle.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray_blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0
)

if circles is not None:
    circles = np.uint16(np.around(circles))

    x, y, radius = circles[0][0]

    rounded_radius = round(radius, 2)  # Round to 2 decimal places

    # Calculate the area of the circle
    area = math.pi * (radius ** 2)
    rounded_area = round(area, 2)

    # Mark the center of the circle
    cv2.circle(image, (x, y), 2, (0, 0, 255), 3)  # Red center mark

    cv2.circle(image, (x, y), radius, (0, 0, 255), 2)  # Red outline of circle

    print(f"Radius of the circle: {radius} units")
    print(f"Radius of the circle in round figure: {rounded_radius} units")
    print(f"Area of the circle: {rounded_area} square units")
else:
    print("No circle detected in the image.")

cv2.imshow('Circle Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
