from turtleRobot import TurtleRobot

if __name__ == '__main__':
    TIME_STEP = 64

    # create the Robot instance.
    robot = TurtleRobot(TIME_STEP)
    robot.track_object('rubber duck')
    robot.start_mission()