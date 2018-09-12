#!/usr/bin/env python
# -*- coding: utf-8 -*-
from quickweather import QuickWeather
from pprint import pprint
import json
import os
import re
import RPi.GPIO as GPIO
from datetime import datetime


def rain_delay(myforecast, mypin):
    """Function to set actual rain delay"""
    runtime = datetime.now()
    last_rain = datetime.strptime(myforecast['last_rain'], "%Y-%m-%dT%H:%M:%S")
    td = runtime - last_rain
    mlc = myforecast['last_status_check']
    if td.days > 1 and (mlc or mlc is None):
        print("Ensuring rain delay is OFF")
        GPIO.output(mypin, False)
        myforecast['last_status_check'] = False
    elif td.days < 1 and (not mlc or mlc is None):
        print("Ensuring rain delay is ON")
        GPIO.output(mypin, True)
        myforecast['last_status_check'] = True
    return myforecast


def prepare_state(state_file, myforecast):
    """Function to write to state file"""
    if not os.path.isfile(state_file):
        print("Creating state file")
        f = open(state_file, 'w')
        f.close()
    with open(state_file, "r") as state:
        try:
            last = json.loads(state.read())
        except ValueError:
            print("Unable to load json from state file, using empty data.")
            last = {}
        if re.match(".*rain.*", x.description.lower()):
            myforecast['last_rain'] = myforecast['build_date']
        elif 'last_rain' not in last:
            myforecast['last_rain'] = "1980-01-01T00:00:00"
        else:
            myforecast['last_rain'] = last['last_rain']
        if 'last_status_check' not in last:
            last['last_status_check'] = None
        myforecast['last_status_check'] = last['last_status_check']
    return myforecast


def write_state(state_file, myforecast):
    with open(state_file, "w") as state:
        state.write(json.dumps(myforecast))


if __name__ == "__main__":
    # setup
    pin = int(12)
    statefile = '/tmp/rain_delay_status'
    gpio_mode = GPIO.BOARD
    GPIO.setmode(gpio_mode)
    GPIO.setup(pin, GPIO.OUT)
    # get weather
    x = QuickWeather()
    forecast = json.loads(x.get_json())
    forecast = prepare_state(statefile, forecast)
    # determine rain_delay
    forecast = rain_delay(forecast, pin)
    write_state(statefile, forecast)
    # teardown
    GPIO.cleanup()
