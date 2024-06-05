from personal import DOB, SPECIAL
import hub75
import utime
from machine import Pin, I2C
import urtc

WAKEUP_TIME = 7
SLEEP_TIME = 23

I2C_PORT = 0
I2C_SDA = 20
I2C_SCL = 21

def weeks_between(start_date, end_date):
    start_date += (1, 0, 0, 0, 0)  # ensure a time past midnight
    end_date += (1, 0, 0, 0, 0)
    return (utime.mktime(end_date)-utime.mktime(start_date))//604800


if __name__ == "__main__":
    i2c = I2C(I2C_PORT, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
    rtc = urtc.DS3231(i2c)

    matrix = hub75.Hub75(64, 64)
    matrix.start()
    
    while True:
        datetime = rtc.datetime()
        print(datetime)
        curr_date = (datetime.year, datetime.month, datetime.day)
        weeks_me = weeks_between(DOB, curr_date)

        if WAKEUP_TIME <= datetime.hour < SLEEP_TIME:
            for i in range(weeks_me):
                matrix.set_pixel(i % 64, i // 64, 255, 0, 0)
            for week in SPECIAL:
                matrix.set_pixel(week % 64, week // 64, 255, 255, 255)
            utime.sleep(60)
        else:
            matrix.clear()
            utime.sleep(60)