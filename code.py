import time
import adafruit_trellism4
import game

trellis = adafruit_trellism4.TrellisM4Express()
trellis.pixels.auto_write = False

def showGame(g, all):
    print("Show game")
    for column in range(8):
        for row in range(4):
            cell = g.cells[column][row]
            if (cell.status or all):
                trellis.pixels[column, row] = cell.colour
            else:
                trellis.pixels[column, row] = game.OFF
    trellis.pixels.show()        

current_press = set()
while True:
    g = game.Game()
    showGame(g, True)
    time.sleep(1.000)
    trellis.pixels.fill(game.OFF)
    trellis.pixels.show()
    
    while True:
        pressed = set(trellis.pressed_keys)
        for press in pressed - current_press:
            column, row = press
            trellis.pixels[column, row] = g.cells[column][row].colour
            trellis.pixels.show()        

            if g.keyPressed(press):
                showGame(g, False)
        current_press = pressed
        trellis.pixels.show()





    # pressed = set(trellis.pressed_keys)
    # for press in pressed - current_press:
    #     for x in range(8):
    #         trellis.pixels[x, 0] = game.GREEN
    #         trellis.pixels[x, 1] = game.BLUE
    #         trellis.pixels[x, 2] = game.RED
    #         trellis.pixels[x, 3] = game.YELLOW
    # for release in current_press - pressed:
    #     trellis.pixels.fill(game.OFF)
    # trellis.pixels.show()
    # time.sleep(0.08)
    # current_press = pressed
