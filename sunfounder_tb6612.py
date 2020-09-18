#!/usr/bin/env python
'''
**********************************************************************
* Filename    : TB6612.py
* Description : A driver module for TB6612
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-23    New release
*               LDG      2020-09-18
**********************************************************************
'''
import RPi.GPIO

def _map(x, in_min, in_max, out_min, out_max):
    '''To map the value from one range to another'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class TBMotors():
    '''Lazy creation and caching of motor objects. Treated as a sequence.'''
    
    def __init__(self, tb66xx):
        self._tb66xx = tb66xx;
        self._motors = [None] * len(self);
        pass

    def __len__(self):
        return 2;
    
    def __getitem__(self, index):
        if not(self._motors[index]):
            mxgpio_pin = self._tb66xx.mxgpio_pins[index];
            pwmx_out = self._tb66xx.pwmx_out[index];
            self._motors[index] = Motor(mxgpio_pin, pwmx_out);
        return self._motors[index];

class TB6612():
    ''' Initialise the TB6612 chip '''
    _MOTOR_A = 0;
    _MOTOR_B = 1;
    
    def __init__(self, ma_pin, mb_pin, pwma_out, pwmb_out):
        ''' TB6612 class
            :param int ma_pin: Motor A direction ~Rpi.GPIO pin id
            :param int mb_pin: Motor B direction GPIO pin id
            :param ~pulseio.PWMOut pwma_out: PWM output object for Motor A
            :param ~pulseio.PWMOut pwmb_out: PWM output object for Motor B
        '''
        self.mxgpio_pins = [ma_pin, mb_pin];
        self.pwmx_out = [pwma_out, pwmb_out];
        self.motors = TBMotors(self);
    
    @property
    def motor_a(self):
        ''' Motor A object '''
        return self.motors[self._MOTOR_A];
    
    @property
    def motor_b(self):
        ''' Motor B object '''
        return self.motors[self._MOTOR_B];

class Motor():
    ''' Motor driver class '''
    def __init__(self, gpio_pin=None, pwm=None, offset=False):
        '''Init a motor on giving dir. ~Rpi.GPIO pin and ~pulseio.PWMOut PWM channel.'''
        # config GPIO env
        RPi.GPIO.setwarnings(False)
        RPi.GPIO.setmode(RPi.GPIO.BCM);
        # config GPIO output pin
        self._gpio_pin = gpio_pin;
        RPi.GPIO.setup(self._gpio_pin, RPi.GPIO.OUT);
        
        self._pwm = pwm;
        
        self._forward_offset = offset
        self._backward_offset = not self._forward_offset
        self._speed = 0

# 		self._debug_('setup motor direction channel at %s' % direction_channel)
# 		self._debug_('setup motor pwm channel')# self._debug_('setup motor pwm channel as %s ' % self._pwm.__name__)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        RPi.GPIO.cleanup(self._gpio_pin);

    @property
    def offset(self):
        ''' Return offset value '''
        return self._forward_offset;

    @offset.setter
    def offset(self, value):
        ''' Set offset for motor direction '''
        if value not in (True, False):
            raise ValueError('offset value must be Boolean value, not "{}"'.format(value))
        self._forward_offset = value
        self._backward_offset = not self._forward_offset
# 		self._debug_('Set offset to %d' % self._offset)

    @property
    def speed(self):
        ''' Return speed value '''
        return self._speed

    @speed.setter
    def speed(self, speed):
        ''' Set Speed with giving value '''
        if speed < 0 or speed > 100:
            raise ValueError('speed ranges fron 0 to 100, not "{}"'.format(speed))
        self._speed = speed;
        pulse_width = int(_map(self._speed, 0, 100, 0x0000, 0xFFFF));
        self._pwm.duty_cycle = pulse_width;

    def forward(self):
        ''' Set the motor direction to forward '''
        RPi.GPIO.output(self._gpio_pin, self._forward_offset)
        self.speed = self._speed
        # self._debug_('Motor moving forward (%s)' % str(self.forward_offset))

    def backward(self):
        ''' Set the motor direction to backward '''
        RPi.GPIO.output(self._gpio_pin, self._backward_offset)
        self.speed = self._speed;
# 		self._debug_('Motor moving backward (%s)' % str(self.backward_offset))

    def stop(self):
        ''' Stop the motor by giving a 0 speed '''
        self.speed = 0
# 		self._debug_('Motor stop')


if __name__ == '__main__':
# 	test()
    print('under development');
