#!/usr/bin/env python
import argparse
import sys

# termux-clipboard-set [text]
# Set the system clipboard text.
# The text to set is either supplied as arguments or read from stdin if no arguments are given.

USAGE = """termux-clipboard-set [text]"""
DESCRIPTION = """
    Set the system clipboard text. The text to set is either supplied as arguments or read from stdin
    if no arguments are given.
"""

DATA = ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()

    sys.stdout.write(DATA)
