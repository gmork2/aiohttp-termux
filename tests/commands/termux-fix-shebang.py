#!/usr/bin/env python
import argparse
import json
import sys

# termux-fix-shebang -h
# usage: termux-fix-shebang <files>
# Rewrite shebangs in specified files for running under Termux,
# which is done by rewriting #!*/bin/binary to #!/data/data/com.termux/files/usr/bin/binary.

USAGE = """termux-fix-shebang"""
EPILOG = """
Rewrite shebangs in specified files for running under Termux,
which is done by rewriting #!*/bin/binary to #!/data/data/com.termux/files/usr/bin/binary.
"""

DATA = {

}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, epilog=EPILOG)
    parser.add_argument('files', type=str, nargs='*')
    args = parser.parse_args()

    json_data = json.dumps(DATA)
    sys.stdout.write(json_data)
