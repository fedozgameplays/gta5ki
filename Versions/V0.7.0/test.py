import numpy as np
import cv2
import time
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
from steuerung import PressKey, ReleaseKey, W, A, S, D
from inception_v3 import inception3
import os
import time
import random

def run(width, height, learning_rate, epochs):
    model_id = 1     
    nn_width = int(width)/2
    nn_height = int(height)/2
    output_size = 9

    model_name = "model{}-{}_lr-{}_epochs".format(str(model_id),float(learning_rate), str(epochs))


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
        if random.randrange(0,4) == 1:
            PressKey(W)
        else:
            ReleaseKey(W)
        ReleaseKey(A)
        ReleaseKey(D)
        ReleaseKey(S)



    model = inception3(int(nn_width), int(nn_height), float(learning_rate), output=int(output_size))
    model.load(model_name)

    for i in list(range(6))[::-1]:
        print(i+1)
        time.sleep(1)
        
    paused = False

    while True:
        if not paused:
            bild = bild_erfassen(region=(0,30,int(width),int(height)+26))
            bild = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)
            bild = cv2.resize(bild, (int(nn_width),int(nn_height)))
            #cv2.imshow("test", bild)
            #time.sleep(0.09)

            vorhersage = model.predict([bild.reshape(int(nn_width), int(nn_height), 3)])[0]
            vorhersage = np.array(vorhersage)  * np.array([0.3, 0.9, 2.8, 2.8, 1.5, 1.5, 0.5, 0.5, 0.7])
            #print(vorhersage)
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

##            if cv2.waitKey(15) & 0xFF == ord("q"):
##                cv2.destroyAllWindows()
##                break
                
                

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
                

            
