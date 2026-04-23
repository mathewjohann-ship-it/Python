import cv2

def apply_filter(image, filter_type):
    image1 = image.copy()
    if filter_type == "red_tint":
        image1[:,:, 1] = 0
        image1[:, :, 0] = 0
    elif filter_type == "green_tint":
        image1[:,:, 0] = 0
        image1[:, :, 2] = 0
    elif filter_type == "blue_tint":
        image1[:,:, 1] = 0
        image1[:, :, 2] = 0
    elif filter_type == "increase_red":
        image1[:, :, 2] = cv2.add(image1[:, :, 2], 50)
    elif filter_type == "increase_green":
        image1[:, :, 1] = cv2.add(image1[:, :, 1], 50)
    elif filter_type == "increase_blue":
        image1[:, :, 0] = cv2.add(image1[:, :, 0], 50)
    elif filter_type == "decrease_red":
        image1[:, :, 2] = cv2.subtract(image1[:, :, 2], 50)
    elif filter_type == "decrease_green":
        image1[:, :, 1] = cv2.subtract(image1[:, :, 1], 50)
    elif filter_type == "decrease_blue":
        image1[:, :, 0] = cv2.subtract(image1[:, :, 0], 50)
    elif filter_type == "increase_contrast":
        image1[:, :, 2] = cv2.add(image1[:, :, 2], 50)
        image1[:, :, 1] = cv2.add(image1[:, :, 1], 50)
        image1[:, :, 0] = cv2.add(image1[:, :, 0], 50)
    elif filter_type == "decrease_contrast":
        image1[:, :, 2] = cv2.subtract(image1[:, :, 2], 50)
        image1[:, :, 1] = cv2.subtract(image1[:, :, 1], 50)
        image1[:, :, 0] = cv2.subtract(image1[:, :, 0], 50)
    return image1

choice = input("What picture would you like?:\n1. Bird\n2.Forest\n")
if choice == "1":
    path = "example1.jpg"
else:
    path = "example2.jpg"

image = cv2.imread(path)
filter_type = "original"

print("Press the following keys to apply filters:")
print("r - Red Tint")
print("b - Blue Tint")
print("g - Green Tint")
print("y - Increase Red Intensity")
print("u - Increase Green Intensity")
print("i - Increase Blue Intensity")
print("j - Decrease Red Intensity")
print("k - Decrease Green Intensity")
print("l - Decrease Blue Intensity")
print("n - Increase Contrast")
print("m - decrease Contrast")
print("o - Original Image")
print("q - Quit")

while True:
    filtered_image = apply_filter(image, filter_type)
    cv2.imshow("Filtered Image", filtered_image)

    keys = cv2.waitKey(0) & 0xFF
    if keys == ord("r"):
        filter_type = "red_tint"
    elif keys == ord("b"):
        filter_type = "blue_tint"
    elif keys == ord("g"):
        filter_type = "green_tint"
    elif keys == ord("y"):
        filter_type = "increase_red"
    elif keys == ord("u"):
        filter_type = "increase_green"
    elif keys == ord("i"):
        filter_type = "increase_blue"
    elif keys == ord("j"):
        filter_type = "decrease_red"
    elif keys == ord("k"):
        filter_type = "decrease_green"
    elif keys == ord("l"):
        filter_type = "decrease_blue"
    elif keys == ord("n"):
        filter_type = "increase_contrast"
    elif keys == ord("m"):
        filter_type = "decrease_contrast"
    elif keys == ord("o"):
        filter_type = "original_image"
    elif keys == ord("q"):
        exit()
    else:
        print("Invalid response: Please Try again")

cv2.destroyAllWindows()