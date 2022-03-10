def exercise_angles_checking(desired_angle, measured_angle):
    desired_angle = int(desired_angle)
    measured_angle = int(measured_angle)

    if desired_angle >= measured_angle - 10:
        if desired_angle <= measured_angle + 10:
            return True
        else:
            return False
    else:
        return False


def check_joint_first_position(joint_angle=0):
    print(joint_angle)
    return joint_angle
