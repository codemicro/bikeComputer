import constants


def calculate_speed(time):
    """
    Calculate speed based on time in seconds for one wheel rotation
    :param time: float, number of seconds between wheel rotation
    :return: float, speed in MPH
    """
    return constants.SPEED_WHEEL_CIRCUMFERENCE / (time / 60 / 60)