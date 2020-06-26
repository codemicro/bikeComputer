from PIL import Image
from PIL import ImageDraw
import adafruit_ssd1306
import board

class Display:
    def __init__(self, i2c_addr, disp_width=128, disp_height=64):
        self.width = disp_width
        self.height = disp_height

        self.disp = adafruit_ssd1306.SSD1306_I2C(disp_width, disp_height, board.I2C(), addr=i2c_addr)
        self.disp.fill(0)
        self.disp.show()

    def clear(self):
        d = Drawing()
        d.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.show_image(d)

    def show_image(self, drawing):
        self.disp.image(drawing.image)
        self.disp.show()


class Drawing:
    def __init__(self, width=128, height=64):
        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)
