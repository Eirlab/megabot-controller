import json
import leg
import linear_actuator
import motor
import nucleo

with open("config.json", "r", encoding="utf-8") as file:
    data = json.load(file)

megabot = []

for nucleos in data.values():
    nucleo_object = nucleo.Nucleo(nucleos["port"], nucleos["baudrate"])
    for keys in nucleos.keys():
        if str(keys).startswith("leg"):
            linear_actuators = []
            for linear_actuator_object in nucleos[keys]:
                motor_object = motor.Motor(
                    nucleo_object, str(keys), str(linear_actuator_object)
                )
                linear_actuators.append(linear_actuator.LinearActuator(motor_object))

            megabot.append(
                leg.Leg(linear_actuators[0], linear_actuators[1], linear_actuators[2])
            )

print(megabot[0].motor1.motor)