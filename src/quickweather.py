#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from weather import Weather
from datetime import datetime
import json

__location_environment_variable__ = 'WOEID'


class QuickWeather(object):
    def __init__(self, location=None):
        weather = Weather()
        lookup = weather.lookup(self.__getLocation(location))
        self.title = lookup.title().replace('Yahoo! ', '')
        # for build_date I strip last 4 since %Z wasn't working in all scenarios
        self.build_date = datetime.strptime(lookup.last_build_date()[:-4], '%a, %d %b %Y %I:%M %p')
        self.units = lookup.units()
        self.sunrise = lookup.astronomy()['sunrise']
        self.sunset = lookup.astronomy()['sunset']
        self.wind = lookup.wind()
        self.atmosphere = lookup.atmosphere()
        self.description = lookup.condition().text()
        self.temp = lookup.condition().temp()
        self.temp_f = ((int(lookup.condition().temp()) * (9 / 5)) + 32)
        self.forecast = {}
        for item in lookup.forecast():
            fdate = datetime.strptime(item.date(), "%d %b %Y").date().isoformat()
            self.forecast[fdate] = {
                'low': item.low(),
                'high': item.high(),
                'description': item.text()
            }
        del lookup
        del weather

    def __getLocation(self, location_arg):
        if location_arg:
            return location_arg
        location_key = os.environ.get(__location_environment_variable__)
        if not location_key:
            err = []
            err.append("Error, environment variable '{}' is not set".format(__location_environment_variable__))
            err.append("You need to specify a WOEID, it can be found here:")
            err.append("http://weather.yahoo.com")
            raise Exception("\n".join(err))
        return location_key

    def reload_status(self):
        self.__init__()

    def get_json(self):
        rv = {}
        rv['title'] = self.title
        rv['units'] = self.units
        rv['build_date'] = self.build_date.isoformat()
        rv['sunset'] = self.sunset
        rv['wind'] = self.wind
        rv['atmosphere'] = self.atmosphere
        rv['description'] = self.description
        rv['temp'] = self.temp
        rv['temp_f'] = self.temp_f
        rv['forecast'] = self.forecast
        return json.dumps(rv)
