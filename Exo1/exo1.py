import time
ROBOT_COUNT = 0

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
      
    """
      Give your best code here ( •̀ ω •́ )✧
    """
	
    # Constructor
    def __init__(self, name=None):
        if name:
            self.__name = name
        self.__current_status = self.__states[0]
        self.__power = False
        global ROBOT_COUNT
        ROBOT_COUNT += 1

    # Destructor
    def __del__(self):
        print("%s Auto destruction NOW"%(self.__name))
        global ROBOT_COUNT
        ROBOT_COUNT -= 1
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def battery_level(self):
        return self.__battery_level
    
    @property
    def current_status(self):
        return self.__current_status

    def boot(self):
    # Do someting to boot
        self.power = True
        current_speed = 0
        self.states = 'running'

    def shutdown(self):   
        self.__power = False
        self.__current_status = self.__states[0]
        self.__current_speed = 0

    def charge(self):
        print('Charging battery...')
        

    def status(self):
        print("%s status : %s [%s%% battery]"%(self.name, self.__current_status, self.battery_level)) 
    
    def stop(self):
        self.__current_speed=0

    def move(self,speed):
        if type(speed)==int:
            self.__current_speed = speed

    def speed(self):
        return self.__current_speed

    def __str__(self): # must return a string
        return "Robot %s [state: %s current speed : %s battery_level : %s ]"%(self.name, self.states,self.speed, self.__battery_level)
  
    #def __repr__(self): # must return a string
     #   return str({"name":self.name, "size":self.size})

if __name__ == '__main__':
  r = Robot()
  r.name = "Termonator"
  r.move(100)
  r.charge()
  print(r.status)
  print(r.name + "\nSpeed:", r.speed())
  r = Robot(name="Robotnik")
  r.status()
  r.boot()
  r.status()
  r.charge()
  r.shutdown()
  r.status()
  str(r)

  print("\nEncore encore !")
  r.status()
  r.boot()
  r.status()
  r.charge()
  r.shutdown()
  r.status()

