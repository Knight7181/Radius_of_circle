# Radius_of_circle
This Python script utilizes the OpenCV library to detect and analyze circles in an input image. It performs the following tasks

## Load Image
The script loads an image named 'circle.jpg' from the current directory.

## Preprocessing
It converts the image to grayscale and applies Gaussian blur to reduce noise.

## Circle Detection
Using the Hough Circle Transform, the script identifies circles in the image, assuming there's only one circle to detect.

## Radius and Area Calculation
It calculates the radius and area of the detected circle using mathematical formulas.

## Display Results
The script prints both the exact and rounded values of the radius and the area of the detected circle.

## Display Image
It displays the input image with the detected circle outlined.
