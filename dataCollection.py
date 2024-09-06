import mediapipe as mp
import numpy as np
import cv2

def datacollection(value):
    cap = cv2.VideoCapture(0)

    holistic = mp.solutions.holistic
    hands = mp.solutions.hands
    holis = holistic.Holistic()
    drawing = mp.solutions.drawing_utils

    x = []
    data_size = 0
    # max_landmarks = 21  # Maximum number of landmarks for each hand and face combined

    while True:
        lst = []
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))


        if res.pose_landmarks:
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                # Fill in zeros if left hand landmarks are not detected
                for _ in range(42):  # 21 is the total number of hand landmarks
                    lst.append(0.0)

            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                # Fill in zeros if right hand landmarks are not detected
                for _ in range(42):  # 21 is the total number of hand landmarks
                    lst.append(0.0)
        #
        x.append(lst)
        data_size += 1

        # drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
        drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
        drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)

        cv2.putText(frm, str(data_size), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("window", frm)


        if cv2.waitKey(1) == 27 or data_size > 99:
            cap.release()
            cv2.destroyAllWindows()
            break

    np.save(f"{value}.npy", np.array(x))
    print(np.array(x).shape)

