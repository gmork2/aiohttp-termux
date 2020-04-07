#!/usr/bin/env python
import argparse
import json
import sys

# termux-download -h
# Usage: termux-download [-d description] [-t title] url-to-download
# Download a resource using the system download manager.
#   -d description  description for the download request notification
#   -t title        title for the download request notification

USAGE = """termux-download"""
DESCRIPTION = """Download a resource using the system download manager."""

# termux-download -d description https://dominoes.readthedocs.io/en/latest/_sources/index.txt
DATA = {

}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument('url-to-download', type=str)
    parser.add_argument('-d', type=str, metavar='description', help='description for the download request notification')
    parser.add_argument('-t', type=str, metavar='title', help='title for the download request notification')
    args = parser.parse_args()

    json_data = json.dumps(DATA)
    sys.stdout.write(json_data)
