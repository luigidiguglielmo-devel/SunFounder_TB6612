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
import busio
from adafruit_pca9685 import PCA9685
from sunfounder_tb6612 import TB6612, Motor

board_pins = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9,
	board.D10, board.D11, board.D12, board.D13, board.D14, board.D15, board.D16, board.D17, board.D18, board.D19,
	board.D20, board.D21, board.D22, board.D23, board.D24, board.D25, board.D26, board.D27];

def header(ma, mb, pwma, pwmb):
	print('********************************************')
	print('*                                          *')
	print('*           SunFounder TB6612              *')
	print('*                                          *')
	print('*          Connect MA to BCM-{}            *'.format(ma))
	print('*          Connect MB to BCM-{}            *'.format(mb))
	print('*     Connect PWMA to BCM/Channel-{}       *'.format(pwma))
	print('*     Connect PWMB to BCM/Channel-{}       *'.format(pwmb))
	print('*                                          *')
	print('********************************************')

def init_gpio(ma, mb, pwma, pwmb):
	import pulseio
	# print header	
	header(ma, mb, pwma, pwmb)

	# GPIO setup
	pwma_o = pulseio.PWMOut(board_pins[pwma], frequency=60);
	pwmb_o = pulseio.PWMOut(board_pins[pwmb], frequency=60);

	return ma, mb, pwma_o, pwmb_o;


def init_pwm(ma, mb, pwma, pwmb):
	# print header	
	header(ma, mb, pwma, pwmb)

	i2c_bus = busio.I2C(board.SCL, board.SDA)
	pca = PCA9685(i2c_bus)
	pca.frequency = 60;

	pwma_o = pca.channels[pwma];
	pwmb_o = pca.channels[pwmb];

	return ma, mb, pwma_o, pwmb_o;

def test_motor(gpio_a, gpio_b, pwma, pwmb):	
	tb66xx = TB6612(gpio_a, gpio_b, pwma, pwmb);
	motorA = tb66xx.motor_a;
	motorA.offset = False;
	print('mA.pwma.dc={}'.format(pwma.duty_cycle));
	print('mA.motor.speed={}'.format(motorA.speed));
	motorB = tb66xx.motor_b;
	print('mB.pwma.dc={}'.format(pwma.duty_cycle));
	print('mB.motor.speed={}'.format(motorB.speed));

	#motorA.debug = True
	#motorB.debug = True
	delay = 0.05

	motorA.forward()
	#pwma.duty_cycle = 80000
	#time.sleep(1);
	#pwma.duty_cycle = 0
	#quit();
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


def usage():
    print('Usage:  test [Command] [index]')
    print('Commands:')
    print('\tmotor-gpio [ma_pin mb_pin pwma_pin pwmb_pin]\t\tTest motors connected to software-based PWM')
    print('\tmotor-pca  [ma_pin mb_pin pwma_chn pwmb_chn]\t\tTest motors connected to PWM controller')
    quit()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'motor-gpio':
            ma = 17;
            mb = 27;
            pwma = 19;
            pwmb = 26;
            gpio_a, gpio_b, pwma_o, pwmb_o = init_gpio(ma, mb, pwma, pwmb);
            test_motor(gpio_a, gpio_b, pwma_o, pwmb_o);
        elif sys.argv[1] == 'motor-pca':
            ma = 17;
            mb = 27;
            pwma = 5;
            pwmb = 4;
            gpio_a, gpio_b, pwma_o, pwmb_o = init_pwm(ma, mb, pwma, pwmb);
            test_motor(gpio_a, gpio_b, pwma_o, pwmb_o);
        else:
            print('Command error, "{}" is not in list'.format(sys.argv[1]));
            usage();
    else:
        usage();

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()
