#!/usr/bin/python3

import serial
import phue as hue
import time

b = hue.Bridge('192.168.1.227')
#b.connect()
ser = serial.Serial('/dev/ttyACM0', 9600)

lights = b.get_light_objects('id')

kitchen_lights = []

for i in [7, 9, 10, 12, 8, 11]:
    kitchen_lights.append(lights[i])

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
       

# read response back from Arduino
while True:
    input = ser.readline()
    if input:
        try:
            brightness = input.split(',')[1]
            if isInt(brightness):
                print(int(brightness))
                kitchen_lights[0].transitiontime = 0
                kitchen_lights[0].brightness = int(brightness)

