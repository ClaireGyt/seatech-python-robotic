"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
#class SmashRobot(Robot):
   # def _init(_self,speed=None):
    #super().__init__():
    #self.__front_left_wheel_joint(
    
from math import copysign
from controller import Motor

class TurtleMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf')) # set rotation infinite (radian), will move forward by default
        self.setVelocity(0) # do not give a speed to the infinite rotation by default to hold position

class TurtleMotors():
    def __init__(self):
        self.left_motor = TurtleMotor('left wheel motor')
        self.right_motor = TurtleMotor('right wheel motor')

    def run(self, speed=None, left=False, right=False):
        """Run forward or backward but never over Epuck max speed"""
        max_speed = self.get_max_speed()
        if speed is None: # half speed by default
            speed = max_speed / 2
        if abs(speed) > abs(max_speed): # not more than max speed
            speed = copysign(max_speed, speed)
        
        left_speed = speed
        right_speed = speed
        # print(speed, left, right)
        if left:
            left_speed = 0
        elif right:
            right_speed = 0
        
        # run motors
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)

    def turn_left(self, capacity=1):
        self.left_motor.setVelocity(0)
        self.right_motor.setVelocity(self.get_max_speed()*capacity)

    def turn_right(self, capacity=1):
        self.left_motor.setVelocity(self.get_max_speed()*capacity)
        self.right_motor.setVelocity(0)


    def get_max_speed(self):
        """Max speed of the two wheels, divided by 2"""
        return (self.left_motor.getMaxVelocity() + self.right_motor.getMaxVelocity())/2

