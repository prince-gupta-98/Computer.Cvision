import cv2 
import numpy as np 

img = cv2.imread("c:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg", 0)

if img is not None:
    mean = cv2.blur(img, (5, 5))
    gaussian = cv2.GaussianBlur(img, (9, 9), 0)
    median = cv2.medianBlur(img, 15)

    cv2.imshow("original image", img)
    cv2.imshow("mean image", mean)
    cv2.imshow("gaussian image", gaussian)
    cv2.imshow("median image", median)

    cv2.imwrite("output_mean.png", mean)
    cv2.imwrite("output_gaussian.png", gaussian)
    cv2.imwrite("output_median.png", median)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
