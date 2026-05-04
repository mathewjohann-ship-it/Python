import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
for _ in range(20):

    cap.read()

time.sleep(2)

print("Camera opened:", cap.isOpened())
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:

        fail_count += 1

        print(f"⚠️ Frame failed {fail_count}")

        if fail_count > 5:

            print("❌ Camera unstable, exiting")

            break

        time.sleep(1)

        continue

    fail_count = 0
    #     print("Error: Failed to capture image")
    #     break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.circle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Face Detection - Press q to Quit", frame)
        if cv2.waitKey(1) &0xFF == ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()