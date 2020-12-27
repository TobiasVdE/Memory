import random
import time
from cell import Cell


RED = (255, 0, 0)
YELLOW = (150, 125, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

class Game:
    lastCell = None

    def keyPressed(self, cell):
        # Zelfde cell als voordien
        if self.lastCell == cell:
            print("Same cell")
            return False

        column, row = cell
        
        # Cell is reeds gekend
        if self.cells[column][row].status:
            print("Cell known")
            return False

        # Eerste selectie
        if self.lastCell is None:
            print("First cell")
            self.lastCell = cell
            return False

        lastColumn, lastRow = self.lastCell

        if (self.cells[lastColumn][lastRow].colour == self.cells[column][row].colour):
            # Right anser
            print("Right answer")
            self.cells[lastColumn][lastRow].status = True
            self.cells[column][row].status = True
        else:
            time.sleep(1)
   
        print("Done")

        self.lastCell = None
        return True

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
