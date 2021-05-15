from tkinter import Widget
import pygame
import math

from pygame.scrap import put

pygame.init()

screen = pygame.display.set_mode([1500, 1000])

class Board:
    def __init__(self):
        self.tigers = []
        self.goats = []
        # Macierz pól, nie lista!!!
        self.fieldsRows = []

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
        pygame.draw.circle(screen, self.color, center, 10)

    def changeColor(self, col):
        self.color = col

class Tiger:
    def __init__(self):
        self.isBlocked = False

class Goat:
    def __init__(self):
        self.isAlive = True

board = Board()


running = True

screen.fill((255, 255, 255))
board.prepareBoard()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.prepareBoard()

            x, y = pygame.mouse.get_pos()
            print(x)
            print(y)
            for row in board.fieldsRows:
                for field in row:
                    if x > 100 and x < 1100 and y > 100 and y < 1100:
                        if (math.floor(x / 100) * 100) % 200 != 0 and (math.floor(y / 100) * 100) % 200 != 0:
                            pygame.draw.circle(screen, 'red', [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)

    pygame.display.flip()

pygame.quit()