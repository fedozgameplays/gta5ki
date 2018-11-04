import h5py
import cv2
import numpy as np

dateiname = "trainingsdaten/trainingsdaten-8.h5"
trainingsdaten = h5py.File(dateiname, "r")
bilder = trainingsdaten["bild"][:]
bilder = np.array(bilder)
print(bilder.shape)
bilder = bilder.swapaxes(1, 2)
print(bilder.shape)
steuerung = trainingsdaten["steuerung"][:]
i = 0
steuerung = np.array(steuerung).tolist()

for bild in bilder:
    print(steuerung[i])
    # bild = bild.reshape(480, 270, 3)
    cv2.imshow("test", bild)
    i = int(i) + 1

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
