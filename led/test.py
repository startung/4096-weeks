from interstate75 import Interstate75, SWITCH_A, SWITCH_B
from machine import Pin, I2C
import time
import urtc

I2C_PORT = 0
I2C_SDA = 20
I2C_SCL = 21

i75 = Interstate75(display=Interstate75.DISPLAY_INTERSTATE75_64X64)
graphics = i75.display

i2c = I2C(I2C_PORT, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
rtc = urtc.DS3231(i2c)

#while True:
#    if i75.switch_pressed(SWITCH_A):
#        i75.set_led(255, 0, 0)
#    elif i75.switch_pressed(SWITCH_B):
#        i75.set_led(0, 255, 0)


MAGENTA = graphics.create_pen(255, 0, 255)
BLACK = graphics.create_pen(0, 0, 0)
WHITE = graphics.create_pen(255, 255, 255)

graphics.set_pen(BLACK)
graphics.clear()

def clock():
    datetime = rtc.datetime()
    graphics.set_pen(MAGENTA)
    graphics.text(str(datetime.day), 4, 4, scale=1)
    graphics.set_pen(WHITE)
    graphics.text(str(datetime.month), 18, 4, scale=1)
    graphics.set_pen(MAGENTA)
    graphics.text(str(datetime.year), 30, 4, scale=1)
    graphics.set_pen(WHITE)
    graphics.text(str(datetime.hour), 4, 18, scale=1)
    graphics.set_pen(MAGENTA)
    graphics.text(str(datetime.minute), 18, 18, scale=1)
    i75.update(graphics)
    time.sleep(60.0)
    graphics.set_pen(BLACK)
    graphics.clear()
    i75.update(graphics)
    
while True:
    clock()
    

#    graphics.set_pen(BLACK)
#    graphics.clear()
#    i75.update(graphics)
#    time.sleep(0.5)