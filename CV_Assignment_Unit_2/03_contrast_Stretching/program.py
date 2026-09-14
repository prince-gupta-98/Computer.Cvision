import cv2
import numpy as np 
img = cv2.imread("c:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg")
minimum = np.min(img)
maximum = np.max(img)
strech = (img-minimum)*(255.0/(maximum-minimum))
strech = strech.astype(np.uint8)
cv2.imshow("output.png",img)
cv2.imshow("strech",strech)
cv2.imwrite("output.png",strech)
cv2.waitKey(0)
cv2.destroyAllWindows