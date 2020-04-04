#!/usr/bin/env python
import argparse
import json
import sys

USAGE = """termux-create-package"""
DESCRIPTION = """"""

DATA = {

}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()
    json_data = json.dumps(DATA)

    sys.stdout.write(json_data)
