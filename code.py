import time
import adafruit_trellism4

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

trellis = adafruit_trellism4.TrellisM4Express()
trellis.pixels.auto_write = False

current_press = set()
while True:
    pressed = set(trellis.pressed_keys)
    for press in pressed - current_press:
        for x in range(8):
            trellis.pixels[x, 0] = GREEN
            trellis.pixels[x, 1] = BLUE
            trellis.pixels[x, 2] = GREEN
            trellis.pixels[x, 3] = BLUE
    for release in current_press - pressed:
        trellis.pixels.fill(OFF)
    trellis.pixels.show()
    time.sleep(0.08)
    current_press = pressed
