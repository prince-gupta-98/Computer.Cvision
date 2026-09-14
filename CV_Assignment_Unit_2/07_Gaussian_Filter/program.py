import cv2
import numpy as np 
img = cv2.imread("c:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg",0)
gaussian = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("output.png",img)
cv2.imshow("GaussianBlur",gaussian)
cv2.imwrite("output.png",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()