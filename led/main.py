from led.personal import DOB, SPECIAL
import hub75
import utime
from machine import Pin, I2C
import urtc

WAKEUP_TIME = (7, 0)
SLEEP_TIME = (23, 0)

WIDTH = 64
HEIGHT = 64

I2C_PORT = 0
I2C_SDA = 20
I2C_SCL = 21


def weeks_between(start_date, end_date):
    start_date += (1, 0, 0, 0, 0)  # ensure a time past midnight
    end_date += (1, 0, 0, 0, 0)
    return utime.mktime(end_date) // (7 * 24 * 3600) - utime.mktime(start_date) // (
        7 * 24 * 3600
    )


if __name__ == "__main__":
    i2c = I2C(I2C_PORT, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
    rtc = urtc.DS3231(i2c)

    wakeup_time_sec = WAKEUP_TIME[0] * 3600 + WAKEUP_TIME[1] * 60
    sleep_time_sec = SLEEP_TIME[0] * 3600 + SLEEP_TIME[1] * 60

    # print(f"Seconds between: {datetime.hour}:{datetime.minute}:{datetime.second} and {SLEEP_TIME[0]}:{SLEEP_TIME[1]}:00 = {sleep_time_sec - curr_time_sec}")

    matrix = hub75.Hub75(WIDTH, HEIGHT)
    while True:
        datetime = rtc.datetime()
        curr_date = (datetime.year, datetime.month, datetime.day)
        weeks_me = weeks_between(DOB, curr_date)

        curr_time_sec = datetime.hour * 3600 + datetime.minute * 60 + datetime.second
        # print(curr_time_sec)
        # print(wakeup_time_sec)
        # print(sleep_time_sec)
        if wakeup_time_sec <= curr_time_sec <= sleep_time_sec:
            # print("Should be awake...")
            matrix.start()
            for i in range(weeks_me):
                matrix.set_pixel(i % 64, i // 64, 255, 0, 0)
            for week in SPECIAL:
                matrix.set_pixel(week % 64, week // 64, 0, 255, 0)
            # matrix.set_pixel(SPECIAL % 64, SPECIAL // 64, 255, 255, 255)
            # print(f"Run for {sleep_time_sec - curr_time_sec} seconds")
            # utime.sleep(60)
            # matrix.stop()

            # print(f"Sleep for {(wakeup_time_sec - curr_time_sec) % 86400} seconds")
            utime.sleep(60)
        else:
            # print("Should be asleep...")
            # print(f"Sleeping for {(wakeup_time_sec - curr_time_sec) % 86400} seconds")
            matrix.stop()
            utime.sleep(60)
