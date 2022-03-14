# Web camera joints detection
# User manual

1) Choose exercise from the option menu or define what joints and each joint angle you want the program to detecte
2) Set the number of sets you want to perform for the exercise
3) Stand two meters away from the web camera
4) Press the "Start" button
5) Wait a few seconds for the program to identtify you
6) Strat the exercise!
7) The exercise is finished when the program close itself and a gif window is created

#### Optional
1) Press the "Add new exercise"
2) Define the name of the exrcise
3) Define the joints and each joint necessary angle
4) Press "Finish" 
5) Exit the program

## cv2 liabrary

Used to open the computer web camera, disaply the image and close the progarm when the user is finished

```
#press 'q' to close the window
if cv2.waitKey(10) == ord('q'):
    break
```
## Mediapipe & numpy

Used to measure the necessary joints and decodes the quality of the exercise performance 

![image](https://user-images.githubusercontent.com/87011531/155020288-654970d3-5e5b-4099-8000-dd73d04e81dc.png)

## tKinter

Display's the main window to choose the necesary exercise and the window to add exercise to the JSON data base

Main window:


![image](https://user-images.githubusercontent.com/87011531/158135423-0d3068d0-6997-421d-9162-d7d85338752a.png)


Add exercise to db window:

![image](https://user-images.githubusercontent.com/87011531/158135677-350ed3ff-0adc-4f55-8d09-a0988de3908b.png)


Gif to confirm the success at the exercise (random gif each time):


![image](https://user-images.githubusercontent.com/87011531/158136109-f48921e4-a991-4542-b372-a3b79ff404ae.png)
