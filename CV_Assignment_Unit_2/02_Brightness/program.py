import cv2
import numpy as np

img = cv2.imread(
    "C:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg"
)

brightness = np.ones(img.shape, dtype=np.uint8) * 50

bright_img = cv2.add(img, brightness)

print("Before:", img[100, 100])
print("After:", bright_img[100, 100])

cv2.imshow("Original", img)
cv2.imshow("Bright Image", bright_img)

cv2.imwrite("../02_Brightness/output.png", bright_img)

cv2.waitKey(0)
cv2.destroyAllWindows()