#!/usr/bin/env python
import argparse
import sys

# termux-job-scheduler -h
# Usage: termux-job-scheduler [options]
# Schedule a script to run at specified intervals.
#   -p/--pending               list pending jobs and exit
#   --cancel-all               cancel all pending jobs and exit
#   --cancel                   cancel given job-id and exit
# Options for scheduling:
#   -s/--script path           path to the script to be called
#   --job-id int               job id (will overwrite any previous job with the same id)
#   --period-ms int            schedule job approximately every period-ms milliseconds (default 0 means once).
#                              Note that since Android N, the minimum period is 900.000ms (15 minutes).
#   --network text             run only when this type of network available (default any):
#                              any|unmetered|cellular|not_roaming|none
#   --battery-not-low boolean  run only when battery is not low, default true (at least Android O)
#   --storage-not-low boolean  run only when storage is not low, default false (at least Android O)
#   --charging boolean         run only when charging, default false
#   --persisted boolean        should the job survive reboots, default false
#   --trigger-content-uri text (at least Android N)
#   --trigger-content-flag int default 1, (at least Android N)

USAGE = """termux-job-scheduler"""
DESCRIPTION = """Schedule a script to run at specified intervals."""

# termux-job-scheduler -s $PWD/script.py --period-ms 5000
SCHEDULE_JOB = """
Scheduling Job 0: /data/data/com.termux/files/home/workspace/websocket-termux/tests/commands/cmd.py
(periodic: 900000ms) (battery not low) (network: NetworkRequest [ NONE id=0, [ 
Capabilities: INTERNET&NOT_RESTRICTED&TRUSTED&VALIDATED Unwanted:  Uid: 10086] ]) - response 1
"""

# termux-job-scheduler -p
PENDING_JOB = """
Pending Job 0: /data/data/com.termux/files/home/workspace/websocket-termux/tests/commands/cmd.py 
(periodic: 900000ms) (battery not low) (network: NetworkRequest [ NONE id=0, [ 
Capabilities: INTERNET&NOT_RESTRICTED&TRUSTED&VALIDATED Unwanted:  Uid: 10086] ])
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument('-p', '--pending', action='store_true', help='list pending jobs and exit')
    parser.add_argument('--cancel-all', action='store_true', help='cancel all pending jobs and exit')
    parser.add_argument('-cancel', action='store_true', help='cancel given job-id and exit')

    parser.add_argument('-s', '--script', type=str, metavar='path', help='path to the script to be called')
    parser.add_argument(
        '--job-id', type=int, metavar='int', help='job id (will overwrite any previous job with the same id)'
    )
    parser.add_argument(
        '--period-ms', type=int, metavar='int',
        help='schedule job approximately every period-ms milliseconds (default 0 means once). '
             'Note that since Android N, the minimum period is 900.000ms (15 minutes).'
    )
    parser.add_argument(
        '--network', type=str, metavar='text',
        help='run only when this type of network available (default any): any|unmetered|cellular|not_roaming|none')
    parser.add_argument(
        '--battery-not-low', type=bool, metavar='boolean',
        help='run only when battery is not low, default true (at least Android O)'
    )
    parser.add_argument(
        '--storage-not-low', type=bool, metavar='boolean',
        help='run only when storage is not low, default false (at least Android O)'
    )
    parser.add_argument('--charging', type=bool, metavar='boolean', help='run only when charging, default false')
    parser.add_argument(
        '--persisted', type=bool, metavar='boolean', help='should the job survive reboots, default false'
    )
    parser.add_argument('--trigger-content-uri', type=str, metavar='text', help='(at least Android N)')
    parser.add_argument('--trigger-content-flag', type=int, metavar='int', help='default 1, (at least Android N)')
    args = parser.parse_args()

    sys.stdout.write(SCHEDULE_JOB)
