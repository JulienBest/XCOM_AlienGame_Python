import random
from Player import Player
from Alien import Alien

class Map:

    height = None
    width = None
    alienCount = None
    map = None
    aliens = []
    player = None

    def __init__(self, height, width, alienCount):
        self.height = height +1 #+1 because of the border and the
        self.width = width +1   # numbers around the map
        self.alienCount = alienCount
        self.map = [['*' for i in range(self.width)] for j in range(self.height)]
        self.createEmpty()
        #self.set(2,6,'O')
        self.placePlayer()
        self.placeAliens()
        self.print_map()


    '''
    Creates an empty Map
    '''
    def createEmpty(self):
        for i in range(self.height):
            for j in range(self.width):
                if j == 0:
                    self.map[i][j] = self.format(i-1)
                elif i == 0:
                    self.map[i][j] =self.formatUpper(j-1)
                else:
                    self.map[i][j] = '[ ]'
        self.map[0][0] = ' *'


    def getPlayer(self):
        return self.player

    def getAliens(self):
        return self.aliens

    '''
    Assigns the player object and places it on the map
    '''
    def placePlayer(self):
        randX = random.randint(1,self.width-1)
        randY = random.randint(1,self.height-1)

        self.player = Player(randX, randY, self)


    '''
    Places the Aliens, appends the objects to the alien array
    '''
    def placeAliens(self):
        for i in range(self.alienCount):
            while True:
                randX = random.randint(1,self.width -1)
                randY = random.randint(1,self.height-1)

                if self.map[randY][randX] == '[ ]':
                    self.aliens.append(Alien(randX, randY, self))
                    break

    '''
    Prints the map to the terminal
    '''
    def print_map(self):
        output = ''
        for i in range(self.height):
            output += '\n'
            for j in range(self.width):
                output += self.map[i][j]
        print(output)

    '''
    Sets a field of the map to the char parameter
    '''
    def set(self, x, y, char):
        self.map[y][x] = '['+char+']'

    def getInstance(self):
        return self

    def format(self,num):
        n = str(num)
        if len(n) == 2:
            return n
        else:
            return ' '+ n

    def formatUpper(self, num):
        n = str(num)
        if(len(n)==2):
            return ' '+n

        else:
            return ' '+ n+ ' '
