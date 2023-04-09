#! /usr/bin/env python3

class Motor:
    """
    Class representing a motor

    """

    def __init__(self, nucleo, leg, motor):
        self.nucleo = nucleo
        self.leg = leg
        self.motor = motor

    def go_to_serialized(self, float_position):
        """
        Send a command to the motor to go to the given position through the serial port

        :param float_position: position to go to
        """
        self.nucleo.send_command([self.leg, self.motor, float_position])