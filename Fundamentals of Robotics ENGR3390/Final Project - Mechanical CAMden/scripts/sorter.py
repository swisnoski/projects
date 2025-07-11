from hiwonder import HiwonderRobot
import numpy as np
from time import sleep

from camera_cv import get_coordinates
from arm_models import FiveDOFRobot

robot = HiwonderRobot()

def main():
    while True: 
        print("Moving to Home")
        robot.move_to_home_position()
        sleep(1)

        print("Getting Coords")
        x, y, z, block_color = get_coordinates()
        sleep(1)

        print("Moving Above")
        robot.go_to_position_high([x,y])
        sleep(1)

        print("Moving On")
        theta = robot.go_to_position_low([x,y])
        sleep(1)

        print("Closing")
        robot.close(theta)
        sleep(2)

        print("Sorting")
        theta = robot.sort(block_color)
        sleep(1)

        print("Opening")
        robot.open(theta)
        sleep(2)

if __name__ == "__main__":
    main()