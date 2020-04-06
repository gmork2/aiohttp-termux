#!/usr/bin/env python
import argparse
import json
import sys

# termux-dialog -h
# Usage: termux-dialog widget [options]
# Get user input w/ different widgets! Default: text
#    -h, help   Show this help
#    -l, list   List all widgets and their options
#    -t, title  Set title of input dialog (optional)
#

USAGE = """termux-battery-status"""
DESCRIPTION = """Get the status of the device battery."""
EPILOG = """Supported widgets:

    confirm - Show confirmation dialog
        [-i hint] text hint (optional)
        [-t title] set title of dialog (optional)

    checkbox - Select multiple values using checkboxes
        [-v ",,,"] comma delim values to use (required)
        [-t title] set title of dialog (optional)

    counter - Pick a number in specified range
        [-r min,max,start] comma delim of (3) numbers to use (optional)
        [-t title] set title of dialog (optional)

    date - Pick a date
        [-t title] set title of dialog (optional)
        [-d "dd-MM-yyyy k:m:s"] SimpleDateFormat Pattern for date widget output (optional)

    radio - Pick a single value from radio buttons
        [-v ",,,"] comma delim values to use (required)
        [-t title] set title of dialog (optional)

    sheet - Pick a value from sliding bottom sheet
        [-v ",,,"] comma delim values to use (required)
        [-t title] set title of dialog (optional)

    spinner - Pick a single value from a dropdown spinner
        [-v ",,,"] comma delim values to use (required)
        [-t title] set title of dialog (optional)

    speech - Obtain speech using device microphone
        [-i hint] text hint (optional)
        [-t title] set title of dialog (optional)

    text - Input text (default if no widget specified)
        [-i hint] text hint (optional)
        [-m] multiple lines instead of single (optional)*
        [-n] enter input as numbers (optional)*
        [-p] enter input as password (optional)
        [-t title] set title of dialog (optional)
            * cannot use [-m] with [-n]

    time - Pick a time value
        [-t title] set title of dialog (optional)
"""

# termux-dialog confirm -t Title
CONFIRM_YES = {
    "code": 0,
    "text": "yes"
}

CONFIRM_NO = {
    "code": 0,
    "text": "no"
}

# termux-dialog checkbox -t Title -v 1,2,3
CHECKBOX_OK = {
    "code": -1,
    "text": "[2, 3]",
    "values": [
        {
            "index": 1,
            "text": "2"
        },
        {
            "index": 2,
            "text": "3"
        }
    ]
}

CHECKBOX_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog counter -r 0,10,1
COUNTER_OK = {
    "code": -1,
    "text": "2"
}

COUNTER_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog date
DATE_OK = {
    "code": -1,
    "text": "Thu Mar 19 00:00:00 GMT+01:00 2020"
}

# termux-dialog date -d "01-12-2020 00:00:01"
DATE_SET = {
    "code": -1,
    "text": "01-12-2020 00:00:01"
}

DATE_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog radio -v 1,2,3
RADIO_OK = {
    "code": -1,
    "text": "2",
    "index": 1
}

RADIO_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog sheet -v 1,2,3
SHEET_OK = {
    "code": 0,
    "text": "2",
    "index": 1
}

SHEET_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog spinner -v 1,2,3
SPINNER_OK = {
    "code": -1,
    "text": "2",
    "index": 1
}

SPINNER_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog speech -i "Hi all"
SPEECH_OK = {

}

SPEECH_CANCEL = {

}

SPEECH_ERROR = {
    "code": 0,
    "text": "",
    "error": "ERROR_NETWORK"
}

# termux-dialog -t Title -i "Text" -p
TEXT_OK = {
    "code": -1,
    "text": "hello world",
    "index": 1
}

TEXT_CANCEL = {
    "code": -2,
    "text": ""
}

# termux-dialog time
TIME_OK = {
    "code": -1,
    "text": "07:10"
}

TERMUX_CANCEL = {
    "code": -2,
    "text": ""
}


class Command(object):
    WIDGETS = [
        'confirm', 'checkbox', 'counter', 'date', 'radio', 'sheet', 'spinner', 'speech', 'text', 'time'
    ]

    def __init__(self):
        """
        Usage: termux-dialog widget [options]
        Get user input w/ different widgets! Default: text
            -h, help   Show this help
            -l, list   List all widgets and their options
            -t, title  Set title of input dialog (optional)
        """
        parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
        parser.add_argument('-l', action='store_true', help='List all widgets and their options')
        parser.add_argument('-t', type=str, metavar='title', help='Set title of input dialog (optional)')
        parser.add_argument('widget', nargs='?')

        args = parser.parse_args(sys.argv[1:2])
        self.title = args.t
        if args.l:
            sys.stdout.write(EPILOG)
        elif args.widget in self.WIDGETS:
            getattr(self, args.widget, lambda: None)()

    def confirm(self) -> None:
        """
        confirm - Show confirmation dialog
            [-i hint] text hint (optional)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='confirm', description='Show confirmation dialog')
        parser.add_argument('-i', type=str, metavar='hint', help='text hint (optional)')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        parser.parse_args(sys.argv[2:])

        json_data = json.dumps(CONFIRM_YES)
        sys.stdout.write(json_data)

    def checkbox(self) -> None:
        """
        checkbox - Select multiple values using checkboxes
            [-v ",,,"] comma delim values to use (required)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='checkbox', description='Select multiple values using checkboxes')
        parser.add_argument('-v', type=str, metavar=',,,', help='comma delim values to use (required)')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        args = parser.parse_args(sys.argv[2:])
        if not args.v:
            parser.print_help()
        else:
            json_data = json.dumps(CHECKBOX_OK)
            sys.stdout.write(json_data)

    def counter(self) -> None:
        """
        counter - Pick a number in specified range
            [-r min,max,start] comma delim of (3) numbers to use (optional)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='counter', description='Pick a number in specified range')
        parser.add_argument(
            '-r', type=str, metavar='min,max,start',
            help='comma delim of (3) numbers to use (optional)'
        )
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        parser.parse_args(sys.argv[2:])
        json_data = json.dumps(COUNTER_OK)
        sys.stdout.write(json_data)

    def date(self) -> None:
        """
        date - Pick a date
            [-t title] set title of dialog (optional)
            [-d "dd-MM-yyyy k:m:s"] SimpleDateFormat Pattern for date widget output (optional)
        """
        parser = argparse.ArgumentParser(usage='date', description='Pick a date')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        parser.add_argument(
            '-d', type=str, metavar='"dd-MM-yyyy k:m:s"',
            help='SimpleDateFormat Pattern for date widget output (optional)'
        )
        parser.parse_args(sys.argv[2:])
        json_data = json.dumps(DATE_OK)
        sys.stdout.write(json_data)

    def radio(self) -> None:
        """
        radio - Pick a single value from radio buttons
            [-v ",,,"] comma delim values to use (required)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='radio', description='Pick a single value from radio buttons')
        parser.add_argument('-v', type=str, metavar=',,,', help='comma delim values to use (required)')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        args = parser.parse_args(sys.argv[2:])
        if not args.v:
            parser.print_help()
        else:
            json_data = json.dumps(RADIO_OK)
            sys.stdout.write(json_data)

    def sheet(self) -> None:
        """
        sheet - Pick a value from sliding bottom sheet
            [-v ",,,"] comma delim values to use (required)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='sheet', description='Pick a value from sliding bottom sheet')
        parser.add_argument('-v', type=str, metavar=',,,', help='comma delim values to use (required)')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        args = parser.parse_args(sys.argv[2:])
        if not args.v:
            parser.print_help()
        else:
            json_data = json.dumps(SHEET_OK)
            sys.stdout.write(json_data)

    def spinner(self) -> None:
        """
        spinner - Pick a single value from a dropdown spinner
            [-v ",,,"] comma delim values to use (required)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='spinner', description='Pick a single value from a dropdown spinner')
        parser.add_argument('-v', type=str, metavar=',,,', help='comma delim values to use (required)')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        args = parser.parse_args(sys.argv[2:])
        if not args.v:
            parser.print_help()
        else:
            json_data = json.dumps(SPINNER_OK)
            sys.stdout.write(json_data)

    def speech(self) -> None:
        """
        speech - Obtain speech using device microphone
            [-i hint] text hint (optional)
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='speech', description='Obtain speech using device microphone')
        parser.add_argument('-i', type=str, metavar='hint', help='text hint (optional)')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        parser.parse_args(sys.argv[2:])

        json_data = json.dumps(SPEECH_OK)
        sys.stdout.write(json_data)

    def text(self) -> None:
        """
        text - Input text (default if no widget specified)
            [-i hint] text hint (optional)
            [-m] multiple lines instead of single (optional)*
            [-n] enter input as numbers (optional)*
            [-p] enter input as password (optional)
            [-t title] set title of dialog (optional)
               * cannot use [-m] with [-n]
        """
        parser = argparse.ArgumentParser(
            usage='text',
            description='Input text (default if no widget specified)',
            epilog='* cannot use [-m] with [-n]'
        )
        parser.add_argument('-i', type=str, metavar='hint', help='text hint (optional)')
        parser.add_argument('-m', type=str, help='multiple lines instead of single (optional)*')
        parser.add_argument('-n', type=str, help='enter input as numbers (optional)*')
        parser.add_argument('-p', type=str, help='enter input as password')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        args = parser.parse_args(sys.argv[2:])
        if args.m and args.n:
            parser.print_help()
        else:
            json_data = json.dumps(TEXT_OK)
            sys.stdout.write(json_data)

    def time(self) -> None:
        """
        time - Pick a time value
            [-t title] set title of dialog (optional)
        """
        parser = argparse.ArgumentParser(usage='time', description='Pick a time value')
        parser.add_argument('-t', type=str, metavar='title', help='set title of dialog (optional)')
        parser.parse_args(sys.argv[2:])

        json_data = json.dumps(TIME_OK)
        sys.stdout.write(json_data)


if __name__ == "__main__":
    Command()
