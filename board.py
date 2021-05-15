from tkinter import Widget
import pygame
import math

from pygame.scrap import put

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode([1500, 1000])

empty = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

class Board:
    def __init__(self):
        self.tigers = []
        self.goats = []
        # Macierz pól, nie lista!!!
        self.fieldsRows = []
        self.fields = empty

    def prepareBoard(self):
            # pygame.draw.lines(screen, 'black', False, [((x + 1) * 200 / 2, 1000), ((x + 1) * 200 / 2, 1000)], 5)
        for z in range(5):
            pygame.draw.lines(screen, 'black', False, [(100, 100 + (z * 200)), (900, 100 + (z * 200))], 5)
            pygame.draw.lines(screen, 'black', False, [(100 + (z * 200), 100), (100 + (z * 200), 900)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 100), (900, 900)], 5)
        pygame.draw.lines(screen, 'black', False, [(500, 100), (900, 500)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 500), (500, 900)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 900), (900, 100)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 500), (500, 100)], 5)
        pygame.draw.lines(screen, 'black', False, [(500, 900), (900, 500)], 5)
        for x in range(5):
            row = []
            for y in range(5):
                field = Field(x * 200, y * 200, (x + 1) * 200, (y + 1) * 200, x * 5 + y)
                row.append(field)
            self.fieldsRows.append(row)

    def updateBoard(self):
        self.fields = empty
        for tiger in self.tigers:
            pygame.draw.circle(screen, 'orange', [tiger.x, tiger.y], 30)
            self.fields[math.floor(tiger.y / 200)][math.floor(tiger.x / 200)] = 1
        for goat in self.goats:
            pygame.draw.circle(screen, 'grey', [goat.x, goat.y], 30)
            self.fields[math.floor(goat.y / 200)][math.floor(goat.x / 200)] = 2

class Field:
    def __init__(self, xStart, yStart, xEnd, yEnd, id):
        self.taken = False
        self.xStart = xStart
        self.yStart = yStart
        self.xEnd = xEnd
        self.yEnd = yEnd
        self.id = id
        self.color = 'black'
        self.drawField()
    
    def drawField(self):
        center = [(self.xStart + self.xEnd) / 2, (self.yStart + self.yEnd) / 2]
        pygame.draw.circle(screen, self.color, center, 30)

    def changeColor(self, col):
        self.color = col

class Tiger:
    def __init__(self, x, y):
        self.isBlocked = False
        self.x = x
        self.y = y

    def makeMove(self, tigerX, tigerY, board):
        noCoords = True
        while noCoords:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    destX, destY = pygame.mouse.get_pos()
                    destX = math.floor(destX / 100) * 100
                    destY = math.floor(destY / 100) * 100
                    if (destX == tigerX or destY == tigerY) and (destX % 200 != 0 and destY % 200 != 0) and not (destX == tigerX and destY == tigerY):
                        for fieldRow in board.fieldsRows:
                            for field in fieldRow:
                                if (field.xStart + field.xEnd) / 2 == tigerX and (field.yStart + field.yEnd) / 2 == tigerY:
                                    field.taken = False
                        for tiger in board.tigers:
                            if tiger.x == tigerX and tiger.y == tigerY:
                                board.fields[math.floor(tiger.y / 200)][math.floor(tiger.x / 200)] = 0
                                tiger.x = destX
                                tiger.y = destY
                                pygame.draw.circle(screen, 'black', [tigerX, tigerY], 30)
                        noCoords = False

class Goat:
    def __init__(self, x, y):
        self.isAlive = True
        self.x = x
        self.y = y

    def makeMove(self, goatX, goatY, board):
        noCoords = True
        while noCoords:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    destX, destY = pygame.mouse.get_pos()
                    destX = math.floor(destX / 100) * 100
                    destY = math.floor(destY / 100) * 100
                    if (destX == goatX or destY == goatY) and (destX % 200 != 0 and destY % 200 != 0) and not (destX == goatX and destY == goatY) and ((abs(destX - goatX) / 200 == 1) or (abs(destY - goatY) / 200 == 1)):
                        for fieldRow in board.fieldsRows:
                            for field in fieldRow:
                                if (field.xStart + field.xEnd) / 2 == goatX and (field.yStart + field.yEnd) / 2 == goatY:
                                    field.taken = False
                        for goat in board.goats:
                            if goat.x == goatX and goat.y == goatY:
                                board.fields[math.floor(goat.y / 200)][math.floor(goat.x / 200)] = 0
                                goat.x = destX
                                goat.y = destY
                                pygame.draw.circle(screen, 'black', [goatX, goatY], 30)
                        noCoords = False

board = Board()


running = True

screen.fill((255, 255, 255))
board.prepareBoard()

color = 'orange'
addingTigers = True
addingGoats = False
tigersMove = False

text = 'Tygrysy rozstawiają'


def isInsideSquare(x, y):
    if math.floor(x / 100) * 100 >= 300 and math.floor(x / 100) * 100 <= 700 and math.floor(y / 100) * 100 >= 300 and math.floor(y / 100) * 100 <= 700:
        return True
    else:
        return False

def goatLost(goatX, goatY):
    for goat in board.goats:
        if goat.x == goatX and goat.y == goatY:
            board.goats.remove(goat)
            board.fields[goat.x][goat.y] = 0

while running:
    textsurface = myfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))

    for event in pygame.event.get():
        if len(board.tigers) >= 2:
            addingTigers = False
            addingGoats = True
            color = 'grey'
        
        if len(board.goats) >= 18:
            addingGoats = False


        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            textsurface = myfont.render(text, False, (255, 255, 255))
            screen.blit(textsurface,(0,0))
            # board.prepareBoard()

            x, y = pygame.mouse.get_pos()
            if x > 100 and x < 1100 and y > 100 and y < 1100:
                if (math.floor(x / 100) * 100) % 200 != 0 and (math.floor(y / 100) * 100) % 200 != 0:
                    for row in board.fieldsRows:
                        for field in row:
                            if (field.xStart + field.xEnd) / 2 == math.floor(x / 100) * 100 and (field.yStart + field.yEnd) / 2 == math.floor(y / 100) * 100:
                                if addingTigers == True and isInsideSquare(x, y) and field.taken == False:
                                    print('Tygrysy rozstawiły')
                                    text = 'Tygrysy rozstawiły ' + str(len(board.tigers) + 1)
                                    board.tigers.append(Tiger(math.floor(x / 100) * 100, math.floor(y / 100) * 100))
                                    field.taken = True
                                    pygame.draw.circle(screen, color, [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                elif tigersMove == True:
                                    for tiger in board.tigers:
                                        if math.floor(x / 100) * 100 == tiger.x and math.floor(y / 100) * 100 == tiger.y:
                                            tiger.makeMove(tiger.x, tiger.y, board)
                                            print('Tygrysy zrobiły ruch')
                                            text = 'Tygrysy zrobiły ruch'
                                            tigersMove = False
                                elif addingGoats == True and field.taken == False:
                                    print('Kozy rozstawiły')
                                    text = 'Kozy rozstawiły '  + str(len(board.goats) + 1)
                                    board.goats.append(Goat(math.floor(x / 100) * 100, math.floor(y / 100) * 100))
                                    field.taken = True
                                    pygame.draw.circle(screen, color, [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                    if len(board.goats) >= 1 :
                                        tigersMove = True
                                elif tigersMove == False and addingTigers == False:
                                    for goat in board.goats:
                                        if math.floor(x / 100) * 100 == goat.x and math.floor(y / 100) * 100 == goat.y:
                                            goat.makeMove(goat.x, goat.y, board)
                                            print('Kozy zrobiły ruch')
                                            text = 'Kozy zrobiły ruch'
                                            tigersMove = True
                board.updateBoard()
                for row in board.fields:
                    print(row)
            screen.blit(textsurface,(0,0))
        
                                



    pygame.display.flip()

pygame.quit()