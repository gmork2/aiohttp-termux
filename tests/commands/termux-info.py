#!/usr/bin/env python
import argparse
import sys

# termux-info -h
# usage: termux-info
# Provides information about Termux, and the current system. Helpful for debugging.
USAGE = """termux-info"""
DESCRIPTION = """Provides information about Termux, and the current system. Helpful for debugging."""

DATA = """
Packages CPU architecture:
i686
Subscribed repositories:
# sources.list
deb https://termux.org/packages/ stable main
# science-repo (sources.list.d/science.list)
deb https://dl.bintray.com/grimler/science-packages-24 science stable
# game-repo (sources.list.d/game.list)
deb https://dl.bintray.com/grimler/game-packages-24 games stable
Updatable packages:
apt/stable 1.4.9-27 i686 [upgradable from: 1.4.9-25]
command-not-found/stable 1.48 i686 [upgradable from: 1.47]
dpkg/stable 1.20.0-2 i686 [upgradable from: 1.20.0]
git/stable 2.25.2 i686 [upgradable from: 2.25.1]
gpgv/stable 2.2.20-2 i686 [upgradable from: 2.2.19]
liblzma/stable 5.2.5-1 i686 [upgradable from: 5.2.4-7]
openssl/stable 1.1.1e i686 [upgradable from: 1.1.1d-1]
python/stable 3.8.2-2 i686 [upgradable from: 3.8.2]
xz-utils/stable 5.2.5-1 i686 [upgradable from: 5.2.4-7]
Android version:
9
Kernel build information:
Linux localhost 4.4.124+ #1 SMP PREEMPT Wed Jan 30 07:13:09 UTC 2019 i686 Android
Device manufacturer:
Google
Device model:
AOSP on IA Emulator
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    args = parser.parse_args()

    sys.stdout.write(DATA)
