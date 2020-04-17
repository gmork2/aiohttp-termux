#!/usr/bin/env python
import argparse
import json
import sys

# termux-usb -h
# Usage: termux-usb [-l | [-r] [-e command] device]
# List or access USB devices. Devices cannot be accessed directly,
#                  only using termux-usb.
#   -l           list available devices
#   -r           show permission request dialog if necessary
#   -e command   execute the specified command with a file descriptor
#                  referring to the device as its argument

USAGE = """termux-usb"""
DESCRIPTION = """List or access USB devices. Devices cannot be accessed directly, only using termux-usb."""

# termux-usb -l
DATA = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument('device', type=str)
    parser.add_argument('-l', action='store_true', help='list available devices')
    parser.add_argument('-r', action='store_true', help='show permission request dialog if necessary')
    parser.add_argument(
        '-e', type=str, metavar='command',
        help='execute the specified command with a file descriptor referring to the device as its argument'
    )
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
