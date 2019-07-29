
import sys
import time

def pause():
    time.sleep(0.5)

class Player:

    x = None
    y = None
    max_health = 16
    health = None

    lastHealth = None

    heart = u"\U0001F49C"
    death = u"\U0001F480"

    '''
    Player constructor, gets the map instance as input to place
    it on the map
    '''
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.setPosition(x,y)
        map.set(self.getX(), self.getY(), self.toString())
        self.health = self.max_health
        self.lastHealth = self.max_health


    def toString(self):
        return 'P'

    '''
    Setter and Getter Functions
    '''

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def getHealth(self):
        return int(self.health)

    def damage(self, value):
        self.health -= value

    '''
    Attacks a alien if he exists at the coordinates
    returns True if the attack was a success
    returns False if it failed
    '''
    def attack(self,x,y, map):
        if map.map[y][x] == '[A]':
            print('Attack will be executed')
            for alien in map.getAliens():
                if alien.getX() == int(x) and alien.getY() == int(y):
                    alien.kill(map)
                    return True
        else:
            print('No alien at this coordinates!')
            return False

    def print_healt(self):
        output = '['
        for i in range(self.max_health):
            if int(self.health) > int(i):
                output += self.heart + ' '
            else:
                output += self.death + ' '
        output += ']'
        print(output)


    def print_healt_fade(self):
        for j in range(self.lastHealth - self.health):
            output = '['
            for i in range(self.max_health):
                if int(self.lastHealth) > int(i):
                    output += self.heart + ' '
                else:
                    output += self.death + ' '
            output += ']'
            sys.stdout.write('\r'+output)
            sys.stdout.flush()
            self.lastHealth -= 1
            pause()
