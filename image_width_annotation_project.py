import cv2
import matplotlib.pyplot as plt

image = cv2.imread("car.jpeg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

rect1_width, rect1_height = 20, 20
top_left1 = (5, 5)
bottom_left1 = (top_left1[0] + rect1_width, top_left1[1]+rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_left1, (255, 0, 0), 0)

rect2_width, rect2_height = 20, 15
top_left2 = (width - rect2_width - 10, height - rect2_height - 10)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 0)

center1_x = top_left1[0] + rect1_width//2
center1_y = top_left1[1] + rect1_height//2
center2_x = top_left2[0] + rect2_width//2
center2_y = top_left2[1] + rect2_height//2
cv2.circle(image_rgb, (center1_x, center1_y), 2, (0, 255, 0), -1)
cv2.circle(image_rgb, (center2_x, center2_y), 2, (0, 255, 0), -1)

cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 2)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, "Region 1", (top_left1[0] + 20, top_left1[1]+10), font, 0.4, (255, 255, 255), 0, cv2.LINE_AA)
cv2.putText(image_rgb, "Region 2", (top_left2[0] - 60, top_left2[1] + 10), font, 0.4, (255, 255, 255), 0, cv2.LINE_AA)

arrow_start = (width-10, 10)
arrow_end = (width-10, height-30)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

height_label_position = (arrow_start[0] - 250, (arrow_start[1] + arrow_end[1]//2))
cv2.putText(image_rgb, f"Height: {height} px", height_label_position, font, 1, (255, 255, 0), 1, cv2.LINE_AA)

arrow_start1 = (10, height - 10)
arrow_end1 = (width-10, height-10)

cv2.arrowedLine(image_rgb, arrow_start1, arrow_end1, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end1, arrow_start1, (255, 255, 0), 3, tipLength=0.05)

height_label_position = (arrow_start1[0] - 10, (arrow_start1[1]-100 + arrow_end1[1]//2))
cv2.putText(image_rgb, f"Width: {width} px", height_label_position, font, 1, (255, 255, 0), 1, cv2.LINE_AA)

plt.figure(figsize = (12, 8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis("off")
plt.show()


