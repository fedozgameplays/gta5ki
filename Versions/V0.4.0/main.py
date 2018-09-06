import numpy as np
import cv2
import time
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
import os
import sys

def run(screen_width, screen_height, dateiname):
    def tasten_ausgabe(tasten):
        #[A,W,D]
        ausgabe = [0,0,0]
        if "A" in tasten:
            ausgabe[0] = '1'
        elif "D" in tasten:
            ausgabe[2] = '1'
        elif "W" in tasten:
            ausgabe[1] = '1'
        else:
            ausgabe = [0,0,0]

        return ausgabe
    
    if os.path.isfile(dateiname):
        print("Trainingsdaten existieren bereits, lade vorhandene Daten...")
        trainingsdaten = list(np.load(dateiname)) 
    else:
        print("Keine Trainingsdaten existieren.")
        trainingsdaten = []

    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(1)
        
    paused = False
        
    while True:
        if not paused:
            bild = bild_erfassen(region=(0,30,int(screen_width),int(screen_height)+26))
            bild = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
            #bild = cv2.resize(bild, (int(int(screen_width)/10),int(int(screen_height)/10)))
            bild = cv2.resize(bild, (80,60))
            tasten = key_check()
            ausgabe = tasten_ausgabe(tasten)
            if ausgabe != [0,0,0]:
                trainingsdaten.append([bild, ausgabe])
                
            if len(trainingsdaten) % 500 == 0:
                print("100%, speichere...")
                np.save(dateiname, trainingsdaten)

            keys=key_check()

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)
                
