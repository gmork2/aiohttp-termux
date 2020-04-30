#!/usr/bin/env python
import argparse
import json
import sys

# termux-infrared-transmit -h
# Usage: termux-infrared-transmit -f frequency pattern
# Transmit an infrared pattern. The pattern is specified in comma-separated on/off intervals, such as '20,50,20,30'.
# Only patterns shorter than 2 seconds will be transmitted.
#   -f frequency  IR carrier frequency in Hertz

USAGE = """termux-infrared-transmit"""
DESCRIPTION = """
Transmit an infrared pattern. The pattern is specified in comma-separated on/off intervals, such as '20,50,20,30'.
Only patterns shorter than 2 seconds will be transmitted.
"""

# termux-infrared-transmit -f 2000 "20,50,20,30"
INFRARED_TRANSMIT_ERROR = {
    "API_ERROR": "No infrared emitter available"
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument('pattern', type=str)
    parser.add_argument('-f', type=str, metavar='frequency', help='IR carrier frequency in Hertz')
    args = parser.parse_args()

    json_data = json.dumps(INFRARED_TRANSMIT_ERROR)
    sys.stdout.write(json_data)
