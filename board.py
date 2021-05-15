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

move_connections = {
    0: [1, 5, 6], 1: [2, 0, 6], 2: [3, 1, 7, 6, 8], 3: [4, 2, 8], 4: [3, 9, 8],
    5: [6, 10, 0], 6: [7, 5, 11, 1, 10, 2, 12, 0], 7: [8, 6, 12, 2], 8: [9, 7, 13, 3, 12, 4, 14, 2], 9: [8, 14, 4],
    10: [11, 15, 5, 6, 16], 11: [12, 10, 16, 6], 12: [13, 11, 17, 7, 16, 8, 18, 6], 13: [14, 12, 18, 8],
    14: [13, 19, 9, 18, 8],
    15: [16, 20, 10], 16: [17, 15, 21, 11, 20, 12, 22, 10], 17: [18, 16, 22, 12],
    18: [19, 17, 23, 13, 22, 14, 24, 12], 19: [18, 24, 14],
    20: [21, 15, 16], 21: [22, 20, 16], 22: [23, 21, 17, 18, 16], 23: [24, 22, 18], 24: [23, 19, 18]
}

capture_connections = {
    0: [2, 10, 12], 1: [3, 11], 2: [4, 0, 12, 10, 14], 3: [1, 13], 4: [2, 14, 12],
    5: [7, 15], 6: [8, 16, 18], 7: [9, 5, 17], 8: [6, 18, 16], 9: [7, 19],
    10: [12, 20, 0, 2, 22], 11: [13, 21, 1], 12: [14, 10, 22, 2, 20, 4, 24, 0],
    13: [11, 23, 3], 14: [12, 24, 4, 22, 2],
    15: [17, 5], 16: [18, 6, 8], 17: [19, 15, 7], 18: [16, 8, 6], 19: [17, 9],
    20: [22, 10, 12], 21: [23, 11], 22: [24, 20, 12, 14, 10], 23: [21, 13], 24: [22, 14, 12]
}

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
            print(tiger.x)
            print(tiger.y)
            self.fields[math.floor(tiger.y / 200)][math.floor(tiger.x / 200)] = 1
        for goat in self.goats:
            pygame.draw.circle(screen, 'grey', [goat.x, goat.y], 30)
            self.fields[math.floor(goat.y / 200)][math.floor(goat.x / 200)] = 2

class Field:
    def __init__(self, xStart, yStart, xEnd, yEnd, id):
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
                    mouseX, mouseY = pygame.mouse.get_pos()
                    destX = math.floor(mouseX / 100) * 100
                    destY = math.floor(mouseY / 100) * 100
                    for connection in move_connections[math.floor(tigerX / 200) * 5 + math.floor(tigerY / 200)]:
                        if connection == math.floor(mouseX / 200) * 5 + math.floor(mouseY / 200) and board.fields[math.floor(destY / 200)][math.floor(destX / 200)] == 0 and (destX % 200 != 0 and destY % 200 != 0):
                            print('Destination Value: ', board.fields[math.floor(destY / 200)][math.floor(destX / 200)])
                            for tiger in board.tigers:
                                if tiger.x == tigerX and tiger.y == tigerY:
                                    board.fields[math.floor(tigerY / 200)][math.floor(tigerX / 200)] = 0
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
                    mouseX, mouseY = pygame.mouse.get_pos()
                    destX = math.floor(mouseX / 100) * 100
                    destY = math.floor(mouseY / 100) * 100
                    for connection in move_connections[math.floor(goatX / 200) * 5 + math.floor(goatY / 200)]:
                        if connection == math.floor(mouseX / 200) * 5 + math.floor(mouseY / 200) and board.fields[math.floor(destY / 200)][math.floor(destX / 200)] == 0 and (destX % 200 != 0 and destY % 200 != 0):
                            print('Destination Value: ', board.fields[math.floor(destY / 200)][math.floor(destX / 200)])
                            for goat in board.goats:
                                if goat.x == goatX and goat.y == goatY:
                                    board.fields[math.floor(goatY / 200)][math.floor(goatX / 200)] = 0
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

            x, y = pygame.mouse.get_pos()
            if x > 100 and x < 1100 and y > 100 and y < 1100:
                if (math.floor(x / 100) * 100) % 200 != 0 and (math.floor(y / 100) * 100) % 200 != 0:
                    for row in board.fieldsRows:
                        for field in row:
                            if (field.xStart + field.xEnd) / 2 == math.floor(x / 100) * 100 and (field.yStart + field.yEnd) / 2 == math.floor(y / 100) * 100:
                                if addingTigers == True and isInsideSquare(x, y) and board.fields[math.floor(y / 200)][math.floor(x / 200)] == 0:
                                    print('Tygrysy rozstawiły')
                                    text = 'Tygrysy rozstawiły ' + str(len(board.tigers) + 1)
                                    board.tigers.append(Tiger(math.floor(x / 100) * 100, math.floor(y / 100) * 100))
                                    pygame.draw.circle(screen, color, [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                elif tigersMove == True:
                                    for tiger in board.tigers:
                                        if math.floor(x / 100) * 100 == tiger.x and math.floor(y / 100) * 100 == tiger.y:
                                            tiger.makeMove(tiger.x, tiger.y, board)
                                            print('Tygrysy zrobiły ruch')
                                            text = 'Tygrysy zrobiły ruch'
                                            tigersMove = False
                                elif addingGoats == True and board.fields[math.floor(y / 200)][math.floor(x / 200)] == 0:
                                    print('Kozy rozstawiły')
                                    text = 'Kozy rozstawiły '  + str(len(board.goats) + 1)
                                    board.goats.append(Goat(math.floor(x / 100) * 100, math.floor(y / 100) * 100))
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