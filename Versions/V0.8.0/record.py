import h5py
import cv2
from bild_erfassen import grab_screen
from tasten_erfassen import key_check
import os
import time
import threading
import sys


def run():
    nn_width = 480
    nn_height = 270

    startwert = 1

    w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
    a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
    d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
    wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
    wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
    sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
    sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
    nokey = [0, 0, 0, 0, 0, 0, 0, 0, 1]

    lock = threading.Lock()

    while True:
        dateiname = "trainingsdaten/trainingsdaten-{}.h5".format(startwert)
        if os.path.isfile(dateiname):
            print("Trainingsdaten existieren bereits, lade vorhandene Daten... ({})".format(str(startwert)))
            startwert = int(startwert) + 1
        else:
            print("Keine Trainingsdaten existieren.")
            break

    def tasten_ausgabe(tasten):
        # [W, A, S, D, WA, WD, SA, SD, nokey]
        ausgabe = [0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    def speichern(trainings_bilder, trainings_steuerung):
        global datei
        with lock:
            if trainings_bilder:
                datei["bild"].resize((datei["bild"].shape[0] + len(trainings_bilder)), axis=0)
                datei["bild"][-len(trainings_bilder):] = trainings_bilder
                datei["steuerung"].resize((datei["steuerung"].shape[0] + len(trainings_steuerung)), axis=0)
                datei["steuerung"][-len(trainings_steuerung):] = trainings_steuerung

    def open(startwert):
        datei = None
        dateiname = "trainingsdaten/trainingsdaten-{}.h5".format(startwert)
        datei = h5py.File(dateiname, "w")
        datei.create_dataset("bild", (0, 270, 480, 3), dtype="u1", maxshape=(None, 270, 480, 3), chunks=(50, 270, 480, 3))
        datei.create_dataset("steuerung", (0, 9), dtype="i1", maxshape=(None, 9), chunks=(50, 9))
        return datei

    def main(startwert):
        global datei
        startwert = startwert
        trainings_bilder = []
        trainings_steuerung = []
        bilder = 0
        datei = open(startwert)
        for i in list(range(6))[::-1]:
            print(i+1)
            time.sleep(1)

        paused = False
        closed = False
        newfile = False
        while not closed:
            if not paused:
                bild = grab_screen()
                bild = cv2.resize(bild, (int(nn_width), int(nn_height)))
                bild = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)

                tasten = key_check()
                ausgabe = tasten_ausgabe(tasten)
                trainings_bilder.append(bild)
                trainings_steuerung.append(ausgabe)

                if len(trainings_bilder) % 50 == 0:
                    bilder = int(bilder) + 50
                    print("Speichere Daten in Datei {}, Länge insgesamt: {}".format(str(startwert), str(bilder)))
                    threading.Thread(target=speichern, args=(trainings_bilder, trainings_steuerung)).start()
                    trainings_bilder = []
                    trainings_steuerung = []
                    newfile = False

                if bilder > 0 and bilder % 10000 == 0 and newfile is False:
                    startwert = int(startwert) + 1
                    print("Länge: 10000, erstelle neue Datei ({})".format(str(startwert)))
                    datei = open(startwert)
                    newfile = True

                time.sleep(0.01)

            keys = key_check()

            if 'T' in keys:
                if paused:
                    paused = False
                    time.sleep(1)
                else:
                    paused = True
                    time.sleep(1)

            if 'C' in keys:
                closed = True
                datei.close()
                time.sleep(1)
                sys.exit()

    main(startwert)
