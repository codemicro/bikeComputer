import json
import math

with open("../settings.json") as f:
    loaded_settings = json.load(f)

VERSION = "0.0.0"

# Constants for assets
ASSET_UBUNTU_MONO = "../assets/UbuntuMono.ttf"

# Constants for display information
DISPLAY_HEIGHT = loaded_settings["display"]["height"]
DISPLAY_I2C_ADDR = loaded_settings["display"]["i2cAddr"]
DISPLAY_WIDTH = loaded_settings["display"]["width"]

# Constants for calculating speed
SPEED_WHEEL_DIAMETER = loaded_settings["wheelDiameter"]  # Inches
SPEED_WHEEL_CIRCUMFERENCE = (math.pi * SPEED_WHEEL_DIAMETER) / 63360  # In miles so result is miles per hour
