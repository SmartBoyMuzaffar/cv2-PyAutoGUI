import cv2
import pyautogui as m
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector

import fingers as fn

detector = HandDetector(detectionCon=0.8, maxHands=2)
f_detector = FaceDetector()
video = cv2.VideoCapture(0)

r_btnpressed = False
l_btnpressed = False

l_hand = []
r_hand = []

while True:

    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    faces = f_detector.findFaces(frame)

    if hands:
        print(hands[0]["type"])

        try:

            r_hand = detector.fingersUp(hands[0])
            l_hand = detector.fingersUp(hands[1])
            if r_hand and hands[0]["type"] == "Right":
                if hand in fn.finger0 and r_btnpressed:
                    r_btnpressed = False
                    m.press('win')

                elif hand in fn.finger5 and r_btnpressed == False:
                    r_btnpressed = True
                    m.press('win')

                else:
                    pass
            if l_hand and hands[1]["type"] == "Left":
                # print(l_hand, hands[1]["type"])

                if l_hand in fn.finger0 and l_btnpressed == False:
                    l_btnpressed = True
                    m.hotkey('win', 'tab')

                elif l_hand in fn.finger5 and l_btnpressed:
                    l_btnpressed = False
                    m.hotkey('win', 'tab')

                else:
                    pass
        except:
            pass


        # print("\n*******************************")
        
        hand = detector.fingersUp(hands[0])
        if hands[0]["type"] == "Right":

            if hand in fn.finger0 and r_btnpressed:
                r_btnpressed = False
                m.press('win')

            elif hand in fn.finger5 and r_btnpressed == False:
                r_btnpressed = True
                m.press('win')

            else:
                pass
        elif hands[0]["type"] == "Left":
            if hand in fn.finger0 and l_btnpressed == False:
                l_btnpressed = True
                m.hotkey('win', 'tab')

            elif hand in fn.finger5 and l_btnpressed:
                l_btnpressed = False
                m.hotkey('win', 'tab')

            else:
                pass
        else:
            pass
    else:
        pass
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break
    else:
        pass

video.release()
cv2.destroyAllWindows()
