import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

trainingsdaten = np.load("trainingsdaten.npy")
print(len(trainingsdaten))
df = pd.DataFrame(trainingsdaten)
#print(df.head)
#print(Counter(df[1].apply(str)))

links = []
rechts = []
geradeaus = []
nichts = []

shuffle(trainingsdaten)
i=0
for daten in trainingsdaten:
    bild = daten[0]
    auswahl = daten[1]

    if auswahl == ['1', 0, 0]:
        links.append([bild, auswahl])
    elif auswahl == [0, '1', 0]:
        geradeaus.append([bild, auswahl])
    elif auswahl == [0, 0, '1']:
        rechts.append([bild, auswahl])
    else:
        i=i+1
        print("Kein Tastenanschlag, "+str(i))
        pass

geradeaus = geradeaus[:len(links)][:len(rechts)]
links = links[:len(geradeaus)]
rechts = rechts[:len(geradeaus)]

trainierte_daten = geradeaus + links + rechts
shuffle(trainierte_daten)
print(len(trainierte_daten))
np.save("trainierte_daten.npy", trainierte_daten)
    

##for daten in trainingsdaten:
##    bild = daten[0]
##    auswahl = daten[1]
##    cv2.imshow("test", bild)
##    print(auswahl)
##    if cv2.waitKey(25) & 0xFF == ord("q"):
##        cv2.destroyAllWindows()
##        break
