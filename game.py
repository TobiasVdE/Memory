from cell import Cell

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

class Game:
    def __init__(self):
        self.cells = []
        for column in range (8):
            self.cells.append([
                Cell (RED), 
                Cell (GREEN),
                Cell (BLUE),
                Cell (YELLOW)
            ])
