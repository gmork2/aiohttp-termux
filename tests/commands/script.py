#!/usr/bin/env python
import argparse
import sys
from datetime import datetime

# Dummy script for job scheduling
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    sys.stdout.write(f'\r{datetime.now()}\n')
    sys.stdout.flush()
