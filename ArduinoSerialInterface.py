#!/usr/bin/python3

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

# read response back from Arduino
while True:
    input = ser.readline()
    if input:
        print(input)

