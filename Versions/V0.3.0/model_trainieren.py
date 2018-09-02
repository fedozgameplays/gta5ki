import numpy as np
from alexnet import alexnet

width = 80
height = 60
learning_rate = 1E-3
epoch = 8
model_name = "car-{}-{}-{}-epochs.model".format(learning_rate, "alexnet", epoch)

model = alexnet(width, height, learning_rate)

trainingsdaten = np.load("trainierte_daten.npy")
train = trainingsdaten[:-500]
test = trainingsdaten[-500:]

x = np.array([i[0] for i in train]).reshape(-1, width, height, 1)
y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, width, height, 1)
test_y = [i[1] for i in test]

model.fit({"input": x}, {"targets": y}, n_epoch=epoch,
          validation_set=({"input": test_x}, {"targets": test_y}),
          snapshot_step=500, show_metric=True, run_id=model_name)

# tensorboard --logdir=foo:C:/Users/Kevin/Desktop/V0.2/log

model.save(model_name)

