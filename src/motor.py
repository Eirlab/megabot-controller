#! /usr/bin/env python3
"""
Module containing the motor class

authors: A.Hauswald C.Vernant
date: 2023-09-04
"""


class Motor:
    """
    Class representing a motor

    self.nucleo: nucleo object
    self.leg: leg number
    self.motor: motor number

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

    def __str__(self):
        return self.motor
