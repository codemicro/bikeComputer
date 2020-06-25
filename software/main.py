import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
import math
import gpiozero
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

wheel_circ = (math.pi * 26) / 63360
last_active = None
b = gpiozero.Button(22)
def calculate_speed(time):
    return wheel_circ / (time / 60 / 60)

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.load_default()


while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    if b.wait_for_press(timeout=5):
        if last_active is None:
            last_active = time.time()
            draw.text((2, 2), "Speed: 0",  font=font, fill=255)
        else:
            speed = calculate_speed(time.time() - last_active)
            last_active = time.time()
            draw.text((2, 2), "Speed: " + str(int(speed)),  font=font, fill=255)
    else:
            draw.text((2, 2), "Speed: 0",  font=font, fill=255)
    
    disp.image(image)
    disp.display()
    b.wait_for_release()
