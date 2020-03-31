#!/usr/bin/env python
import argparse
import json
import sys

# $ termux-camera-info -h
# Usage: termux-camera-info
# Get information about device camera(s).

USAGE = """termux-camera-info"""
DESCRIPTION = """Get information about device camera(s)."""

DATA = [
    {
        "id": "0",
        "facing": "back",
        "jpeg_output_sizes": [
            {
                "width": 640,
                "height": 480
            },
            {
                "width": 352,
                "height": 288
            },
            {
                "width": 320,
                "height": 240
            },
            {
                "width": 176,
                "height": 144
            },
            {
                "width": 1280,
                "height": 720
            },
            {
                "width": 1280,
                "height": 960
            }
        ],
        "focal_lengths": [
            5.0
        ],
        "auto_exposure_modes": [
            "CONTROL_AE_MODE_OFF",
            "CONTROL_AE_MODE_ON"
        ],
        "physical_size": {
            "width": 3.200000047683716,
            "height": 2.4000000953674316
        },
        "capabilities": [
            "backward_compatible"
        ]
    },
    {
        "id": "1",
        "facing": "front",
        "jpeg_output_sizes": [
            {
                "width": 1280,
                "height": 720
            },
            {
                "width": 320,
                "height": 240
            },
            {
                "width": 176,
                "height": 144
            },
            {
                "width": 1280,
                "height": 720
            },
            {
                "width": 640,
                "height": 480
            }
        ],
        "focal_lengths": [
            5.0
        ],
        "auto_exposure_modes": [
            "CONTROL_AE_MODE_OFF",
            "CONTROL_AE_MODE_ON"
        ],
        "physical_size": {
            "width": 3.200000047683716,
            "height": 2.4000000953674316
        },
        "capabilities": [
            "backward_compatible",
            "manual_sensor",
            "manual_post_processing",
            5,
            6,
            10
        ]
    }
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
