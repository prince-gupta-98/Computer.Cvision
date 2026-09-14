import cv2 
import numpy as np 

img = cv2.imread("C:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg", 0)

if img is not None:
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharp = cv2.filter2D(img, -1, kernel)

    cv2.imshow("original image", img)
    cv2.imshow("sharpened image", sharp)

    cv2.imwrite("output.png", sharp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

