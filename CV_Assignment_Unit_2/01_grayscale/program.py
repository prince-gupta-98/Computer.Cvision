import cv2
img = cv2.imread(
    "C:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg"
)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imwrite("grayscale.png", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()