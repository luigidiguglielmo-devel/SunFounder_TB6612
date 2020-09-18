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

import time
import board
import pulseio
import sunfounder_tb6612 as tb6612

def header():
	print("********************************************")
	print("*                                          *")
	print("*           SunFounder TB6612              *")
	print("*                                          *")
	print("*          Connect MA to BCM27             *")
	print("*          Connect MB to BCM22             *")
	print("*         Connect PWMA to BCM19            *")
	print("*         Connect PWMB to BCM26            *")
	print("*                                          *")
	print("********************************************")

def test_tb6612():

	#print header
	header();

	# GPIO setup
	gpio_a = 27;
	gpio_b = 22;
	# PWM setup
	pwma = pulseio.PWMOut(board.D19, frequency=50);
	pwmb = pulseio.PWMOut(board.D26, frequency=50);


	tb66xx = tb6612.TB6612(gpio_a, gpio_b, pwma, pwmb);
	
	motorA = tb66xx.motor_a;
	motorB = tb66xx.motor_b;

	#motorA.debug = True
	#motorB.debug = True
	delay = 0.05

	motorA.forward()
	for i in range(0, 101):
		motorA.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorA.speed = i
		time.sleep(delay)

	motorA.backward()
	for i in range(0, 101):
		motorA.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorA.speed = i
		time.sleep(delay)

	motorB.forward()
	for i in range(0, 101):
		motorB.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorB.speed = i
		time.sleep(delay)

	motorB.backward()
	for i in range(0, 101):
		motorB.speed = i
		time.sleep(delay)
	for i in range(100, -1, -1):
		motorB.speed = i
		time.sleep(delay)

	motorA.stop()
	motorB.stop()

if __name__ == '__main__':
	try:
		test_tb6612()
	except KeyboardInterrupt:
		destroy()
