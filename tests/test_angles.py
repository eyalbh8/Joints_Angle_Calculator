from main_window import calculate_angle

joints = {
    "shoulder": [0.31897982954978943, 0.2254987210035324],
    "elbow": [0.7195838689804077, 0.642013669013977],
    "wrist": [0.8107253313064575, 0.3998505771160126],
    "elbow_angle": 64.50900905642266
}


def test_angle_calculating():
    angle = calculate_angle(joints["shoulder"], joints["elbow"], joints["wrist"])

    assert angle == joints["elbow_angle"]