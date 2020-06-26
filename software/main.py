from display import Display, Drawing

import time
import math
import gpiozero
from PIL import ImageFont

wheel_circ = (math.pi * 26) / 63360
last_active = None
b = gpiozero.Button(22)
def calculate_speed(time):
    return wheel_circ / (time / 60 / 60)

disp = Display(0x3c)

width = disp.width
height = disp.height

image = Drawing()

image.draw.rectangle((0,0,width,height), outline=0, fill=0)

font = ImageFont.truetype("umono.ttf", 15)

image.draw.text((2, 2), "Hello world!",  font=font, fill=255)

disp.show_image(image)

time.sleep(2)

disp.clear()

# while True:
#     draw.rectangle((0,0,width,height), outline=0, fill=0)
#
#     if b.wait_for_press(timeout=5):
#         if last_active is None:
#             last_active = time.time()
#             draw.text((2, 2), "Speed: 0",  font=font, fill=255)
#         else:
#             speed = calculate_speed(time.time() - last_active)
#             last_active = time.time()
#             draw.text((2, 2), "Speed: " + str(int(speed)),  font=font, fill=255)
#     else:
#             draw.text((2, 2), "Speed: 0",  font=font, fill=255)
#
#     disp.image(image)
#     disp.display()
#     b.wait_for_release()
