# Create Dataset

## In this section first we create dataset as below steps

* First we grab screen

* Convert That Frame into Gray Scale because gray scale have only 1 channel so we can reduce size of the image and also it is good for train data

* And then we resize our frame into 200 X 150 so we can reduce much size.

* And then we take key which is pressed at that frame. For key i take one list which contain keys like [A, W, D]. here A stand for left move, W stand for Forward move and D stand for Right move.

* Now Combine both frame and key into list and append it into one list.

* Here i am taking 1000 frame and key in one .npy file because of low RAM you can take more but i will take much time while saving file.

* This data is unorganized manner so we have to preprocess our data.
