import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    
    return filtered_image


image = cv2.imread("example1.jpg")

if image is None:
    print("ERROR: Image not found!")
else:
    filter_type = "original"

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")

    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)

        keys = cv2.waitKey(0) & 0xFF
        if keys == ord("r"):
            filter_type = "red_tint"
        elif keys == ord("b"):
            filter_type = "blue_tint"
        elif keys == ord("g"):
            filter_type = "green_tint"
        elif keys == ord("i"):
            filter_type = "increase_red"
        elif keys == ord("d"):
            filter_type = "decrease_blue"
        elif keys == ord("q"):
            exit()
        else:
            print("Invalid response: Please Try again")

cv2.destroyAllWindows()
        