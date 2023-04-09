#! /usr/bin/env python3
"""
Module containing the linear actuator class

authors: A.Hauswald C.Vernant
date: 2023-09-04
"""

class LinearActuator:
    """
    Class representing a linear actuator
    
    self.motor: motor object
    """
    def __init__(self, motor):
        self.motor = motor

    def go_to(self, float_position):
        """
        Send a command to the motor to go to the given position
        
        :param float_position: position to go to
        """
        self.motor.go_to_serialized(float_position)
