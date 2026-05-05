import cv2
import matplotlib.pyplot as plt
image = cv2.imread("car.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cropped_image = gray[1500:4000, 0:5000]



cv2.imshow("Filtered Image", cropped_image)
cv2.imshow("Original Image", image)

if cv2.waitKey(0)&0xFF == ord("q"):
    exit()

cv2.destroyAllWindows()