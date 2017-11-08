import RPi.GPIO as GPIO
import time
from phue import Bridge

b = Bridge('<ip of bridge here>')
#b.connect()


print(b.get_group(1))
b.set_group(1, 'on', False)
on = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_two_clicks = 0
default_warm = 400
default_cool = 153

def set_scene(scene_number):
    print('Set Scene %d' % scene_number)
    if scene_number == 0:
        b.set_group(1, 'ct', default_warm)
        b.set_group(1, 'bri', 254)
    if scene_number == 1:
        b.set_group(1, 'ct', default_warm)
        b.set_group(1, 'bri', 127)
    if scene_number == 2:
        b.set_group(1, 'ct', default_warm)
        b.set_group(1, 'bri', 63)
    if scene_number == 3:
        b.set_group(1, 'ct', default_cool)
        b.set_group(1, 'bri', 127)
    if scene_number == 4:
        b.set_group(1, 'ct', default_cool)
        b.set_group(1, 'bri', 254)


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
        button_two_clicks = button_two_clicks+1
        set_scene(button_two_clicks % 5)
        time.sleep(0.2)





