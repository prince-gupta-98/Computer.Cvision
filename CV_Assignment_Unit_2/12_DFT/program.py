import cv2
import numpy as np
img = cv2.imread(
    "C:\\Users\\Asus\\OneDrive\\Pictures\\WhatsApp Image 2025-03-05 at 1.57.44 AM.jpeg",
    0)
if img is None:
    print("Image not found")
    exit()
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
print("Original shape:", img.shape)
print("DFT shape:", dft.shape)
print("Shifted DFT shape:", dft_shift.shape)
magnitude = cv2.magnitude(
    dft_shift[:, :, 0],
    dft_shift[:, :, 1])
magnitude = 20 * np.log(magnitude + 1)
magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX)
magnitude = np.uint8(magnitude)
cv2.imwrite("output.png", magnitude)
cv2.imshow("Original Image", img)
cv2.imshow("DFT Magnitude Spectrum", magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()