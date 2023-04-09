#! /usr/bin/env python3
"""
Module containing the nucleo class

authors: A.Hauswald C.Vernant
date: 2023-09-04

"""
import serial


class Nucleo:
    """
    Class representing a nucleo

    self.serial: serial object
    self.serial_port: serial port
    self.baudrate: baudrate
    """

    def __init__(self, serial_port, baudrate):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.serial = serial.Serial(self.serial_port, self.baudrate)

    def send_command(self, command):
        """
        Send a command in hexadecimal to the nucleo through the serial port

        :param command: command to send
        """
        hex_command = bytearray(command)
        self.serial.write(hex_command)

    def read_serial(self):
        """
        Read the serial port

        :return: response
        """
        response = self.serial.read_all()
        return response
