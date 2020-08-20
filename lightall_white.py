import time
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(1)
for x in range(8):
        for y in range(4):
                    uh.set_pixel(x, y, 255, 255, 255)
uh.show()
time.sleep(120)
