#!/usr/bin/env python
import argparse
import sys

USAGE = """termux-upgrade-repo"""

DATA = ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE)
    args = parser.parse_args()

    sys.stdout.write(DATA)
