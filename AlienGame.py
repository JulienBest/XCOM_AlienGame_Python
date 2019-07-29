import sys
import os
import time
from Map import Map

def clear():
    os.system("clear")

def seperate_but_equal():
    print('-----------------------------------')

def pause():
    time.sleep(0.5)


class AlienGame:

    height = None
    width = None
    alienCount = None
    gameOver = False
    map = None

    lastHits = None


    def __init__(self):
        #Argumente einlesen
        if len(sys.argv) < 4:
            print('Input width, height and alien count as arguments')
        else:
            self.width  = int(sys.argv[1])
            self.height = int(sys.argv[2])
            self.alienCount = int(sys.argv[3])

            if self.height * self.width < self.alienCount:
                print('Feld zu klein')
            else:
                self.play()



    '''
    Main play method
    '''
    def play(self):
        clear()
        #Initialisierung und Einlesung
        map = Map(self.height, self.width, self.alienCount)
        #Game schleife
        while not self.gameOver:
            lastHits = 0
            print('Input x to attack an Alien')
            x = int(input())+1
            print('Input y to attack an Alien')
            y = int(input())+1
            clear()
            #Player attack
            if y > self.height or x > self.width:
                print('Attack failed. Input out of map')
            else:
                if map.getPlayer().attack(x,y,map):
                    clear()
                    print('The attack killed the alien')
            #Alien attacks
            map.print_map()
            seperate_but_equal()
            for alien in map.getAliens():
                if alien.attack(
                map.getPlayer().getX(), map.getPlayer().getY(), map):
                    lastHits += 1
            seperate_but_equal()
            if int(map.getPlayer().getHealth()) < 1:
                print('Game Over!')
                seperate_but_equal()
                break
            map.getPlayer().print_healt_fade()
            print('\nThe player has '+ str(map.getPlayer().getHealth())+ ' health points left')
            seperate_but_equal()




game = AlienGame()
