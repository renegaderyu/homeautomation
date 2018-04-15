#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import argparse
import time

parser = argparse.ArgumentParser(description='Script to toggle a RasPi GPIO pin like a momentary switch w/ given time delay acting as the activation time.')
parser.add_argument("-p", "--pin", help="GPIO pin to set.", default=int(7))
parser.add_argument("-b", "--bcm", help="Set gpio mode to BCM (Broadcom SoC numbering) default is board numbering.", action='store_true')
parser.add_argument("-l", "--low", help="Set gpio pin to LOW default is set HIGH.", action='store_true')
parser.add_argument("-t", "--time", help="Sleep time between state change.", default=0.2)
args = parser.parse_args()

gpio_mode = GPIO.BOARD
begin_state = True

if args.bcm:
    gpio_mode = GPIO.BCM
if args.low:
    begin_state = False

GPIO.setmode(gpio_mode)
GPIO.setup(args.pin, GPIO.OUT)
GPIO.output(args.pin, begin_state)
time.sleep(args.time)
GPIO.output(args.pin, not begin_state)
GPIO.cleanup()
