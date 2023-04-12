import json

import leg
import linear_actuator
import motor
import nucleo
from typing import List, Dict, Union
with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # type: Dict[str, Union[List[str], int, str]]

# Init the final structure
megabot = []  # type: List[leg.Leg]

# Iterate through the nucleos names
for nucleos in data.values():

    # Creating a Nucleo object for each nucleo
    nucleo_object = nucleo.Nucleo(nucleos["port"], nucleos["baudrate"])

    # Iterate through each keys for a given nucleo
    for keys in nucleos.keys():
        if str(keys).startswith("leg"):
            linear_actuators = []   # type: List[linear_actuator.LinearActuator]
            leg_name = str(keys)

            # Iterate through each motor for a given leg
            for linear_actuator_name in nucleos[keys]:

                # Creating a Motor object for each linear actuator
                motor_object = motor.Motor(
                    nucleo_object, str(leg_name), str(linear_actuator_name)
                )

                # Creating a LinearActuator object based on the Motor object created
                linear_actuators.append(linear_actuator.LinearActuator(motor_object))

            # Adding the leg object to the final structure
            megabot.append(
                leg.Leg(linear_actuators[0], linear_actuators[1], linear_actuators[2])
            )

"""
    Example of use of the megabot class  
    
    megabot[0].motor2.go_to(100.5) 
    megabot[0].motor1.motor.nucleo.read_serial()
    
"""
megabot[0].motor2.go_to(100.5)
megabot[0].motor1.motor.nucleo.read_serial()
