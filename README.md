# Web camera joints detection

## cv2 liabrary

Used to open the computer web camera and close the progarm when the user is finished

```
if cv2.waitKey(10) == ord('q'):
    break
```
## Mediapipe & numpy

Used to detecet the necessary joints and calculate the angles
