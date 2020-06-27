from constants import *
from display import Display
import gpiozero


class MasterClass:
    disp = Display(DISPLAY_I2C_ADDR, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    currentSpeed = "0.00"
    ready = False

    reedSwitch = gpiozero.Button(PIN_REED_SWITCH)


m = MasterClass()