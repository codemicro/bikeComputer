import adafruit_ssd1306
import board
from PIL import Image
from PIL import ImageDraw


"""
Classes and functions related to display drawing/generation
"""

class Display:
    def __init__(self, i2c_addr, disp_width, disp_height):
        self.width = disp_width
        self.height = disp_height

        self.disp = adafruit_ssd1306.SSD1306_I2C(disp_width, disp_height, board.I2C(), addr=i2c_addr)
        self.disp.fill(0)
        self.disp.show()

    def clear(self):
        d = Drawing(self)
        d.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.show_drawing(d)

    def show_image(self, im):
        self.disp.image(im)
        self.disp.show()

    def show_drawing(self, drawing):
        self.show_image(drawing.image)


class Drawing:
    def __init__(self, display):
        self.display = display
        self.image = Image.new("1", (display.width, display.height))
        self.draw = ImageDraw.Draw(self.image)

    def show(self):
        self.display.show_image(self)
