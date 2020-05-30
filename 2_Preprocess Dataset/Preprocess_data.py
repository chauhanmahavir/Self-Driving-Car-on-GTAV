import numpy as np
from random import shuffle
import cv2
import os

lefts = []
rights = []
forwards = []

# Replace with your dataset location
dataset_location = 'dataset/'

# take file name from dataset location
dataset_filename = os.listdir(dataset_location)

for i in dataset_filename:
    train_data = np.load(dataset_location + i)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == [1, 0, 0]:
            lefts.append([img, choice])
            rights.append([cv2.flip(img, 0), [0, 0, 1]])
        elif choice == [0, 1, 0]:
            forwards.append([img, choice])
        elif choice == [0, 0, 1]:
            rights.append([img, choice])
            lefts.append([cv2.flip(img, 0), [1, 0, 0]])

forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
    
final_data = forwards + lefts + rights
shuffle(final_data)

np.save('final_training_data.npy', final_data)
