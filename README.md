# HomeAutomation
The beginnings of my homeautomation

**Update** 2018-04-07 - shortly after I started this I found [home-assistant](https://www.home-assistant.io/), which runs on a RasPi and does a whole lot more than I originally imagined so I'll be mostly using HA and this repo will become my drop point for custom scripts and automations. You can read more on my personal site, [ryanmiguel.com](https://ryanmiguel.com/).

## Classes
### quickweather
A wrapper class for weather-api to make it refreshable and easier to interact with.

## Scripts
* [toggle-gpio-pin](bin/toggle-gpio-pin.py) - toggle a RasPi GPIO pin like a momentary switch w/ given time delay acting as the activation time.
* [determine-rain-delay](bin/determine-rain-delay.py) - use quickweather to determine if we need to set a rain delay

#### Special Thanks
* [shollingsworth](https://github.com/shollingsworth) - I used your work/examples/scripts for packaging
