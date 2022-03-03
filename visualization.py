import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def calculate_angle(first, mid, end):
    first = np.array(first)
    mid = np.array(mid)
    end = np.array(end)

    radians = np.arctan2(end[1] - mid[1], end[0] - mid[0]) - np.arctan2(first[1] - mid[1], first[0] - mid[0])
    angle = np.abs(radians * 180 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


def visualizer(first_angle=0, second_angle=0, third_angle=0, fourth_angle=0, fifth_angle=0):
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

                joint_angles = {
                    "left_elbow": [[landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y],

                                   [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y],

                                   [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                                   ],

                    "left_wrist": [[landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y],

                                   [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y],

                                   [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                                   ],

                    "left_shoulder": [[landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                       landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y],

                                      [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                       landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y],

                                      [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                       landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                                      ],

                    "left_hip": [[landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y],

                                 [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y],

                                 [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                                 ],

                    "left_knee": [[landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y],

                                  [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y],

                                  [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                                  ],

                    "left_ankle": [[landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y],

                                   [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y],

                                   [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                                   ],

                    "right_elbow": [[landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y],

                                    [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y],

                                    [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                                    ],

                    "right_wrist": [[landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y],

                                    [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y],

                                    [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                                    ],

                    "right_shoulder": [[landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y],

                                       [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y],

                                       [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                                       ],

                    "right_hip": [[landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y],

                                  [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y],

                                  [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                                  ],

                    "right_knee": [[landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                    landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y],

                                   [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                    landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y],

                                   [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                    landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                                   ],

                    "right_ankle": [[landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y],

                                    [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y],

                                    [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                                    ]
                }

                try:
                    first_measured_angle = calculate_angle(joint_angles[first_angle][0],
                                                           joint_angles[first_angle][1],
                                                           joint_angles[first_angle][2])

                    cv2.putText(image, str(first_measured_angle),
                                tuple(np.multiply(joint_angles[first_angle][1], [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                except:
                    pass

                try:
                    second_measured_angle = calculate_angle(joint_angles[second_angle][0],
                                                            joint_angles[second_angle][1],
                                                            joint_angles[second_angle][2])

                    cv2.putText(image, str(second_measured_angle),
                                tuple(np.multiply(joint_angles[second_angle][1], [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                except:
                    pass

                try:
                    third_measured_angle = calculate_angle(joint_angles[third_angle][0],
                                                           joint_angles[third_angle][1],
                                                           joint_angles[third_angle][2])

                    cv2.putText(image, str(third_measured_angle),
                                tuple(np.multiply(joint_angles[third_angle][1], [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                except:
                    pass

                try:
                    fourth_measured_angle = calculate_angle(joint_angles[fourth_angle][0],
                                                            joint_angles[fourth_angle][1],
                                                            joint_angles[fourth_angle][2])

                    cv2.putText(image, str(fourth_measured_angle),
                                tuple(np.multiply(joint_angles[fourth_angle][1], [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                except:
                    pass

                try:
                    fifth_measured_angle = calculate_angle(joint_angles[fifth_angle][0],
                                                           joint_angles[fifth_angle][1],
                                                           joint_angles[fifth_angle][2])

                    cv2.putText(image, str(fifth_measured_angle),
                                tuple(np.multiply(joint_angles[fifth_angle][1], [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                except:
                    pass

            except:
                pass

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
