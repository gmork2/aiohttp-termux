#!/usr/bin/env python
import argparse
import json
import sys

# termux-infrared-frequencies -h
# Usage: termux-infrared-frequencies
# Query the infrared transmitter's supported carrier frequencies.

USAGE = """termux-infrared-frequencies"""
DESCRIPTION = """Query the infrared transmitter's supported carrier frequencies."""

DATA = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
