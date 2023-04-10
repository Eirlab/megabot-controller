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
        command_int_list=[]
        leg = int(command[0][4])+48
        motor = int(command[1][6])+48
        command_int_list.append(leg)
        command_int_list.append(motor)
        for c in str(command[2]):
            if c != ".":
                if c == "0":
                    command_int_list.append(48)
                    
                else :
                    command_int_list.append(int(c)+48)
            else:
                command_int_list.append(46)
        hex_command = bytearray(command_int_list)
        hex_command.append(0x7e)
        
        print("sent: ",hex_command)
        self.serial.write(hex_command)
        #command=[0x55,0x3a,0x56,0x3a,0x30,0x31,0x32,0x33,0x3a,0x30,0x31,0x32,0x33,0x7e]
        #self.serial.write(bytearray(command))

    def read_serial(self):
        """
        Read the serial port

        :return: response
        """
        response = self.serial.read_all()
        print("received: ", response.decode())
        return response
