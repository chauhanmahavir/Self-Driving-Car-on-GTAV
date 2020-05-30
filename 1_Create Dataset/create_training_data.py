import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
    [A,W,D] boolean values.
    '''
    output = [0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output



i=0
training_data=[]

def new():
    global i
    file_name = 'dataset/'+str(i)+'_training_data.npy'
    i=i+1
    return file_name


def main():
    x=0

    for i in list(range(10))[::-1]:
        print("Dataset is creating in",i+1, "Second")
        time.sleep(1)
    last_time = time.time()

    while True:
        global trainin_data
        
        # Grab Screen of your top left corner of 800 X 600 resolution
        screen = grab_screen(region=(0,0,800,600))

        # Convert frame into Gray Scale
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # Resize Frame into 200 X 150
        screen = cv2.resize(screen,(200,150))

        # Check Which key is pressed at that frame
        keys = key_check()
        output = keys_to_output(keys)

        # Append Frame and key into list
        training_data.append([screen, output])
        
        print(len(training_data),'Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        
        if len(training_data)%1000 ==0:
            
            # Create New file and save 1000 frame into .npy file
            np.save(new(), training_data)
            print(x,"SAVED")
            x = x + 1
            training_data.clear()

if __name__ == "__main__":
    main()
