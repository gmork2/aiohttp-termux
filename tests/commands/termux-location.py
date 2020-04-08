#!/usr/bin/env python
import argparse
import json
import sys

# termux-location -h
# usage: termux-location [-p provider] [-r request]
# Get the device location.
#   -p provider  location provider [gps/network/passive] (default: gps)
#   -r request   kind of request to make [once/last/updates] (default: once)

USAGE = """termux-location"""
DESCRIPTION = """Get the device location."""

PROVIDERS = ['gps', 'network', 'passive']
REQUESTS = ['once', 'last', 'updates']

# termux-location -p gps -r updates
LOCATION_GPS = {
    "latitude": 37.421998333333335,
    "longitude": -122.08400000000002,
    "altitude": 5.0,
    "accuracy": 20.0,
    "vertical_accuracy": 0.0,
    "bearing": 0.0,
    "speed": 0.0,
    "elapsedMs": 1,
    "provider": "gps"
}

LOCATION_ERROR = {
    "API_ERROR": "Failed to get location"
}


def check_provider(value: str) -> str:
    if value not in PROVIDERS:
        raise argparse.ArgumentTypeError(f"Invalid provider value ({value})")
    return value


def check_request(value: str) -> str:
    if value not in REQUESTS:
        raise argparse.ArgumentTypeError(f"Invalid request value ({value})")
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument(
        '-p', type=check_provider, metavar='provider', default='gps',
        help='location provider [gps/network/passive] (default: gps)'
    )
    parser.add_argument(
        '-r', type=check_request, metavar='request', default='once',
        help='kind of request to make [once/last/updates] (default: once)'
    )
    args = parser.parse_args()
    json_data = json.dumps(LOCATION_GPS)
    sys.stdout.write(json_data)
