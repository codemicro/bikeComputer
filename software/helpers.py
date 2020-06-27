from constants import *
from PIL import Image, ImageFont, ImageChops
from display import Drawing

def calculate_speed(time):
    """
    Calculate speed based on time in seconds for one wheel rotation

    :param time: float, number of seconds between wheel rotation
    :return: float, speed in MPH
    """
    return SPEED_WHEEL_CIRCUMFERENCE / (time / 60 / 60)


def grow_to_display_footprint(im: Image.Image, background=0):
    """
    The grows the image supplied to the resolution of the display

    :param im: image to grow
    :param background: colour to fill the background of the image with
    :return: new image
    """

    insert_w, insert_h = im.size

    position_w = int((DISPLAY_WIDTH - insert_w) / 2)
    position_h = int((DISPLAY_HEIGHT - insert_h) / 2)

    d = Drawing()
    d.draw.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=background)
    d.image.paste(im, (position_w, position_h))

    return d.image


def crop_whitespace(im):
    """
    Crops whitespace around a supplied image

    :param im: image to crop
    :return: cropped image
    """

    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    else:
        return im


def center_image(im:Image.Image) -> Image.Image:
    """
    Centers image in the middle of the screen

    :param im: Image.Image
    :return: Image.Image
    """

    return grow_to_display_footprint(crop_whitespace(im))


def add_text_to_image(im: Image.Image, text: str, font: ImageFont.ImageFont, text_fill: int = 255,
                      text_on_top: bool = True,
                      gap: int = 4):
    """
    Add text to an image

    :param im: image to add text too
    :param text: text to add to image
    :param font: font to use
    :param text_fill: colour of the text (0 to 255)
    :param text_on_top: if the text should be placed above the image
    :param gap: gap between image and text in pixels
    :return: image with text
    """

    text_img = Drawing()

    text_img.draw.text((0, 0), text, font=font, fill=text_fill)
    text_img.image = crop_whitespace(text_img.image)

    new_height = text_img.image.size[1] + gap + im.size[1]

    if text_img.image.size[0] > im.size[0]:
        new_width = text_img.image.size[0]
    else:
        new_width = im.size[0]

    final_drawing = Drawing(Image.new("1", (new_width, new_height)))

    # Determine image placement

    image_placement_x = int((new_width - im.size[0]) / 2)
    image_placement_y = 0

    if text_on_top:
        image_placement_y += gap + text_img.image.size[1]

    # Determine text placement

    text_placement_x = int((new_width - text_img.image.size[0]) / 2)
    text_placement_y = 0

    if not text_on_top:
        text_placement_y = im.size[1] + gap

    final_drawing.image.paste(im, (image_placement_x, image_placement_y))
    final_drawing.image.paste(text_img.image, (text_placement_x, text_placement_y))

    return final_drawing.image