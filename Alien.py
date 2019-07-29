import time

def pause():
    time.sleep(0.5)

class Alien:

    x = None
    y = None
    alive = None
    symbol = 'A'


    '''
    Alien constructor, gets the map instance as input to place
    it on the map
    '''
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        alive = True
        self.setPosition(x,y)
        map.set(self.getX(), self.getY(), self.toString())

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return self.symbol

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    '''
    Calculates the distance between alien and player
    '''
    def distance(self, alien, player):
        return abs(alien.getX()-player.getX())+abs(alien.getY()- player.getY())

    '''
    Kills the alien and displays an X
    '''
    def kill(self, map):
        self.alive= False
        self.symbol = 'X'
        map.set(self.x, self.y, self.symbol)

    '''
    Attacks a player if he exists at the coordinates
    returns True if the attack was a success
    returns False if it failed
    '''
    def attack(self,x,y, map):
        if map.map[y][x] == '[P]':
            map.getPlayer().damage(1)
            print('Alien at ('+ str(self.x) +'|'+str(self.y)+ ') damaged the player!')
            pause()
            return True
        else:
            print('No player at this coordinates!')
            return False
