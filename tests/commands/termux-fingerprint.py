#!/usr/bin/env python
import argparse
import json
import sys

# termux-fingerprint -h
# Usage: termux-fingerprint [-t title] [-d description] [-s subtitle] [-c cancel]
# Use fingerprint sensor on device to check for authentication
# NOTE: Only available on Marshmallow and later

USAGE = """termux-fingerprint"""
DESCRIPTION = """Use fingerprint sensor on device to check for authentication."""
EPILOG = """NOTE: Only available on Marshmallow and later"""

# termux-fingerprint -t title -d description -s subtitle -c cancel
FINGERPRINT_OK = {
    "errors": [],
    "failed_attempts": 0,
    "auth_result": "AUTH_RESULT_SUCCESS"
}

FINGERPRINT_CANCEL = {
    "errors": [],
    "failed_attempts": 0,
    "auth_result": "AUTH_RESULT_FAILURE"
}

FINGERPRINT_ERROR = {
    "errors": [
        "ERROR_TIMEOUT"
    ],
    "failed_attempts": 0,
    "auth_result": "AUTH_RESULT_UNKNOWN"
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(USAGE)
    parser.add_argument('-t', type=str, metavar='title')
    parser.add_argument('-d', type=str, metavar='description')
    parser.add_argument('-s', type=str, metavar='subtitle')
    parser.add_argument('-c', type=str, metavar='cancel')
    args = parser.parse_args()

    json_data = json.dumps(FINGERPRINT_OK)
    sys.stdout.write(json_data)
