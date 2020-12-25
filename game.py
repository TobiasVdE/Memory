import random

from cell import Cell

RED = (255, 0, 0)
YELLOW = (150, 125, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

class Game:
    def randomize(self):
        for index in range(8):
            column = self.cells[index]
            for iteration in range(10):
                first = random.randrange(4)
                second = random.randrange(4)
                column[first], column[second] = column[second], column[first]

    def __init__(self):
        self.cells = []
        for column in range (8):
            self.cells.append([
                Cell (RED), 
                Cell (GREEN),
                Cell (BLUE),
                Cell (YELLOW)
            ])
        self.randomize()
