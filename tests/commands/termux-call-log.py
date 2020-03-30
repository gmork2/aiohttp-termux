#!/usr/bin/env python
import argparse
import json
import sys

# termux-call-log -h
# Usage: termux-call-log [-l limit] [-o offset]
# List call log history
#   -l limit   offset in call log list (default: 10)
#   -o offset  offset in call log list (default: 0)

USAGE = """termux-call-log"""
DESCRIPTION = """List call log history"""


ERROR = {
  "error": "Call log is no longer permitted by Google"
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(USAGE)
    parser.add_argument('-l', type=int, metavar='limit', help='offset in call log list (default: 10)')
    parser.add_argument('-o', type=int, metavar='offset', help='offset in call log list (default: 0)')
    args = parser.parse_args()

    json_data = json.dumps(ERROR)
    sys.stdout.write(json_data)
