import cv2
import mediapipe as mp
import numpy as np
import os
from ultralytics import YOLO


mp_hands = mp.solution.hands
hands = mp.hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
mp_draw = mp.soltutions.drawing_utils
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
if not cap.isOpened():
    print("Error:, Could not access the webcam.")
    exit()
WIN = "AI Brightness Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)
print("Hand Tracking Started! Press 'q' to quit.")

def detect_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [2, 6, 10, 14, 17]
    extended = 0

    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
        extended += 1
    
    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
            extended += 1
    
    if extended >= 4:
        return "Open"
    elif extended <= 1:
        return "Closed Fist"
    else:
        return "Partial"

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    gesture = "No hand detected"

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[idx].classification[0].label
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingertip_ids = [4, 8, 12, 16, 20]
            for tip_id in fingertip_ids:
                lm = hand_landmarks.landmarks[tip_id]
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 10, (255, 0, 255), cv2.FILLED)
                cv2.putText(frame, str(tip_id), (x - 5, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
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


            wrist = hand_landmarks.landmark[0]

            wrist_x, wrist_y = int(wrist.x * w), int(wrist.y * h)

            cv2.putText(frame, f"{hand_label} Hand", (wrist_x - 40, wrist_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    status_color = (0, 255, 0) if gesture in ["Open", "Closed Fist"] else (0, 165, 255)
    cv2.putText(frame, f"Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)
    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()

            