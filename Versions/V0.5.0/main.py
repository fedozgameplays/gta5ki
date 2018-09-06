import numpy as np
import cv2
import time
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
import os
import sys

def run(screen_width, screen_height, dateiname):
    def tasten_ausgabe(tasten):
        #[W,A,S,D,WA,WD,SA,SD,nokey]
        ausgabe = [0,0,0,0,0,0,0,0,0]
        if "W" in tasten:
            ausgabe = [1,0,0,0,0,0,0,0,0]
        elif "S" in tasten:
            ausgabe = [0,1,0,0,0,0,0,0,0]
        elif "A" in tasten:
            ausgabe = [0,0,1,0,0,0,0,0,0]
        elif "D" in tasten:
            ausgabe = [0,0,0,1,0,0,0,0,0]
        elif "W" in tasten and "A" in tasten:
            ausgabe = [0,0,0,0,1,0,0,0,0]
        elif "W" in tasten and "D" in tasten:
            ausgabe = [0,0,0,0,0,1,0,0,0]
        elif "S" in tasten and "A" in tasten:
            ausgabe = [0,0,0,0,0,0,1,0,0]
        elif "S" in tasten and "D" in tasten:
            ausgabe = [0,0,0,0,0,0,0,1,0]
        else:
            ausgabe = [0,0,0,0,0,0,0,0,1]

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
            nn_width = int(screen_width)/10
            nn_height = int(screen_height)/10
            bild = cv2.resize(bild, (int(nn_width),int(nn_height)))
            tasten = key_check()
            ausgabe = tasten_ausgabe(tasten)
            trainingsdaten.append([bild, ausgabe])
                
            if len(trainingsdaten) % 500 == 0:
                print(str(len(trainingsdaten)) + " , speichere...")
                np.save(dateiname, trainingsdaten)
            if len(trainingsdaten) == 20001:
                sys.exit()

            keys=key_check()

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)
                
