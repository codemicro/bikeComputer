import time

from PIL import ImageFont, Image
from constants import *
import helpers
from masterclass import m


def loading_animation():
    """
    Displays a loading animation
    """

    font_lg = ImageFont.truetype(ASSET_UBUNTU_MONO, 15)
    font_sm = ImageFont.truetype(ASSET_UBUNTU_MONO, 10)

    im1 = helpers.add_text_to_image(Image.open("../assets/loading_1.png").convert("1"), "Loading...", font_lg)
    im2 = helpers.add_text_to_image(Image.open("../assets/loading_2.png").convert("1"), "Loading...", font_lg)

    im1 = helpers.add_text_to_image(im1, "PiBike v" + VERSION, font_sm)
    im2 = helpers.add_text_to_image(im2, "PiBike v" + VERSION, font_sm)

    im1 = helpers.grow_to_display_footprint(im1, background=0)
    im2 = helpers.grow_to_display_footprint(im2, background=0)

    while True:
        m.disp.show_image(im1)
        time.sleep(0.3)
        m.disp.show_image(im2)
        time.sleep(0.3)