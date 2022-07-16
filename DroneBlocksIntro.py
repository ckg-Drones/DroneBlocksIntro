#!pip install droneblocks-python-utils

from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

tello = DroneBlocksTello()

tello.connect()

print(tello.get_battery())

tello.takeoff()

tello.rotate_clockwise(90)
time.sleep(5)
tello.land() 
