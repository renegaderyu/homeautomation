#!/usr/bin/env python
# -*- coding: utf-8 -*-
from quickweather import QuickWeather
import re


def rain_delay():
    """Function to set actual rain delay"""
    print("Rain detected, setting a rain delay")


if __name__ == "__main__":
    x = QuickWeather()
    if re.match("rain", x.description.lower()):
        rain_delay()
