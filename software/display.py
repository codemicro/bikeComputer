import threading

import adafruit_ssd1306
import board
from PIL import Image
from PIL import ImageDraw
from constants import *


"""
Classes and functions related to display drawing/generation
"""

class Display:
    lock = threading.Lock()

    def __init__(self, i2c_addr, disp_width, disp_height):
        self.width = disp_width
        self.height = disp_height

        self.disp = adafruit_ssd1306.SSD1306_I2C(disp_width, disp_height, board.I2C(), addr=i2c_addr)
        self.disp.fill(0)
        self.disp.show()

    def clear(self, inverted=False):
        if inverted:
            self.show_image(UI_INVERTED_BLANK_IMAGE)
        else:
            self.show_image(UI_BLANK_IMAGE)

    def show_image(self, im):
        self.lock.acquire()
        self.disp.image(im)
        self.disp.show()
        self.lock.release()

    def show_drawing(self, drawing):
        self.show_image(drawing.image)


class Drawing:
    def __init__(self, im=None):
        if im is None:
            self.image = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
        else:
            self.image = im
        self.draw = ImageDraw.Draw(self.image)
