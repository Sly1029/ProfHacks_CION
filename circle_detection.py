import numpy as np
import argparse
import cv2
from PIL import Image

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to the image")
#args = vars(ap.parse_args())
# load the image, clone it for output, and then convert it to grayscale
filename = "images/color_correct.jpg"
image = cv2.imread(filename)
image_data = np.asanyarray(image)
output = image.copy()
m = Image.open(filename)
pix = m.load()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),0);
gray = cv2.medianBlur(gray,5)


# Adaptive Guassian Threshold is to detect sharp edges in the Image. For more information Google it.
gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3.5)
param2_num = 11
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.35, 100,
                               param1=100,
                               param2=10,
                               minRadius=30,
                               maxRadius=150
                               )

while circles.shape[1] != 3:
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.35, 100,
                               param1=100,
                               param2=param2_num,
                               minRadius=35,
                               maxRadius=150
                               )
    param2_num+=1
# ensure at least some circles were found
avg = 0
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")


    # loop over the (x, y) coordinates and radius of the circles
    x1 = 0
    y1 = 0
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        x1 = np.uint64(x).item()
        y2 = np.uint64(y).item()
        print(x1,y2)
        print(pix[x1, y2])
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # show the output image
    cv2.imshow("output", image)
    cv2.waitKey(0)
