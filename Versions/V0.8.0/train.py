import numpy as np
import h5py
from inception_v3 import inception3
from sklearn.model_selection import train_test_split
import gc


def run(learning_rate, epochs, dateiende, load):
    # Batch-size des Neural Networks (Standart: 32)
    batchsize = 64
    # ID vom Model, für mehrere ändern
    model_id = 1
    # Größe des Outputs (Standart: 9)
    output_size = 9
    # Modelname mit ID, Lernrate und Epochen
    model_name = "model{}-{}_lr-{}_epochs.model".format(str(model_id), float(learning_rate), str(epochs))
    # Breite des Neural Networks
    nn_width = 480
    # Höhe des Neural Networks
    nn_height = 270
    # Inception Model erstellen
    model = inception3(int(nn_width), int(nn_height), float(learning_rate), output=int(output_size))
    # Vorherige Model-Datei laden
    # load = True

    if load is True:
        model.load(model_name)

    for e in range(int(epochs)):
        daten_rf = [i for i in range(1, int(dateiende)+1)]
        for count, i in enumerate(daten_rf):
            try:
                dateiname = "trainingsdaten/trainingsdaten-{}.h5".format(i)
                with h5py.File(dateiname, "r") as trainingsdaten:
                    x_daten = trainingsdaten["bild"][:]
                    y_daten = trainingsdaten["steuerung"][:]
                trainingsdaten.flush
                trainingsdaten.close
                x_daten = np.array(x_daten)
                x_daten = x_daten.swapaxes(1, 2)
                print(x_daten.shape, y_daten.shape)
                y_daten = np.array(y_daten)
                x_train, x_test, y_train, y_test = train_test_split(x_daten, y_daten, test_size=0.3)
                print("X_train:"+str(x_train.shape))
                print("x_test:"+str(x_test.shape))
                print("y_train:"+str(y_train.shape))
                print("y_test:"+str(y_test.shape))

                model.fit({"input": x_train}, {"targets": y_train}, n_epoch=1,
                          validation_set=({"input": x_test}, {"targets": y_test}),
                          snapshot_step=2500, show_metric=True, run_id=model_name, batch_size=batchsize)

                if count % 2 == 0:
                    print("Model wird gespeichert...")
                    model.save(model_name)

                del x_daten, y_daten, x_train, x_test, y_train, y_test, trainingsdaten
                gc.collect()

            except Exception as e:
                print(e.message, e.args)

        model.save(model_name)
