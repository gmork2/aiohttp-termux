#!/usr/bin/env python
import argparse
import json
import sys

# termux-battery-status -h
# Usage: termux-battery-status
# Get the status of the device battery.

USAGE = """termux-battery-status"""
DESCRIPTION = """Get the status of the device battery."""

DATA = {
  "health": "GOOD",
  "percentage": 100,
  "plugged": "UNPLUGGED",
  "status": "NOT_CHARGING",
  "temperature": 25.0,
  "current": 900000
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
