# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from math import floor
from adafruit_rplidar import RPLidar
import busio
# from busio import UART
# from typing import Tuple, Dict, Any, Optional, List, Iterator, Union
from digitalio import DigitalInOut
import board
print(board.GPIO12)
motor_pin = DigitalInOut(board.GPIO12)
# motor_pin.value = 12
# Setup the RPLidar
PORT_NAME = busio.UART
lidar = RPLidar(motor_pin, PORT_NAME, 115200, timeout=3)


# used to scale data to fit on the screen
max_distance = 0


def process_data(data):
    print(data)


scan_data = [0] * 360

try:
    #    print(lidar.get_info())
    for scan in lidar.iter_scans():
        for _, angle, distance in scan:
            scan_data[min([359, floor(angle)])] = distance
        process_data(scan_data)

except KeyboardInterrupt:
    print("Stopping.")
lidar.stop()
lidar.disconnect()
