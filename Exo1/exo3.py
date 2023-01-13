from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(classmeta=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """

    pass

class AerialVehicle(classmeta=ABCMeta):
    """ A vehicle made for ground fields."""
    
    @abstractmethod
    def fly(self):
        print('Now in the sky')

    @abstractmethod
    def land(self):
        print('Landed with success')

    def start_mission(self, mission):
        print('Aerial mission start :', mission)
        self.fly()

    def stop_mission(self):
        print('Aerial mission stop.')
        self.land()

    def status(self):
        print('Unmanned Aerial Vehicle')


class GroundVehicle(classmeta=ABCMeta):

    """ A vehicle made for ground fields."""
    @abstractmethod
    def move(self, forward=True):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass


class UnderseaVehicle(classmeta=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def dive(self):
        pass

    @abstractmethod
    def surface(self):
        pass

    @abstractmethod
    def status(self):
        pass

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def fly(self):
        print('Now in the sky')

    def land(self):
        print('Landed with success')

    def start_mission(self, mission):
        print('Aerial mission start :', mission)
        self.fly()

    def stop_mission(self):
        print('Aerial mission stop.')
        self.land()

    def status(self):
        print('Unmanned Aerial Vehicle')
        

class UUV():
    """Unmanned Undersea Vehicle"""
    pass

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    



if __name__ == '__main__':

    uav = UAV()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()

    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()