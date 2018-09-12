import numpy as np
import cv2
import time
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
from steuerung import PressKey, ReleaseKey, W, A, S, D
from alexnet import alexnet
import os
import time
import random

def run(width, height, learning_rate, epochs):
    for i in range(1,10):
        check_model = "car-{}-{}-{}.model".format(str(i),str(learning_rate),str(epochs))
        if os.path.isfile(check_model):
            print("Model existiert bereits: "+str(check_model))
        else:
            model_name = "car-{}-{}-{}.model".format(str(i),str(learning_rate),str(epochs))
            return model_name
    nn_width = int(width)/2
    nn_height = int(height)/2
    t_time = 0.09

    def geradeaus():
        PressKey(W)
        ReleaseKey(A)
        ReleaseKey(D)
        ReleaseKey(S)

    def links():
        if random.randrange(0,3) == 1:
            PressKey(W)
        else:
            ReleaseKey(W)
        PressKey(A)
        ReleaseKey(D)
        ReleaseKey(S)

    def rechts():
        if random.randrange(0,3) == 1:
            PressKey(W)
        else:
            ReleaseKey(W)
        PressKey(D)
        ReleaseKey(A)
        ReleaseKey(S)

    def zurücksetzen():
        PressKey(S)
        ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(D)

    def geradeaus_links():
        PressKey(W)
        PressKey(A)
        ReleaseKey(D)
        ReleaseKey(S)

    def geradeaus_rechts():
        PressKey(W)
        PressKey(D)
        ReleaseKey(A)
        ReleaseKey(S)

    def zurücksetzen_links():
        PressKey(S)
        PressKey(A)
        ReleaseKey(W)
        ReleaseKey(D)

    def zurücksetzen_rechts():
        PressKey(S)
        PressKey(D)
        ReleaseKey(W)
        ReleaseKey(A)

    def nichts():
        if random.randrange(0,3) == 1:
            PressKey(W)
        else:
            ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(D)
        ReleaseKey(S)



    model = alexnet(int(nn_width), int(nn_height), float(learning_rate))
    model.load(model_name)

    for i in list(range(6))[::-1]:
        print(i+1)
        time.sleep(1)
        
    paused = False

    while True:
        if not paused:
            bild = bild_erfassen(region=(0,30,int(width),int(height)+26))
            bild = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)
            nn_width = int(width)/2
            nn_height = int(height)/2
            bild = cv2.resize(bild, (int(nn_width),int(nn_height)))

            vorhersage = model.predict([bild.reshape(int(nn_width), int(nn_height), 3)])[0]
            vorhersage = np.array(vorhersage) * np.array([4.5, 0.1, 0.1, 0.1,  1.8,   1.8, 0.5, 0.5, 0.2])
            print(vorhersage)
            auswahl = np.argmax(vorhersage)

            if auswahl == 0:
                geradeaus()
                auswahl_getroffen = "Geradeaus"
            elif auswahl == 1:
                zurücksetzen()
                auswahl_getroffen = "Zurücksetzen"
            elif auswahl == 2:
                links()
                auswahl_getroffen = "Links"
            elif auswahl == 3:
                rechts()
                auswahl_getroffen = "Rechts"
            elif auswahl == 4:
                geradeaus_links()
                auswahl_getroffen = "Geradeaus + Links"
            elif auswahl == 5:
                geradeaus_rechts()
                auswahl_getroffen = "Geradeaus + Rechts"
            elif auswahl == 6:
                zurücksetzen_links()
                auswahl_getroffen = "Zurücksetzen + Links"
            elif auswahl == 7:
                zurücksetzen_rechts()
                auswahl_getroffen = "Zurücksetzen + Rechts"
            elif auswahl == 8:
                nichts()
                auswahl_getroffen = "Nichts"

            print(auswahl_getroffen)
                
                

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
                ReleaseKey(S)
                time.sleep(1)
                

            
