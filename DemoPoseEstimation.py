import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)
    
    if results.detections:
        for detection in results.detections:
            mp_draw.draw_detection(frame, detection)
    
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
