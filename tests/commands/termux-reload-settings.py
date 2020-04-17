#!/usr/bin/env python
import argparse
import sys

# termux-reload-settings -h
# usage: termux-reload-settings
# Use without arguments to reload settings after modifying any of:
#   ~/.termux/colors.properties
#   ~/.termux/font.ttf
#   ~/.termux/termux.properties

USAGE = """termux-reload-settings"""
EPILOG = """
Use without arguments to reload settings after modifying any of:
    ~/.termux/colors.properties
    ~/.termux/font.ttf
    ~/.termux/termux.properties
"""

# termux-reload-settings
DATA = ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, epilog=EPILOG)
    args = parser.parse_args()

    sys.stdout.write(DATA)
