import time
import unicornhat as uh
import colorsys

uh.set_layout(uh.PHAT)
uh.brightness(1)

while True:
    for x in range(8):
        for y in range(4):
            uh.set_pixel(x, y, 255, 0, 255)
    uh.show()
    time.sleep(0.25)
    uh.clear()
    uh.show()
    time.sleep(0.25)
