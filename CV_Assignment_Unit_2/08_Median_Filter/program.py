import cv2
import numpy as np 
img = cv2.imread("c:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg",0)
median = cv2.medianBlur(img,15)
cv2.imshow("output.png",img)
cv2.imshow("medianBlur",median)
cv2.imwrite("output.png",median)
cv2.waitKey(0)
cv2.destroyAllWindows()