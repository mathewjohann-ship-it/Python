import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands
TIP = H.HandLandmark
ids = {
    "thumb": TIP.THUM_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP,
}

hands = H.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
pairs = {"middle":("SEPIA", "NEGATIVE"), "ring":("BLUR", "GLITCH"), "pinky":("EDGE", "CARTOON")}
st = {k:0 for k in pairs}; cur = "SEPIA"
DEB, CAP, TT, TP = 0.6, 1.2, 30, 20
la = lc = 0; pinch_on = False
MAIN, POP = "Gesture-Controlled Photo App", "Captured (ESC / Close to resume)"
