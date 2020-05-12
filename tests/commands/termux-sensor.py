#!/usr/bin/env python
import argparse
import json
import sys
import random

# termux-sensor -h
# Usage: termux-sensor
# Get information about types of sensors as well as live data
#   -h, help           Show this help
#   -a, all            Listen to all sensors (WARNING! may have battery impact)
#   -c, cleanup        Perform cleanup (release sensor resources)
#   -l, list           Show list of available sensors
#   -s, sensors [,,,]  Sensors to listen to (can contain just partial name)
#   -d, delay [ms]     Delay time in milliseconds before receiving new sensor update
#   -n, limit [num]    Number of times to read sensor(s) (default: continuous) (min: 1)


USAGE = """termux-sensor"""
DESCRIPTION = """Get information about types of sensors as well as live data"""

# termux-sensor -a
SENSOR_ALL = {
    "Goldfish 3-axis Accelerometer": {
        "values": [
            0,
            9.776309967041016,  # randomize
            0.8123490214347839
        ]
    },
    "Game Rotation Vector Sensor": {
        "values": [
            0.6771285533905029,
            -2.14633018913446E-5,
            -1.260980498045683E-4,
            0.7358648180961609
        ]
    },
    "GeoMag Rotation Vector Sensor": {
        "values": [
            0.677196741104126,
            1.8694560602241367E-13,
            -2.5895618657213737E-13,
            0.7358020544052124,
            0
        ]
    },
    "Goldfish 3-axis Gyroscope": {
        "values": [
            0,
            0,
            0
        ]
    },
    "Goldfish 3-axis Magnetic field sensor": {
        "values": [
            0,
            9.887660026550293,
            -47.745201110839844
        ]
    },
    "Goldfish 3-axis Magnetic field sensor (uncalibrated)": {
        "values": [
            0,
            9.887660026550293,
            -47.745201110839844,
            4.203895392974451E-45,
            0,
            0
        ]
    },
    "Goldfish Ambient Temperature sensor": {
        "values": [
            0
        ]
    },
    "Goldfish Humidity sensor": {
        "values": [
            0
        ]
    },
    "Goldfish Light sensor": {
        "values": [
            0
        ]
    },
    "Goldfish Orientation sensor": {
        "values": [
            -0.08290310204029083,
            0,
            0
        ]
    },
    "Goldfish Pressure sensor": {
        "values": [
            1013.25
        ]
    },
    "Goldfish Proximity sensor": {
        "values": [
            1
        ]
    },
    "Gravity Sensor": {
        "values": [
            -0.001364899449981749,
            9.772818565368652,
            0.8138918280601501
        ]
    },
    "Orientation Sensor": {
        "values": [
            359.9999694824219,
            -85.25000762939453,
            2.017623592109885E-5
        ]
    },
    "Linear Acceleration Sensor": {
        "values": [
            0.001364899449981749,
            0.0034914016723632812,
            -0.001542806625366211
        ]
    },
    "Rotation Vector Sensor": {
        "values": [
            0.6771971583366394,
            1.331396592973988E-8,
            2.7446557737675903E-7,
            0.735801637172699,
            0
        ]
    }
}

# termux-sensor -c
SENSOR_CLEANUP = "Sensor cleanup unnecessary"

# termux-sensor -l
SENSOR_LIST = {
    "sensors": [
        "Goldfish 3-axis Accelerometer",
        "Goldfish 3-axis Gyroscope",
        "Goldfish 3-axis Magnetic field sensor",
        "Goldfish Orientation sensor",
        "Goldfish Ambient Temperature sensor",
        "Goldfish Proximity sensor",
        "Goldfish Light sensor",
        "Goldfish Pressure sensor",
        "Goldfish Humidity sensor",
        "Goldfish 3-axis Magnetic field sensor (uncalibrated)",
        "Game Rotation Vector Sensor",
        "GeoMag Rotation Vector Sensor",
        "Gravity Sensor",
        "Linear Acceleration Sensor",
        "Rotation Vector Sensor",
        "Orientation Sensor"
    ]
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument(
        '-a', action='store_true',
        help='Listen to all sensors (WARNING! may have battery impact)'
    )
    parser.add_argument(
        '-c', action='store_true',
        help='Perform cleanup (release sensor resources)'
    )
    parser.add_argument(
        '-l', action='store_true',
        help='Show list of available sensors'
    )
    parser.add_argument(
        '-s', type=str, metavar='sensors [,,,]',
        help='Sensors to listen to (can contain just partial name)'
    )
    parser.add_argument(
        '-d', type=int, metavar='delay [ms]',
        help='Delay time in milliseconds before receiving new sensor update'
    )
    parser.add_argument(
        '-n', type=str, metavar='limit [num]', default='continuous',
        help='Number of times to read sensor(s) (default: continuous) (min: 1)'
    )
    args = parser.parse_args()
    json_data = json.dumps(SENSOR_ALL)

    sys.stdout.write(json_data)
