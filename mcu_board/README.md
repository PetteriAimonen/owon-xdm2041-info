MCU Board
=========

The XDM2041 MCU board contains:

* GD32F103CBT6 microcontroller
* 12 MHz crystal
* 32 kHz crystal
* RTC backup battery
* Beeper
* 3.3V linear regulator
* Membrane keyboard
* Level translator for RS232
* 24-pin TFT connector
* 16-pin ADC connector
* 6-pin USB/serial connector


24-pin TFT connector (U1)
=========================

TFT pin | MCU pin           |   Function
--------|-------------------|------------
1       |                   |   GND
2       |                   |   +3.3V
3       |                   |   +3.3V
4       |                   |   GND
5       |                   |   Probably floating
6       | 10 / PA0          |   D0
7       | 11 / PA1          |   D1
8       | 12 / PA2          |   D2
9       | 13 / PA3          |   D3
10      | 14 / PA4          |   D4
11      | 15 / PA5          |   D5
12      | 16 / PA6          |   D6
13      | 17 / PA7          |   D7
14      |                   |   GND
15      |                   |   Always high
16      | 21 / PB10         |   Write strobe, data is sampled on rising edge
17      | 20 / PB2          |   Data/Command selector, high = data, low = command
18      | 19 / PB1          |   Chip select (active low)
19      |                   |   Capacitor C2 + pull-up R6
20      |                   |   GND
21      |                   |   Backlight?
22      |                   |   Backlight?
23      |                   |   GND
24      |                   |   GND

TFT init sequence is captured in [tft_init_sequence.txt](tft_init_sequence.txt).
