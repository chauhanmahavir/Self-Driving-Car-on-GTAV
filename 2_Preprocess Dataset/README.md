# Preprocess Dataset

## in this section we preprocess dataset which is created earlier:

* First we read all file which is created earlier.

* And then we classify data into 3 manner left move, right move and forward move.

* here our data contain very few left and right move so if we get left move then we append this field into left move and then we flip our image vertically and the we append that flipped image into right move with that movement list so we can increase our left and right move.

* Left Movement Image as below

![alt text](https://github.com/chauhanmahavir/Self-Driving-Car-on-GTAV/blob/master/2_Preprocess%20Dataset/Left.jpg)

* Flipped Image of above

![alt text](https://github.com/chauhanmahavir/Self-Driving-Car-on-GTAV/blob/master/2_Preprocess%20Dataset/Right.jpg)

* After that we balance our data 
```bash
forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
```
Above code will trim all list with minimum list of them.

* After balancing we combine all list and shuffe final list for training and save it into new file.
