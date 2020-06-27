from constants import *
from display import Display


class MasterClass:
    disp = Display(DISPLAY_I2C_ADDR, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    currentSpeed = 0


m = MasterClass()