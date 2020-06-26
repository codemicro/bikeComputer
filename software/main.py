import time

from PIL import Image

from constants import *
from display import Display, Drawing


class MasterClass:
    disp = Display(DISPLAY_I2C_ADDR, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    currentSpeed = 0


m = MasterClass()

disp = Display(0x3c, DISPLAY_WIDTH, DISPLAY_HEIGHT)

# font = ImageFont.truetype(ASSET_UBUNTU_MONO, 15)
#
# image = Drawing(disp)
# image.draw.rectangle((0,0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=255)
# image.draw.text((2, 2), "Hello world!",  font=font, fill=0)
# image.show()
#
# time.sleep(2)


def grow_to_display_footprint(im:Image.Image):
    insert_w, insert_h = im.size

    position_w = int((DISPLAY_WIDTH - insert_w) / 2)
    position_h = int((DISPLAY_HEIGHT - insert_h) / 2)

    new_im = Image.new("1", (DISPLAY_WIDTH, DISPLAY_WIDTH))
    new_im.paste(im, (position_w, position_h))

    return new_im


im1 = grow_to_display_footprint(Image.open("../assets/loading_1.png").convert("1"))
im2 = grow_to_display_footprint(Image.open("../assets/loading_2.png").convert("1"))

while True:
    disp.show_image(im1)
    time.sleep(0.5)
    disp.clear()
    disp.show_image(im2)


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
