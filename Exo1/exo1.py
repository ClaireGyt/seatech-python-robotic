import time
ROBOT_COUNT = 0

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
      
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
        self.power = True
        self.__current_status = self.__states[1]
        self.__current_speed = 0

    def shutdown(self):   
        self.power = False
        self.__current_status = self.__states[0]
        self.__current_speed = 0   

    def charge(self):
        print('Charging battery...')
        while self.__battery_level < 100:
            self.__battery_level += 20
            print("Charge is %s%%"%(self.battery_level))
            time.sleep(1)

    def status(self):
        print("%s Status: %s [%s%% Battery]"%(self.name, self.current_status, self.battery_level)) 
    
    def stop(self):
        self.__current_speed=0

    def move(self,speed):
        if self.current_status=='running' :
            if self.battery_level>0:
                if type(speed)==int:
                    self.__current_speed = speed
                else:
                    print("Speed isn't a int ")
            else:
                print("Please charge your robot ")
        else:
            print("You need to boot your robot ")

    def speed(self):
        return self.__current_speed
    
    def __str__(self): # must return a string
        return "Robot %s [State: %s Current Speed : %s km/h Battery Level : %s ]"%(self.name, self.__current_status, self.__current_speed, self.__battery_level)
    
if __name__ == '__main__':
  r = Robot()
  r.name = "Wally"
  r.move(100)
  r.boot()
  r.move(100)
  r.charge()
  r.move(100)
  print(r.name + "'s speed:", r.speed())
  r.stop()
  print(r.name + "'s speed:", r.speed())
  r.shutdown()
  r.boot()


  r = Robot(name="Terminator")
  r.status()
  r.boot()
  r.status()
  r.charge()
  r.shutdown()
  r.status()
  print(r)
  

  

