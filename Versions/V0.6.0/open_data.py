import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import sys

dateiname = "trainingsdaten-{}.npy".format(sys.argv[1])
trainingsdaten = np.load(dateiname)
print(len(trainingsdaten))  

for daten in trainingsdaten:
    bild = daten[0]
    auswahl = daten[1]
    cv2.imshow("test", bild)
    print(auswahl)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
