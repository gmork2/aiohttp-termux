#!/usr/bin/env python
import argparse
import json
import sys
from typing import Union

# termux-brightness -h
# Usage: termux-brightness brightness
# Set the screen brightness between 0 and 255 or auto

USAGE = """termux-brightness"""
DATA = ""

ERROR = {
  "error": "Please grant the following permission to use this command: android.permission.WRITE_SETTINGS"
}


def check_brightness(value: Union[int, str]) -> Union[int, str]:
    try:
        brightness = int(value)
    except ValueError:
        brightness = value

    if brightness != 'auto' and (brightness < 0 or brightness > 255):
        raise argparse.ArgumentTypeError(f"Invalid brightness value ({brightness})")
    return brightness


if __name__ == "__main__":
    parser = argparse.ArgumentParser(USAGE)
    parser.add_argument('brightness', type=check_brightness,
                        help='Set the screen brightness between 0 and 255 or auto.')
    args = parser.parse_args()

    sys.stdout.write(DATA)
