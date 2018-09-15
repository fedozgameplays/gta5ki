import numpy as np
import os
from inception_v3 import inception3
from random import shuffle



def run(width, height, learning_rate, epochs):

    # Batch-size von Neural Network
    batchsize = 64
    # Menge der Trainingsdaten
    Dateiende = 16
    # ID vom Model, für mehrere ändern
    model_id = 1
    # Größe des Outputs
    output_size = 9
    # Modelname mit ID, Lernrate und Epochen
    model_name = "model{}-{}_lr-{}_epochs".format(str(model_id),float(learning_rate), str(epochs))

    # Breite von Neural Network
    nn_width = int(width)/2
    # Höhe von Neural Network
    nn_height = int(height)/2
    
    model = inception3(int(nn_width), int(nn_height), float(learning_rate), output=int(output_size))

    for e in range(int(epochs)):
        # Reihenfolge der Trainingsdaten
        daten_rf = [i for i in range(1,Dateiende+1)]
        # Reihenfolge ändern
        #shuffle(daten_rf)

        for count, i in enumerate(daten_rf):
            try:
                # Dateiname Trainingsdaten ändern
                dateiname = "trainingsdaten-{}.npy".format(i)
                # Trainingsdaten laden
                trainingsdaten = np.load(dateiname)
                print("Daten werden geladen: %s, Länge: %s" % (dateiname,str(len(trainingsdaten))))

                # Trainingsdaten teilen in train und test Daten
                train = trainingsdaten[:-500]
                test = trainingsdaten[-500:]
                print("Länge train: %s" % (len(train)))
                print("Länge test: %s" % (len(test)))

                x = np.array([i[0] for i in train])
                x = x.reshape(-1, int(nn_width), int(nn_height), 3)
                y = [i[1] for i in train]
                test_x = np.array([i[0] for i in test])
                test_x = test_x.reshape(-1, int(nn_width), int(nn_height), 3)
                test_y = [i[1] for i in test]

                model.fit({"input": x}, {"targets": y}, n_epoch=1,
                          validation_set=({"input": test_x}, {"targets": test_y}),
                          snapshot_step=2500, show_metric=True, run_id=model_name, batch_size=batchsize)

                if count%10 == 0:
                    print("Model wird gespeichert...")
                    model.save(model_name)

            except Exception as e:
                print(str(e))

        # Model speichern
        model.save(model_name)
        

