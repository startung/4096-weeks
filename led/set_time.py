from machine import Pin, I2C
import urtc
import time

I2C_PORT = 0
I2C_SDA = 20
I2C_SCL = 21

if __name__ == '__main__':
    i2c = I2C(I2C_PORT,scl=Pin(I2C_SCL),sda=Pin(I2C_SDA))
    rtc = urtc.DS3231(i2c)
    print(time.localtime())
    time_recv = time.localtime()
    print(time_recv[0], time_recv[1], time_recv[2], time_recv[6], time_recv[3], time_recv[4], time_recv[5], 0)
    rtc.datetime((time_recv[0], time_recv[1], time_recv[2], time_recv[6], time_recv[3], time_recv[4], time_recv[5], 0))

    #rtc.datetime(urtc.DateTimeTuple(*time.localtime()))
