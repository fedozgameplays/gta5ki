import numpy as np
from alexnet import alexnet


def run(width, height, learning_rate, epochs, dateiname): 
    model_name = "car-{}-{}-{}-epochs.model".format(float(learning_rate), "alexnet", int(epochs))
    model = alexnet(int(width), int(height), float(learning_rate))

    trainingsdaten = np.load(dateiname)
    train = trainingsdaten[:-500]
    test = trainingsdaten[-500:]

    x = np.array([i[0] for i in train]).reshape(-1, int(width), int(height), 1)
    y = [i[1] for i in train]
    test_x = np.array([i[0] for i in test]).reshape(-1, int(width), int(height), 1)
    test_y = [i[1] for i in test]

    model.fit({"input": x}, {"targets": y}, n_epoch=int(epochs),
              validation_set=({"input": test_x}, {"targets": test_y}),
              snapshot_step=500, show_metric=True, run_id=model_name)

    model.save(model_name)

