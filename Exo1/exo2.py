from exo1 import Robot
import time
import sys


HUMAN_COUNT = 0
class Human():   
    __sexe = None
    __stomac_content = []

    def __init__(self, sexe=None):
        if sexe:
            self.__sexe = sexe
        global HUMAN_COUNT
        HUMAN_COUNT += 1
        
    @property   
    def sexe(self):
        return self.__sexe
    
    def eat(self, food):   
        if type(food) is str:
            food = [food]
        self.__stomac_content += food
        print('Miam  ', ' and '.join(food))

    def digest(self):   
        while len(self.__stomac_content):
            print('Digest ', self.__stomac_content.pop(), '...')
            time.sleep(1)

        print('*grrl grrl grl are coming from belly...*')
    
    def __str__(self): # must return a string
        return 'Hi from Human %s [%s] !'%(self.name, self.sexe)
        


class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        
    
    def sing(self):
        print(" ------ ")
        print("| @  @ |    🎵 🎵")
        print("|  []  |  🎵  🎵 🎵 🎵 🎵")
        print(" ------ ")

        print(" ------ ")
        print("| @  @ |    🎵 🎵")
        print("|   ~  |  🎵  🎵 🎵 🎵 🎵")
        print(" ------ ")

        print(" ------ ")
        print("| @  @ |    🎵 🎵")
        print("|   0  |  🎵  🎵 🎵 🎵 🎵")
        print(" ------ ")

    def __str__(self): # must return a string
        #super().__init__(name, 'surface')
        return 'Hi from Cyborg %s [%s] !'%(self.name, self.sexe)
        #print('Hi from Cyborg %s [%s] !'%(self.name, self.sexe))

if __name__ == '__main__':


    h=Human(sexe='M')
    print( 'sexe', h.sexe)

    cyborg = Cyborg('Deux Ex Machina', 'M')

    #print(cyborg.name, 'sexe', cyborg.sexe)
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['water', 'pineaple'])
    cyborg.digest()
    cyborg.sing()
    