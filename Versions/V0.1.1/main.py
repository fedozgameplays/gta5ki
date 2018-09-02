import numpy as np
import cv2
import time
from steuerung import PressKey, ReleaseKey, W, A, S, D
from bild_erfassen import bild_erfassen
from spuren_zeichnen import spuren_zeichnen

def roi(img, ecken):
    maske=np.zeros_like(img)
    cv2.fillPoly(maske, ecken, 255)
    masked=cv2.bitwise_and(img, maske)
    return masked

def process_img(image):
    original_image = image
    processed_image = cv2.Canny(image, threshold1=200, threshold2=320)
    processed_image = cv2.GaussianBlur(processed_image,(5,5),0)
    ecken = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],[700,500],[600,300],[200,300],[100,500]], np.int32)
    processed_image = roi(processed_image, [ecken])
    linien = cv2.HoughLinesP(processed_image, 1, np.pi/180, 180, np.array([]) ,50, 10)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1, m2 = spuren_zeichnen(original_image,linien)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [255,255,0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        pass
    try:
        for koordinaten in linien:
            koordinaten = koordinaten[0]
            try:
                cv2.line(processed_image, (koordinaten[0], koordinaten[1]), (koordinaten[2], koordinaten[3]), [255,0,0], 30)
            except Exception as e:
                pass
    except Exception as e:
        pass
            
    return processed_image, original_image, m1, m2

for i in list(range(6))[::-1]:
    print(i+1)
    time.sleep(1)

def geradeaus():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def links():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)

def rechts():
    PressKey(D)
    PressKey(W)
    ReleaseKey(A)

def langsam():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

while True:
    screen=bild_erfassen(region=(0,30,800,626))
    screen2, original_image, m1, m2 = process_img(screen)
    cv2.imshow("window", screen2)
    cv2.imshow("window2", cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    if m1 < 0 and m2 < 0:
        rechts()
    elif m1 > 0 and m2 > 0:
        links()
    else:
        geradeaus()
    if cv2.waitKey(10) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
