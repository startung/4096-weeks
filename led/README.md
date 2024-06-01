## 4096 Weeks LED Grid

LEDs are everywhere, and one use of them are the giant LED displays. These are often formed of much smaller grids, and driven by microcontrollers. I had a 64 by 64 grid I could salvage from an ealier project (an [led sand toy](https://learn.adafruit.com/matrix-led-sand/overview)). When paired with a RP2040 microcontroller and driver board from Pimoroni. I could create a simple reminder that life is short - enjoy it!

### Notes

- [code](https://github.com/startung/4096-weeks/tree/main/led) is in micropython
- uses a real time clock, based on the DS3231 to ensure it keeps time even when unplugged
- ensure your personal information is not sent to git hub

### Future Plans

- switch to wifi version of the microcontroller to simplify the updating and allow for syncing with a network time server
