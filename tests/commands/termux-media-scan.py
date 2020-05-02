#!/usr/bin/env python
import argparse
import json
import sys

# termux-media-scan -h
# Usage: termux-media-scan [-v] [-r] file [file...]
# Scan the specified file(s) and add it to the media content provider.
#   -r  scan directories recursively
#   -v  verbose mode

USAGE = """termux-media-scan"""
DESCRIPTION = """Scan the specified file(s) and add it to the media content provider."""

# termux-media-scan -r . -v
MEDIA_SCAN = """Finished scanning 58 file(s)"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument('file', type=str)
    parser.add_argument('-v', action='store_true', help='verbose mode')
    parser.add_argument('-r', action='store_true', help='scan directories recursively')
    args = parser.parse_args()
    json_data = json.dumps(MEDIA_SCAN)

    sys.stdout.write(json_data)
