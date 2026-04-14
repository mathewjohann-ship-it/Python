import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("project image.jpeg")

(w, h) = image.shape[:2]

M = cv2.getRotationMatrix2D((w//2, h//2), 90, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))
rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_image_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8")*50
brighter = cv2.add(image, brightness_matrix)
plt.imshow(brighter)
plt.title("Brighter Image")
plt.show()

cropped_image = image[50:200, 50:200]
plt.imshow(cropped_image)
plt.title("Cropped Image")
plt.show()