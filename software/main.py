import time

from PIL import Image, ImageFont, ImageChops

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


def grow_to_display_footprint(im:Image.Image, background=0):
    insert_w, insert_h = im.size

    position_w = int((DISPLAY_WIDTH - insert_w) / 2)
    position_h = int((DISPLAY_HEIGHT - insert_h) / 2)

    d = Drawing(disp)
    d.draw.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=background)
    d.image.paste(im, (position_w, position_h))

    return d.image


def crop_whitespace(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


def add_text_to_image(im, text, font, text_fill=255, text_on_top=True, gap=4):
    text_img = Drawing(disp)

    text_img.draw.text((0, 0), text, font=font, fill=text_fill)
    text_img.image = crop_whitespace(text_img.image)

    new_height = text_img.image.size[1] + gap + im.size[1]

    if text_img.image.size[0] > im.size[0]:
        new_width = text_img.image.size[0]
    else:
        new_width = im.size[0]

    final_drawing = Drawing(disp, Image.new("1", (new_width, new_height)))

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


font_lg = ImageFont.truetype(ASSET_UBUNTU_MONO, 15)
font_sm = ImageFont.truetype(ASSET_UBUNTU_MONO, 10)

im1 = add_text_to_image(Image.open("../assets/loading_alt_1.png").convert("1"), "Loading...", font_lg)
im2 = add_text_to_image(Image.open("../assets/loading_alt_2.png").convert("1"), "Loading...", font_lg)

im1 = add_text_to_image(im1, "PiBike v" + VERSION, font_sm)
im2 = add_text_to_image(im2, "PiBike v" + VERSION, font_sm)

im1 = grow_to_display_footprint(im1, background=0)
im2 = grow_to_display_footprint(im2, background=0)


while True:
    disp.show_image(im1)
    time.sleep(0.5)
    disp.show_image(im2)
    time.sleep(0.5)


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
