#!/usr/bin/env python
'''
**********************************************************************
* Filename    : speed_increase.py
* Description : a test script for SunFounder_TB6612 module
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-23    New release
*               LDG      2020-09-18
**********************************************************************
'''
import time
import board
import busio
from adafruit_pca9685 import PCA9685
from sunfounder_tb6612 import TB6612

# PIN selection
gpio_a, gpio_b= (17, 27);
pwma, pwmb = (5, 4);

print('********************************************')
print('*                                          *')
print('*           SunFounder TB6612              *')
print('*                                          *')
print('*          Connect MA to BCM-{}            *'.format(gpio_a))
print('*          Connect MB to BCM-{}            *'.format(gpio_b))
print('*     Connect PWMA to PWM Channel-{}       *'.format(pwma))
print('*     Connect PWMB to PWM Channel-{}       *'.format(pwmb))
print('*                                          *')
print('********************************************')

i2c_bus = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 60;

pwma_o = pca.channels[pwma];
pwmb_o = pca.channels[pwmb];

# TB6612 setup
tb66xx = TB6612(gpio_a, gpio_b, pwma_o, pwmb_o);

motorA = tb66xx.motor_a;
motorA.offset = False;
motorB = tb66xx.motor_b;
motorB.offset = False;
delay = 0.05

# TEST MOTOR A FORWARD/BACKWARD
print('Motor A: moving forward')
motorA.forward()
for i in range(0, 101):
	motorA.speed = i
	time.sleep(delay)

for i in range(100, -1, -1):
	motorA.speed = i
	time.sleep(delay)

print('Motor A: moving backward')
motorA.backward()
for i in range(0, 101):
	motorA.speed = i
	time.sleep(delay)
for i in range(100, -1, -1):
	motorA.speed = i
	time.sleep(delay)

# TEST MOTOR B FORWARD/BACKWARD
print('Motor B: moving forward')
motorB.forward()
for i in range(0, 101):
	motorB.speed = i
	time.sleep(delay)
for i in range(100, -1, -1):
	motorB.speed = i
	time.sleep(delay)

print('Motor B: moving backward')
motorB.backward()
for i in range(0, 101):
	motorB.speed = i
	time.sleep(delay)
for i in range(100, -1, -1):
	motorB.speed = i
	time.sleep(delay)

# STOP MOTORs
motorA.stop()
motorB.stop()

pca.deinit();
