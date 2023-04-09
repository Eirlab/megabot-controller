import json
import motor as m
import nucleo as n
import linear_actuator as la
import leg as l

with open('config.json', 'r') as file:
    data = json.load(file)

megabot = []

for nucleo in data.values():
    for leg in nucleo.values():
        linear_actuators = []

        for linear_actuator in leg.values():
            nucleo = n.Nucleo(linear_actuator['port'], linear_actuator['baudrate'])
            motor = m.Motor(nucleo,str(leg),str(linear_actuator))
            linear_actuators.append(la.LinearActuator(motor))

        megabot.append(l.Leg(linear_actuators[0], linear_actuators[1], linear_actuators[2]))
