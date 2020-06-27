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

    # Main UI

    d = Drawing(UI_RIGHT_SIDE_LIT)

    text_drawing = Drawing()
    text_drawing.draw.text((0, 0), "16.9", font=ASSET_UBUNTU_MONO_XL, fill=255)  # Speed
    text_drawing.image = helpers.crop_whitespace(text_drawing.image)
    text_drawing.image = helpers.add_text_to_image(text_drawing.image, "mph", ASSET_UBUNTU_MONO_ME, text_on_top=False)  # Label

    text_x_size, text_y_size = text_drawing.image.size
    text_x_pos = int(0.25 * DISPLAY_WIDTH) - int(0.5 * text_x_size)
    text_y_pos = int(0.5 * (DISPLAY_HEIGHT - text_y_size))

    text_drawing.image.save("thing.png")

    d.image.paste(text_drawing.image, box=(text_x_pos, text_y_pos))

    m.disp.show_drawing(d)