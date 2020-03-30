#!/usr/bin/env python
import argparse
import json
import sys

# termux-audio-info -h
# Usage: termux-audio-info
# Get information about audio capabilities.

USAGE = """termux-audio-info"""
DESCRIPTION = """Get information about audio capabilities."""

DATA = {
  "PROPERTY_OUTPUT_SAMPLE_RATE": "48000",
  "PROPERTY_OUTPUT_FRAMES_PER_BUFFER": "192",
  "AUDIOTRACK_SAMPLE_RATE": 48000,
  "AUDIOTRACK_BUFFER_SIZE_IN_FRAMES": 3844,
  "AUDIOTRACK_SAMPLE_RATE_LOW_LATENCY": 48000,
  "AUDIOTRACK_BUFFER_SIZE_IN_FRAMES_LOW_LATENCY": 192,
  "BLUETOOTH_A2DP_IS_ON": False,
  "WIREDHEADSET_IS_CONNECTED": False
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
