import numpy as np
import cv2
import time
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
from steuerung import PressKey, ReleaseKey, W, A, S, D
from alexnet import alexnet
import os
import time

width = 80
height = 60
learning_rate = 1E-3
epoch = 10
model_name = "car-{}-{}-{}-epochs.model".format(learning_rate, "alexnet", epoch)

t_time = 0.09

def geradeaus():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def links():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)

def rechts():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)

def chill():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)



model = alexnet(width, height, learning_rate)
model.load(model_name)

for i in list(range(6))[::-1]:
    print(i+1)
    time.sleep(1)
    
paused = False

while True:
    if not paused:
        bild = bild_erfassen(region=(0,30,800,626))
        bild = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
        bild = cv2.resize(bild, (80,60))
        
        vorhersage = model.predict([bild.reshape(width, height, 1)])[0]
        #moves = list(np.around(vorhersage))
        print(vorhersage)

        turn_thresh = 0.75
        forward_thresh = 0.70

        if vorhersage[1] > forward_thresh:
            geradeaus()
        elif vorhersage[0] > turn_thresh:
            links()
        elif vorhersage[2] > turn_thresh:
            rechts()
        elif vorhersage[0] < 0.1 and vorhersage[1] < 0.1 and vorhersage[2] < 0.1:
            chill()     
        else:
            geradeaus()
            
##        if moves == [1, 0, 0]:
##            links()
##        elif moves == [0, 1, 0]:
##            geradeaus()
##        elif moves == [0, 0, 1]:
##            rechts()

    keys = key_check()

    if 'T' in keys:
        if paused:
            paused = False
            time.sleep(1)
        else:
            paused = True
            ReleaseKey(A)
            ReleaseKey(W)
            ReleaseKey(D)
            time.sleep(1)
            

        
