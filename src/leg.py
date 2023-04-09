#! /usr/bin/env python3


class Leg:
    """
    Class representing a leg

    """

    def __init__(self, motor1, motor2, motor3):
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.la_list = [self.motor1, self.motor2, self.motor3]
