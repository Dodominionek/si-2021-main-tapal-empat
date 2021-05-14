import pygame
pygame.init()

screen = pygame.display.set_mode([1500, 1000])

class Board:
    def __init__(self):
        self.tigers = []
        self.goats = []
        self.fields = []

    def prepareBoard(self):
        for x in range(5):
            temp = []
            for y in range(5):
                temp.append(Field(x, y))
            self.fields.append(temp)


class Field:
    def __init__(self, x, y):
        self.taken = False
        self.x = x
        self.y = y

class Tiger:
    def __init__(self):
        self.isAlive = True

class Goat:
    def __init__(self):
        self.isBlocked = False

board = Board()

print(board.fields)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, 'black', pygame.Rect(50, 50, 500, 100))

    pygame.display.flip()

pygame.quit()