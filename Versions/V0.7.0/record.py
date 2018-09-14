import numpy as np
import cv2
from bild_erfassen import bild_erfassen
from tasten_erfassen import key_check
import os
import sys
import time

def run(screen_width, screen_height):
    
    startwert = 1

    nn_width = int(screen_width)/2
    nn_height = int(screen_height)/2

    w = [1,0,0,0,0,0,0,0,0]
    s = [0,1,0,0,0,0,0,0,0]
    a = [0,0,1,0,0,0,0,0,0]
    d = [0,0,0,1,0,0,0,0,0]
    wa = [0,0,0,0,1,0,0,0,0]
    wd = [0,0,0,0,0,1,0,0,0]
    sa = [0,0,0,0,0,0,1,0,0]
    sd = [0,0,0,0,0,0,0,1,0]
    nokey = [0,0,0,0,0,0,0,0,1]

    while True:
        dateiname = "trainingsdaten-{}.npy".format(startwert)
        if os.path.isfile(dateiname):
            print("Trainingsdaten existieren bereits, lade vorhandene Daten... (%s)" % (str(startwert)))
            startwert = int(startwert)+1
        else:
            print("Keine Trainingsdaten existieren.")
            break
    
    def tasten_ausgabe(tasten):
        #[W,A,S,D,WA,WD,SA,SD,nokey]
        ausgabe = [0,0,0,0,0,0,0,0,0]
        if "W" in tasten and "A" in tasten:
            ausgabe = wa
        elif "W" in tasten and "D" in tasten:
            ausgabe = wd
        elif "S" in tasten and "A" in tasten:
            ausgabe = sa
        elif "S" in tasten and "D" in tasten:
            ausgabe = sd
        elif "W" in tasten:
            ausgabe = w
        elif "S" in tasten:
            ausgabe = s
        elif "A" in tasten:
            ausgabe = a
        elif "D" in tasten:
            ausgabe = d
        else:
            ausgabe = nokey

        return ausgabe

    def main(dateiname, startwert):
        
        dateiname = dateiname
        startwert = startwert
        trainingsdaten=[]
        for i in list(range(10))[::-1]:
            print(i+1)
            time.sleep(1)
        
        paused = False
        while(True):
            if not paused:
                bild = bild_erfassen(region=(0,30,int(screen_width),int(screen_height)+26))
                bild = cv2.resize(bild, (int(nn_width),int(nn_height)))
                bild = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)
                
                tasten = key_check()
                ausgabe = tasten_ausgabe(tasten)
                trainingsdaten.append([bild, ausgabe])
                
                if len(trainingsdaten) % 100 == 0:
                    print("Länge der Trainingsdaten: "+str(len(trainingsdaten)))
                    
                    if len(trainingsdaten) == 500:
                        print("Länge: "+str(len(trainingsdaten)) + ", speichere...")
                        np.save(dateiname, trainingsdaten)
                        trainingsdaten = []
                        startwert = int(startwert) + 1
                        dateiname = "trainingsdaten-{}.npy".format(startwert)

            keys=key_check()

            if 'T' in keys:
                if paused:
                    paused = False
                    time.sleep(1)
                else:
                    paused = True
                    time.sleep(1)

    main(dateiname, startwert)
            
                    
