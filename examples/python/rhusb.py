#!/usr/bin/python
# Author: Jon Trulson <jtrulson@ics.com>
# Copyright (c) 2016 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time, sys, signal, atexit
import pyupm_rhusb as sensorObj

## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This function lets you run code on exit
def exitHandler():
	print "Exiting..."
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

defaultDev = "/dev/ttyUSB0"

# if an argument was specified, use it as the device instead
if (len(sys.argv) > 1):
        defaultDev = sys.argv[1]

print "Using device", defaultDev
print "Initializing..."

# Instantiate an RHUSB instance on defaultDev
sensor = sensorObj.RHUSB(defaultDev)

# output the firmware ID
print "Firmware ID:", sensor.getFirmwareID()
print

# update and print available values every second
while (1):
        # update our values from the sensor
        sensor.update()

        # we show both C and F for temperature
        print "Temperature:", sensor.getTemperature(), "C /",
        print sensor.getTemperature(True), "F"

        print "Humidity:", sensor.getHumidity(), "%"

        print
	time.sleep(1)
