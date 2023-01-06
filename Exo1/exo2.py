from exo1 import Robot
import time

class Robot():
    @staticmethod
    def create_simple_robot():
        return Robot()

HUMAN_COUNT = 0
class Human():   
    __sexe='"<undefined>"'
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
        print('Miam, delicious ', ' and '.join(food))

    def digest(self):   
        while len(self.__stomac_content):
            print('Digest ', self.__stomac_content.pop(), '...')
            time.sleep(1)

        print('*Glouglouglouglou noises are coming from belly...*')

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
    
    #def fun(self):


    # if __name__ == '__main__':
    #     cyborg = Cyborg('Deux Ex Machina', 'M')

    #     print(cyborg.name, 'sexe', cyborg.sexe)
    #     print('Charging battery...')
    #     cyborg.charge()
    #     cyborg.status()
    #     cyborg.eat('banana')
    #     cyborg.eat(['coca', 'chips'])
    #     cyborg.digest()
    
if __name__ == '__main__':
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    