import numpy as np
import cv2
import time
from bild_erfassen import grab_screen
from tasten_erfassen import key_check
from inception_v3 import inception3
from bewegungen import geradeaus, links, rechts, zurücksetzen, geradeaus_links, geradeaus_rechts, zurücksetzen_links, zurücksetzen_rechts, nichts


def run(learning_rate, epochs, model_id):
    # Breite des Neural Networks
    nn_width = 480
    # Höhe des Neural Networks
    nn_height = 270
    # Größe des Outputs (Standart: 9)
    output_size = 9
    # Modelname mit ID, Lernrate und Epochen
    model_name = "model{}-{}_lr-{}_epochs.model".format(str(model_id), float(learning_rate), str(epochs))
    # Inception Model erstellen
    model = inception3(int(nn_width), int(nn_height), float(learning_rate), output=int(output_size))
    # Laden des trainierten Models
    model.load(model_name)

    for i in list(range(6))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False

    while True:
        if not paused:
            bild = grab_screen()
            bild = cv2.cvtColor(bild, cv2.COLOR_BGR2RGB)
            bild = cv2.resize(bild, (int(nn_width), int(nn_height)))
            cv2.imshow("test", bild)
            time.sleep(0.09)

            vorhersage = model.predict([bild.reshape(int(nn_width), int(nn_height), 3)])[0]
            vorhersage = np.array(vorhersage)  # * np.array([0.3, 0.9, 4, 4, 1.5, 1.5, 0.5, 0.5, 0.7])
            auswahl = np.argmax(vorhersage)

            if auswahl == 0:
                geradeaus()
                auswahl_getroffen = "Geradeaus, mit {}% Sicherheit".format(float(vorhersage[0]) * 100)
            elif auswahl == 1:
                zurücksetzen()
                auswahl_getroffen = "Zurücksetzen, mit {}% Sicherheit".format(float(vorhersage[1]) * 100)
            elif auswahl == 2:
                links()
                auswahl_getroffen = "Links, mit {}% Sicherheit".format(float(vorhersage[2]) * 100)
            elif auswahl == 3:
                rechts()
                auswahl_getroffen = "Rechts, mit {}% Sicherheit".format(float(vorhersage[3]) * 100)
            elif auswahl == 4:
                geradeaus_links()
                auswahl_getroffen = "Geradeaus + Links, mit {}% Sicherheit".format(float(vorhersage[4]) * 100)
            elif auswahl == 5:
                geradeaus_rechts()
                auswahl_getroffen = "Geradeaus + Rechts, mit {}% Sicherheit".format(float(vorhersage[5]) * 100)
            elif auswahl == 6:
                zurücksetzen_links()
                auswahl_getroffen = "Zurücksetzen + Links, mit {}% Sicherheit".format(float(vorhersage[6]) * 100)
            elif auswahl == 7:
                zurücksetzen_rechts()
                auswahl_getroffen = "Zurücksetzen + Rechts, mit {}% Sicherheit".format(float(vorhersage[7]) * 100)
            elif auswahl == 8:
                nichts()
                auswahl_getroffen = "Keine Aktion, mit {}% Sicherheit".format(float(vorhersage[8]) * 100)

            print(auswahl_getroffen)

            if cv2.waitKey(15) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

        keys = key_check()

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                nichts()
                time.sleep(1)
