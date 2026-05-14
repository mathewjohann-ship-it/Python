import cv2
import numpy as np
import os
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

WIN = "AI Brightness Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame error")
        break
    
    fram = cv2.flip(frame, 1)

    h, w = frame.shape[:2]
    results = model(frame, verbose = False)
    detections = results[0].boxes
    person_found = False
    for box in detections:
        cls = int(box.cls[0])

        if cls == 0:
            person_found = True

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            area = (x2 - x1) * (y2 - y1)
            brightness = int(np.interp(area, [5000, 150000], [20, 100]))
            brightness = max(20, min(brightness, 100))
            os.system(f"brightness {brightness/100}")
            cv2.putText(frame, f"brightness: {brightness}%", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(frame, "Move closer = brighter", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            break

        if not person_found:
            cv2.putText(frame, "No person detected", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow(WIN, frame)
            key = cv2.waitKey(1)&0xFF
            if key == 27 or key == ord("q"):
                break

cap.release()
cv2.destroyAllWindows()
