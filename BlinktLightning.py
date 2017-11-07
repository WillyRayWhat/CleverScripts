import blinkt
import time
import numpy as np

from blinkt import set_pixel, set_brightness, show, clear

set_brightness(1)



def flash(duration):
    clear()
    for pix in range(0,7):
        set_pixel(pix, 255,255,255)
    show()
    time.sleep(duration)
    clear()
    show()


    

def multi_flash():
    flash_count=min(8,max(3,np.random.poisson(5)))
    for i in range(0,flash_count):
        dur=np.random.exponential(.15)
        sleep_dur = np.random.exponential(.15)
        intensity = np.random.uniform(0,1)
        set_brightness(intensity)
        flash(dur)
        time.sleep(sleep_dur)

def main_loop():
    while True:
        time.sleep(np.random.exponential(5))
        multi_flash()

main_loop()
        
    
