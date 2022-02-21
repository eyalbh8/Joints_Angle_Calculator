# Web camera joints detection

## cv2 liabrary

Used to open the computer web camera, disaply the image and close the progarm when the user is finished

```
#press 'q' to close the window
if cv2.waitKey(10) == ord('q'):
    break
```
## Mediapipe & numpy

Used to detecet the necessary joints and calculate the angles
