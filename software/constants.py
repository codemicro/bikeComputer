import json
import math

from PIL import Image, ImageDraw, ImageChops, ImageFont

with open("../settings.json") as f:
    loaded_settings = json.load(f)


class RequiredSettingNotFoundException(Exception):
    def __init__(self, param):
        self.msg = param

    def __str__(self):
        return "Required setting " + ">".join(self.msg) + " not found in the settings file."


def required_option(path):
    """
    Raises if path cannot be resolved using resolve_path

    :param path: list, path to search for
    :return: value from loaded_settings
    """

    try:
        return resolve_path(path, loaded_settings)
    except LookupError:
        raise RequiredSettingNotFoundException(path)


def pick_default(path, default):
    """
    Determines if a default should be used depending on if the specified path can be found in the loaded_settings object

    :param path: path to search
    :param default: default value
    :return: chosen value (default or loaded from specified path)
    """

    try:
        return resolve_path(path, loaded_settings)
    except LookupError:
        return default


def resolve_path(path: list, obj):
    """
    Recursively get value of specified path in array/dict

    :param path: list of JSON arguments, for example j["thing"][1]["hello"] would be ["thing", 1, "hello"]
    :param obj: array/dict to read from
    :return: none if not found otherwise value
    :raises: ValueError if the path is not found
    """
    if len(path) == 0:
        return obj
    else:
        return resolve_path(path[1:], obj[path[0]])


VERSION = "0.0.0"

# Constants for asset paths
ASSET_UBUNTU_MONO_PATH = "../assets/UbuntuMono.ttf"
ASSET_UBUNTU_MONO_SM = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 10)
ASSET_UBUNTU_MONO_ME = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 15)
ASSET_UBUNTU_MONO_LG = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 20)
ASSET_UBUNTU_MONO_XL = ImageFont.truetype(ASSET_UBUNTU_MONO_PATH, 25)

# Constants for display information
DISPLAY_HEIGHT = pick_default(["display", "height"], 128)
DISPLAY_I2C_ADDR = pick_default(["display", "i2cAddr"], 0x3c)
DISPLAY_WIDTH = pick_default(["display", "width"], 64)

# Constants for device pins and hardware
PIN_REED_SWITCH = pick_default(["pins", "reedSwitch"], 22)

# Constants for calculating speed
SPEED_WHEEL_DIAMETER = required_option(["wheelDiameter"])  # Inches
SPEED_WHEEL_CIRCUMFERENCE = (math.pi * SPEED_WHEEL_DIAMETER) / 63360  # In miles so result is miles per hour
SPEED_REED_TIMEOUT = pick_default(["speed", "timeout"], 4)  # Number of seconds to wait before declaring the speed to be
# zero

# Constants for UI prefabs
UI_BLANK_IMAGE = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
ImageDraw.Draw(UI_BLANK_IMAGE).rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=255)

UI_INVERTED_BLANK_IMAGE = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
ImageDraw.Draw(UI_BLANK_IMAGE).rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=0)

UI_SPLIT_DISPLAY = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))  # Right side of the image on
ImageDraw.Draw(UI_SPLIT_DISPLAY).rectangle((int(0.5 * DISPLAY_WIDTH), 0, int(0.5 * DISPLAY_WIDTH), DISPLAY_HEIGHT),
                                           fill=255, outline=255)