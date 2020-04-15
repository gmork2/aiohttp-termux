#!/usr/bin/env python
import argparse
import sys

# termux-share -h
# Usage: termux-share [-a action] [-c content-type] [-d] [-t title] [file]
# Share a file specified as argument or the text received on stdin if no file argument is given.
#   -a action        which action to performed on the shared content:
#                      edit/send/view (default:view)
#   -c content-type  content-type to use (default: guessed from file extension,
#                      text/plain for stdin)
#   -d               share to the default receiver if one is selected
#                      instead of showing a chooser
#   -t title         title to use for shared content (default: shared file name)

USAGE = """termux-share"""
DESCRIPTION = """Share a file specified as argument or the text received on stdin if no file argument is given."""

# termux-share file.txt
DATA = ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument(
        '-a', type=str, metavar='action', default='view',
        help='which action to performed on the shared content: edit/send/view (default:view)'
    )
    parser.add_argument(
        '-c', type=str, metavar='content-type',
        help='content-type to use (default: guessed from file extension, text/plain for stdin)'

    )
    parser.add_argument(
        '-d', action='store_true',
        help='share to the default receiver if one is selected instead of showing a chooser'
    )
    parser.add_argument(
        '-t', type=str, metavar='title',
        help='title to use for shared content (default: shared file name)'
    )
    args = parser.parse_args()
    sys.stdout.write(DATA)
