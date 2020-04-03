#!/usr/bin/env python
import argparse
import sys

# termux-clipboard-get -h
# Usage: termux-clipboard-get
# Get the system clipboard text.

USAGE = """termux-clipboard-get"""
DESCRIPTION = """Get the system clipboard text."""

DATA = "Clipboard"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()

    sys.stdout.write(DATA)
