#!/usr/bin/env python
import argparse
import sys

# termux-camera-photo -h
# Usage: termux-camera-photo [-c camera-id] output-file
# Take a photo and save it to a file in JPEG format.
#   -c camera-id  ID of the camera to use (see termux-camera-info), default: 0

USAGE = """termux-camera-photo"""
DESCRIPTION = """Take a photo and save it to a file in JPEG format."""

DATA = ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(USAGE)
    parser.add_argument('output-file', type=str)
    parser.add_argument('-c', type=int, metavar='camera-id',
                        help='ID of the camera to use (see termux-camera-info), default: 0')
    args = parser.parse_args()

    sys.stdout.write(DATA)
