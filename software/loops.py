import time

from PIL import ImageFont, Image
from constants import *
import helpers
from display import Drawing
from masterclass import m


def loading_animation():
    """
    Displays a loading animation
    """

    im1 = helpers.add_text_to_image(Image.open("../assets/loading_1.png").convert("1"), "Loading...",
                                    ASSET_UBUNTU_MONO_ME)
    im2 = helpers.add_text_to_image(Image.open("../assets/loading_2.png").convert("1"), "Loading...",
                                    ASSET_UBUNTU_MONO_ME)

    im1 = helpers.add_text_to_image(im1, "PiBike v" + VERSION, ASSET_UBUNTU_MONO_SM)
    im2 = helpers.add_text_to_image(im2, "PiBike v" + VERSION, ASSET_UBUNTU_MONO_SM)

    im1 = helpers.grow_to_display_footprint(im1, background=0)
    im2 = helpers.grow_to_display_footprint(im2, background=0)

    while not m.ready:
        m.disp.show_image(im1)
        time.sleep(0.3)
        m.disp.show_image(im2)
        time.sleep(0.3)


def display_loop():
    loading_animation()

    d = Drawing()
    d.draw.text((0, 0), "Ready!", font=ASSET_UBUNTU_MONO_LG, fill=255)

    d.image = helpers.center_image(d.image)

    m.disp.show_drawing(d)