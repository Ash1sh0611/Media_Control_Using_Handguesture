import cv2
import mediapipe as mp
import numpy as np
from keras.models import load_model
import time
import pyautogui

def inference():
    # Load the trained model and labels
    model = load_model('model.h5')
    label = np.load('labels.npy')

    # Initialize MediaPipe Holistic
    holistic = mp.solutions.holistic
    holis = holistic.Holistic()

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    # Initialize variables for tracking time and actions
    action_time = 0
    action_flag = False

    while True:
        end_time = time.time()
        lst = []
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        # Process the frame with MediaPipe Holistic
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        # Check if at least one hand is detected
        if res.left_hand_landmarks or res.right_hand_landmarks:

            # Extract hand landmarks and normalize
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                lst.extend([0.0] * 42)

            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                lst.extend([0.0] * 42)

            lst = np.array(lst).reshape(1, -1)

            # Make predictions using the model
            pred = label[np.argmax(model.predict(lst))]
            # print("Prediction:", pred)

            # Check if predicted value persists for more than 5 seconds
            if pred == "PlayOrPause" or pred == "FastForward" or pred=="Backward" or pred == "Up" or pred == "Down":
                if not action_flag:
                    action_time = time.time()
                    action_flag = True
                elif time.time() - action_time >= 3:
                    if pred == "PlayOrPause":
                        print("space")
                        pyautogui.press("space")
                    elif pred == "Up":
                        print("up")
                        pyautogui.press("up")
                    elif pred == "FastForward":
                        print("right")
                        pyautogui.press("right")
                    elif pred == "Backward":
                        print("backward")
                        pyautogui.press("left")
                    elif pred == "Down":
                        print("down")
                        pyautogui.press("down")
                    
                    action_flag = False

            # Display prediction on the frame
            cv2.putText(frm,pred, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("window", frm)

        # Exit loop on pressing ESC
        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

#
# inference()
