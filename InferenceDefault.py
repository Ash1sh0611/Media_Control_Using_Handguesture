import cv2
import mediapipe as mp
import pyautogui
import time

def inferenceDefault():


    cnt = 0

    def count_fingers(lst):
        cnt = 0

        thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

        if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
            cnt += 1

        return cnt

    cap = cv2.VideoCapture(0)

    d = {
        0: "",
        1: "Up",
        2: "Down",
        3: "Forward",
        4: "Backward",
        5: "PlayOrPause"
    }

    action_time = 0
    action_flag = False

    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hand_obj = hands.Hands(max_num_hands=1)

    start_init = False

    prev = -1

    while True:
        end_time = time.time()
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:

            hand_keyPoints = res.multi_hand_landmarks[0]

            cnt = count_fingers(hand_keyPoints)

            if cnt == 1 or cnt == 2 or cnt == 3 or cnt == 4 or cnt == 5:
                if not action_flag:
                    action_time = time.time()
                    action_flag = True
                elif time.time() - action_time >= 3:
                    if cnt == 5:
                        print("space")
                        pyautogui.press("space")
                    elif cnt == 1:
                        print("up")
                        pyautogui.press("up")
                    elif cnt == 3:
                        print("right")
                        pyautogui.press("right")
                    elif cnt == 4:
                        print("backward")
                        pyautogui.press("left")
                    elif cnt == 2:
                        print("down")
                        pyautogui.press("down")

                    action_flag = False

            drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)
        else:
            cnt = 0

        cv2.putText(frm, d[cnt], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("window", frm)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break

