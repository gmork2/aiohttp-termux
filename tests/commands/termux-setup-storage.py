#!/usr/bin/env python
import argparse
import sys

# termux-setup-storage -h
# usage: termux-setup-storage
# Use without arguments to ensure storage permission granted
# and symlinks to storage available in $HOME/storage

USAGE = """termux-setup-storage"""
EPILOG = """
Use without arguments to ensure storage permission granted
and symlinks to storage available in $HOME/storage
"""

# termux-setup-storage
DATA = ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, epilog=EPILOG)
    args = parser.parse_args()

    sys.stdout.write(DATA)
