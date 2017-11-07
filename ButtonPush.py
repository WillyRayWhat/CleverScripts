import RPi.GPIO as GPIO
import time
from phue import Bridge

b = Bridge('192.168.1.227')
#b.connect()



print(b.get_group(1))
b.set_group(1, 'on', False)
on = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state1 = GPIO.input(18)
    input_state2 = GPIO.input(16)
    if input_state1 == False:
        print('Button 1 Pressed')
        b.set_group(1, 'on', not on)
        on = not on
        print('Office Lights on: %s' % on)
        time.sleep(0.2)
    if input_state2 == False:
        print('Button 2 Pressed')
        time.sleep(0.2)
