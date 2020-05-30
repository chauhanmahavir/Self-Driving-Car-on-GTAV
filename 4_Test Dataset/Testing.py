import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from modified_alexnet import alexnet3
from getkeys import key_check
import time

# Define Height Width of frame which is taken in dataset
WIDTH = 200
HEIGHT = 150
LR = 1e-3
MODEL_NAME = 'self_driving_car_gta5.model'
t_time = 0.09

# Go Straight
def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

# Turn left
def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)

# Turn Right
def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)

# Load Neural Network
model = alexnet3(WIDTH, HEIGHT, LR)

# Load Model
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # Grab Screen of your top left corner of 800 X 600 resolution
            screen = grab_screen(region=(0,0,800,600))
            
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()

            # Convert frame into Gray Scale
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

            # Resize Frame into 200 X 150
            screen = cv2.resize(screen, (200,150))

            # Predict Movement using trained model
            prediction = model.predict([screen.reshape(200,150,1)])[0]
            print(prediction)

            # Set threshold for turn
            turn_thresh = .75
            fwd_thresh = 0.70

            if prediction[1] > fwd_thresh:
                straight()
            elif prediction[0] > turn_thresh:
                left()
            elif prediction[2] > turn_thresh:
                right()
            else:
                straight()

        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

if __name__ == "__main__":
    main()
