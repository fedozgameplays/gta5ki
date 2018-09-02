import numpy as np
import cv2
import time
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
import os


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
        pass

    return ausgabe

dateiname="trainingsdaten.npy"

if os.path.isfile(dateiname):
    print("Trainingsdaten existieren bereits, lade vorhandene Daten...")
    trainingsdaten = list(np.load(dateiname)) 
else:
    print("Keine Trainingsdaten existieren.")
    trainingsdaten = []

for i in list(range(6))[::-1]:
    print(i+1)
    time.sleep(1)
    
while True:
    bild = bild_erfassen(region=(0,30,800,626))
    bild = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
    bild = cv2.resize(bild, (80,60))
    tasten = key_check()
    ausgabe = tasten_ausgabe(tasten)
    trainingsdaten.append([bild, ausgabe])
    if len(trainingsdaten) % 500 == 0:
        print("100%, speichere...")
        np.save(dateiname, trainingsdaten)
        
