import numpy as np
import os
#from models import inception_v3 as googlenet
from alexnet import alexnet
from random import shuffle



def run(width, height, learning_rate, epochs):

    batchsize = 32
    Dateiende = 18
    
    for i in range(1,10):
        check_model = "car-{}-{}-{}.model".format(str(i),str(learning_rate),str(epochs))
        if os.path.isfile(check_model):
            print("Model existiert bereits: "+str(check_model))
        else:
            model_name = "car-{}-{}-{}.model".format(str(i),str(learning_rate),str(epochs))
            return model_name

    nn_width = int(width)/2
    nn_height = int(height)/2
    
    model = alexnet(int(nn_width), int(nn_height), float(learning_rate))

    for e in range(int(epochs)):
        daten_rf = [i for i in range(1,Dateiende+1)]
        shuffle(daten_rf)

        for count, i in enumerate(daten_rf):
            try:
                dateiname = "trainingsdaten-{}.npy".format(i)
                trainingsdaten = np.load(dateiname)
                print("Daten werden geladen: %s, Länge: %s" % (dateiname,str(len(trainingsdaten))))

                train = trainingsdaten[:-50]
                test = trainingsdaten[-50:]
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
        model.save(model_name)
        

