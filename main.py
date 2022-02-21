from math import radians
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(first,mid,end):
    first = np.array(first)
    mid = np.array(mid)
    end = np.array(end)

    radians = np.arctan2(end[1]-mid[1], end[0]-mid[0]) - np.arctan2(first[1]-mid[1], first[0]-mid[0])
    angle = np.abs(radians*180/np.pi)

    if angle > 180.0:
        angle = 360 - angle
    
    return angle

cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:

            landmarks = results.pose_landmarks.landmark

            Left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                             landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

            Left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                          landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

            Left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                          landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            Elbow_angle = calculate_angle(Left_shoulder,Left_elbow,Left_wrist)

            cv2.putText(image, str(Elbow_angle),
                        tuple(np.multiply(Left_elbow,[640,480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)

            Right_foot_index = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x, 
                                landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
            
            Right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, 
                           landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

            Right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, 
                          landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

            Ankle_angle = calculate_angle(Right_foot_index,Right_ankle,Right_knee)

            cv2.putText(image, str(Ankle_angle),
                        tuple(np.multiply(Right_ankle,[640,480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)

        except:
            pass

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()