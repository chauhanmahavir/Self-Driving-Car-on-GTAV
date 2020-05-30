from modified_alexnet import alexnet3
import numpy as np

# Define Height Width of frame which is taken in dataset
WIDTH = 200
HEIGHT = 150
LR = 1e-3
EPOCHS = 50
MODEL_NAME = 'self_driving_car_gta5.model'

# Load Neural Network
model = alexnet3(WIDTH, HEIGHT, 0.001)

# replace location of Final Train Data
train_data = np.load('final_data_flip.npy')

# Try to take 10-15% percent of your data in test
train = train_data[:-300]
test = train_data[-300:]

# seperate feature and labels for training and testing
X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_y = [i[1] for i in test]

# Train Model
model.fit({'input': X}, {'targets': Y}, n_epoch = EPOCHS, validation_set=( {'input': test_x}, {'targets': test_y} ), snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# Save Model
model.save(MODEL_NAME)
