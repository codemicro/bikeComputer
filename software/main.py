import sys
import time

import signal
from PIL import Image, ImageFont, ImageChops

import helpers
from constants import *
from display import Display, Drawing


class MasterClass:
    disp = Display(DISPLAY_I2C_ADDR, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    currentSpeed = 0


m = MasterClass()

disp = Display(0x3c, DISPLAY_WIDTH, DISPLAY_HEIGHT)


def sigint_handler(_=None, __=None):
    print("Attempting gracefully shutting down...")
    disp.clear()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

# font = ImageFont.truetype(ASSET_UBUNTU_MONO, 15)
#
# image = Drawing(disp)
# image.draw.rectangle((0,0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=255)
# image.draw.text((2, 2), "Hello world!",  font=font, fill=0)
# image.show()
#
# time.sleep(2)


font_lg = ImageFont.truetype(ASSET_UBUNTU_MONO, 15)
font_sm = ImageFont.truetype(ASSET_UBUNTU_MONO, 10)

im1 = helpers.add_text_to_image(Image.open("../assets/loading_1.png").convert("1"), "Loading...", font_lg)
im2 = helpers.add_text_to_image(Image.open("../assets/loading_2.png").convert("1"), "Loading...", font_lg)

im1 = helpers.add_text_to_image(im1, "PiBike v" + VERSION, font_sm)
im2 = helpers.add_text_to_image(im2, "PiBike v" + VERSION, font_sm)

im1 = helpers.grow_to_display_footprint(im1, background=0)
im2 = helpers.grow_to_display_footprint(im2, background=0)


while True:
    disp.show_image(im1)
    time.sleep(0.3)
    disp.show_image(im2)
    time.sleep(0.3)


# This will be useful later on
# while True:
#     draw.rectangle((0,0,DISPLAY_WIDTH,DISPLAY_HEIGHT), outline=0, fill=0)
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
