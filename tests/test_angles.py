import pytest
import numpy as np


def calculate_angle(first, mid, end):
    first = np.array(first)
    mid = np.array(mid)
    end = np.array(end)

    radians = np.arctan2(end[1] - mid[1], end[0] - mid[0]) - np.arctan2(first[1] - mid[1], first[0] - mid[0])
    angle = np.abs(radians * 180 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


joints = {
    "shoulder": [0.31897982954978943, 0.2254987210035324],
    "elbow": [0.7195838689804077, 0.642013669013977],
    "wrist": [0.8107253313064575, 0.3998505771160126],
    "elbow_angle": 64.50900905642266
}


def test_angle_calculating():
    angle = calculate_angle(joints["shoulder"], joints["elbow"], joints["wrist"])

    assert angle == joints["elbow_angle"]