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
**********************************************************************
'''
import sys
import time
import board
import pulseio
import busio
from sunfounder_tb6612 import TB6612, Motor

# PIN selection
gpio_a, gpio_b= (17, 27);
pwma, pwmb = (19, 26);

print('********************************************')
print('*                                          *')
print('*           SunFounder TB6612              *')
print('*                                          *')
print('*          Connect MA to BCM-{}            *'.format(gpio_a))
print('*          Connect MB to BCM-{}            *'.format(gpio_b))
print('*         Connect PWMA to BCM-{}           *'.format(pwma))
print('*         Connect PWMB to BCM-{}           *'.format(pwmb))
print('*                                          *')
print('********************************************')


board_pins = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9,
	board.D10, board.D11, board.D12, board.D13, board.D14, board.D15, board.D16, board.D17, board.D18, board.D19,
	board.D20, board.D21, board.D22, board.D23, board.D24, board.D25, board.D26, board.D27];

# GPIO setup
pwma_o = pulseio.PWMOut(board_pins[pwma], frequency=60);
pwmb_o = pulseio.PWMOut(board_pins[pwmb], frequency=60);

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

