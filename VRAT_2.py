import cv2
import mediapipe as mp
import imutils
import requests
import numpy as np
import pyautogui as ptg
import autopy

plocx, plocy = 0, 0
clocx, clocy = 0, 0
smothing = 10
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
url = "http://192.168.43.1:8080/shot.jpg"
#vframe = 100
#hand_no = 8
value = " "

ws, hs= autopy.screen.size()
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.2) as hands:
    while True:

        img = requests.get(url)
        img_arr = np.array(bytearray(img.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        image = imutils.resize(img, width=640, height=480)

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lh = []

        if results.multi_hand_landmarks:
            for my_hand in results.multi_hand_landmarks:
                for id, lm in enumerate(my_hand.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lh.append([id, cx, cy])
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        #try:
        ##    h, w, c = image.shape
         #   cv2.rectangle(image, (vframe, vframe), (w-vframe,h-vframe),(25,150,255),3)
        ##except:
         #   pass
       # try:
            #if lh[8][2] < lh[6][2] and lh[12][2] > lh[10][2] and lh[16][2] > lh[14][2] and lh[20][2] > lh[18][2]:
                #value = "two"

           # if lh[8][2] < lh[6][2] and lh[12][2] < lh[10][2] and lh[16][2] > lh[14][2] and lh[20][2] > lh[18][2]:
       #        value = "two"
            #    ptg.click()
       #     else:
       #         value = " "
       # except:
       ##     pass
       # if value == "one":
        #    pass
            #ptg.click(button='left')
        #elif value == "two":
        #    ptg.click(button='left')
        #else:
        #    pass
       # h, w, c = image.shape
        # current center
        x, y = ptg.position()
        if results.multi_hand_landmarks:
            w, h, c = image.shape
            ccx, ccy = lh[8][1], lh[8][2]
            x3 = np.interp(ccx, (0, w), (0, ws))
            y3 = np.interp(ccy, (0, h), (0, hs))
            x3 = x3 - x
            y3 = y3 - y
            #print(x3,y3)
           # clocx = plocx + (x3 - plocx) / smothing
            #clocy = plocy + (y3 - plocx) / smothing


                   # autopy.mouse.move(ws-x3, y3)

            ptg.moveRel(x3,y3)

            #plocx, plocy = clocx, clocy

        # current position
      #  x, y = ptg.position()
#        try:
#            if ccx > pcx:
#                x = ((ccx-pcx)/w)*1366
#            elif ccx < pcx:
#                x = ((pcx-ccx)/w)*1366
#            else:
#                pass
#        except :
#            pass
#        try:
#            if ccy > pcy:
#                y = ((ccy-pcy)/h)*768
#            elif ccy < pcy:
#                y = ((pcy-ccy)/h)*768
#
#            else:
#                pass
#        except:
#            pass
#        autopy.mouse.move(x,y)
  #      try:
  #          x3 = np.interp(ccx,(vframe,w-vframe),(0,ws))
  #          y3 = np.interp(ccy,(vframe,h-vframe),(0,hs))
  ##          clocx = plocx + (x3 - plocx)/smothing
    #        clocy = plocy + (y3 - plocx)/smothing
    ##        autopy.mouse.move(clocx, clocy)
     #       plocx, plocy = clocx, clocy
     #   except:
     #       pass
       # try:
       #     autopy.mouse.move(clocx, clocy)
       # except:
       #     pass
        cv2.imshow('MediaPipe Hands', image)
        #print(value)
        if cv2.waitKey(5) & 0xFF == 27:
            break
        #print(h,w)
        #try:
            # previuse center
            #pcx, pcy = lh[0][1], lh[0][2]
         #   plocx, plocy = clocx, clocy
        #except:
        ##    pass

cv2.destroyAllWindows()
