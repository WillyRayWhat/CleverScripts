#!/usr/bin/python3

import serial
import phue as hue


b = hue.Bridge('192.168.1.227')
b.connect()
ser = serial.Serial('/dev/ttyACM0', 9600)

lights = b.get_light_objects('id')

kitchen_lights = []

for i in [7, 9, 10, 12, 8, 11]:
    kitchen_lights.append(lights[i])

# read response back from Arduino
while True:
    input = ser.readline()
    if input:
        print(input)
        values = input.split(',')
        for item in kitchen_lights.__iter__():
            bright = item.brightness
            item.transitiontime = 0
            item.brightness = int(values[1])

