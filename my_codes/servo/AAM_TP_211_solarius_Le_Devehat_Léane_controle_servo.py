#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:32:27 2021

@author: leaneledevehat
"""


import time
from adafruit_servokit import Servokit

kit = ServoKit(channels=8)

kit.servo[0].angle = 0

if kit.servo[0].angle < 180:
    time.sleep(0.5)
    kit.servo[0].angle += 1
    kit.continuous_servo[0].throttle = 1
else:
	kit.servo[0].angle = 0

kit.servo[1].angle = 90
if kit.servo[1].angle < 180:
    time.sleep(0.5)
    kit.servo[0].angle += 1
    kit.continuous_servo[1].throttle = -1
else:
    kit.servo[1].angle = 90
