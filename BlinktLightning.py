"""
File Name: BlinktLighting.py
Author: Willy Ray
Date Created: October 2017

Requirements:
Numpy
The Blinkt library described here:
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt

Description:
This script drives a Pimoroni Blinkt led array to simulate a
non-deterministic lightning strike effect.

Lightning is modeled as follows:

A lighting flash is a single flash of the entire array, with a
duration, and an intensity.  The flash function is the only
function that directly addresses the Blinkt device.

A lighting strike is a sequence of multiple lightning flashes,
with flash intensity, duration and sleep-between-flash times drawn
from probability distributions.

The main loop samples intra-lightning strike times from
a exponential probability distribution.

"""

import blinkt
import time
import numpy as np

from blinkt import set_pixel, set_all, set_brightness, show, clear

# Color of flashes. These can be modified for non-white flashes.
R=255
G=255
B=255

# max and min brightness for an individual flash
min_intensity=.25
max_intensity = 1

# The mean duration for an individual flash, in seconds
mean_flash_duration=.15
# the mean duration for the time between flashes, in seconds
mean_sleep_duration=.15

# min, max and mean flash_count in a strike (initial value drawn from
# possion distribution)
min_flash_count = 3
max_flash_count = 8
mean_flash_count=4

# mean duration of time between lightning strikes, in seconds
mean_intra_strike_time = 5


def flash(duration, intensity):
    """
    This flashes the lights for a certain duration then shuts them off.
    :param duration: in seconds, duration of the flash
    :param intensity:  intensity of the flash, bounded [0,1]
    """
    clear()
    set_brightness(intensity)
    set_all(R,G,B)
    show()
    time.sleep(duration)
    clear()
    show()


def strike(flash_count):
    """
    This models a lightning strike, composed of several flashes.
    This is where the bulk of the samples are drawn from probability distributions
    :param flash_count: number of individual flashes composing this strike
    """
    for i in range(0,flash_count):
        # for each flash:

        # draw a sample from an exponential distribution with a given mean
        dur = np.random.exponential(mean_flash_duration)

        # Draw a sample for the amount of time before the next flash
        sleep_dur = np.random.exponential(mean_sleep_duration)

        # Draw a sample for the intensity of this flash
        intensity = np.random.uniform(min_intensity, max_intensity)

        # Lights on,
        flash(dur, intensity)
        # lights off
        time.sleep(sleep_dur)


def main_loop():
    while True:

        # randomly draw a number of flashes for this strike, and bound them
        # by the min/max
        flash_count = np.random.poisson(mean_flash_count)
        flash_count = max(min_flash_count, flash_count)
        flash_count = min(max_flash_count, flash_count)

        # execute the strike.
        strike(flash_count)

        # now draw a intra-strike time.  How long until the next strike?
        next_strike_in = np.random.exponential(mean_intra_strike_time)
        time.sleep(next_strike_in)

# Run it
main_loop()
