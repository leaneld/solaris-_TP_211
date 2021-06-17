#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:34:29 2021

@author: leaneledevehat
"""

import time
from adafruit_circuitplayground.express import cpx
from adafruit_servokit import Servokit
import simpleio

int LDR = downright
int LDL = downleft
int LTR = topright
int LTL = topleft

def changing_angle(angle_180, angle_90):
   if (topleft > topright):
           servo[1] = angle_180 + 1
           time.sleep(0.5)
   if (topleft < topright):
           servo[1] = angle_180 - 1
           time.sleep(0.5)
   if (downleft > downright):
           servo[1] = angle_180 + 1
           time.sleep(0.5)
   if (downleft < downright):
           servo[1] = angle_180 - 1
           time.sleep(0.5)
   if (topleft > downleft):
           servo[2] = angle_180 - 1
           time.sleep(0.5)
   if (topleft < downleft):
           servo[2] = angle_180 + 1
           time.sleep(0.5)
   if (topright > downright):
           servo[2] = angle_180 - 1
           time.sleep(0.5)
   if (topright < downright):
           servo[2] = angle_180 + 1
           time.sleep(0.5)
   kit.servo[1].angle = angle_180
   kit.servo[2].angle = angle_90
   kit
   return angle_90, angle_180


cpx.pixels.auto_write = False
cpx.pixels.brightness = 1

while True:
    peak = simpleio.map_range(cpx.light, 0, 320, 0, 10)
    print(cpx.light)
    print(int(peak))

    for i in range(0, 10, 1):
        if i <= peak:
            cpx.pixels[i] = (0, 255, 255)
            changing_angle_1(angle_90)
            changing_angle_1(angle_180)
            changing_angle_2(angle_90)
        else:
            cpx.pixels[i] = (0, 0, 0)
    cpx.pixels.show()
    time.sleep(0.05)
