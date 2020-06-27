import json
import math

from PIL import Image, ImageDraw, ImageChops, ImageFont

with open("../settings.json") as f:
    loaded_settings = json.load(f)

VERSION = "0.0.0"

# Constants for asset paths
ASSET_UBUNTU_MONO_PATH = "../assets/UbuntuMono.ttf"
ASSET_UBUNTU_MONO_SM = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 10)
ASSET_UBUNTU_MONO_ME = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 15)
ASSET_UBUNTU_MONO_LG = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 20)
ASSET_UBUNTU_MONO_XL = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 25)

# Constants for display information
DISPLAY_HEIGHT = loaded_settings["display"]["height"]
DISPLAY_I2C_ADDR = loaded_settings["display"]["i2cAddr"]
DISPLAY_WIDTH = loaded_settings["display"]["width"]

# Constants for calculating speed
SPEED_WHEEL_DIAMETER = loaded_settings["wheelDiameter"]  # Inches
SPEED_WHEEL_CIRCUMFERENCE = (math.pi * SPEED_WHEEL_DIAMETER) / 63360  # In miles so result is miles per hour

# Constants for UI prefabs
UI_BLANK_IMAGE = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
ImageDraw.Draw(UI_BLANK_IMAGE).rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=255)

UI_INVERTED_BLANK_IMAGE = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
ImageDraw.Draw(UI_BLANK_IMAGE).rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=0)

UI_RIGHT_SIDE_LIT = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))  # Right side of the image on
ImageDraw.Draw(UI_RIGHT_SIDE_LIT).rectangle((int(0.5 * DISPLAY_WIDTH), 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), fill=255,
                                         outline=255)