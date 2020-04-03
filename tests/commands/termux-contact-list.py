#!/usr/bin/env python
import argparse
import json
import sys

# termux-contact-list -h
# Usage: termux-contact-list
# List all contacts.

USAGE = """termux-contact-list"""
DESCRIPTION = """List all contacts."""

DATA = [
  {
    "name": "John Snow",
    "number": "(955) 677-655"
  }
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
