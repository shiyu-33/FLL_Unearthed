from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

LLM = Motor(Port.D, Direction.COUNTERCLOCKWISE)
RLM = Motor(Port.F, Direction.CLOCKWISE)
Robot = DriveBase(LLM, RLM, 56, 116)

#Robot.settings(800)
#Robot.arc(150, angle=170)
async def main():
    await multitask(
LLM.run_angle(speed=500,rotation_angle=180),
RLM.run_angle(speed=500,rotation_angle=180))

run_task(main())