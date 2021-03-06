MCU Board
=========

The XDM2041 MCU board contains:

* GD32F103CBT6 microcontroller
* 12 MHz crystal
* 32 kHz crystal
* RTC backup battery
* Beeper (connected to MCU pin 29 / PA8 via R11 and Q2)
* 3.3V linear regulator
* Membrane keyboard ([layout](keyboard.md))
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
5       | ~~18 / PB0~~      |   Floating (IRQ? via unpopulated R1)
6       | 10 / PA0          |   D0
7       | 11 / PA1          |   D1
8       | 12 / PA2          |   D2
9       | 13 / PA3          |   D3
10      | 14 / PA4          |   D4
11      | 15 / PA5          |   D5
12      | 16 / PA6          |   D6
13      | 17 / PA7          |   D7
14      |                   |   GND
15      |                   |   Always high (Read Strobe?)
16      | 21 / PB10         |   Write strobe, data is sampled on rising edge
17      | 20 / PB2          |   Data/Command selector, high = data, low = command (*1*)
18      | 19 / PB1          |   Chip select (active low)
19      |                   |   RESET, Capacitor C2 + pull-up R6
20      |                   |   GND
21      |                   |   Backlight Anode (connected to +5V via R2//R3 = 12.5 Ohm)
22      | 34 / PA13         |   Backlight Cathode (*2*)
23      |                   |   GND
24      |                   |   GND

(*1*) Shared with BOOT1, pulled-down via R7

(*2*) switched with transistor Q1 via R5 from PA13 (shared with SWDIO/JTMS!).
Can be driven with PWM without flicker, as C1 as connected across Pin 21 and 22.

TFT init sequence is captured in [tft_init_sequence.txt](tft_init_sequence.txt).


16-pin connector to analog board (U5, numbered from left to right)
===

U5 pin	| MCU pin			|	Function
--------|-------------------|------------
1		|					|	GND
2		| 22 / PB11			|	SPI1 - nSS2 (74HC595 latch)
3		|					|	GND
4		|					|	GND
5		|					|	+3.3V
6		|					|	+3.3V
7		|					|	n.c.
8		| 27 / PB14			|	SPI1 - MISO
9		|					|	n.c.
10		| 28 / PB15			|	SPI1 - MOSI
11		|					|	n.c.
12		| 26 / PB13			|	SPI1 - SCK
13		|					|	n.c.
14		| 25 / PB12			|	SPI1 - nSS (HY3131 SPI)
15		|					|	n.c.
16		|					|	n.c.


6-pin USB / RS232 connector (U6)
===

U6 pin	| MCU pin			|	Function
--------|-------------------|------------
1		|					|	GND
2		|					|	GND
3		| 33 / PA12			|	USB D+ (*1*)
4		| 30 / PA9			|	Serial TXD via R22
5		| 32 / PA11			|	USB D- (*2*)
6		| 31 / PA10			|	Serial RXD via R17

(*1*) Originally pulled up to +5V via R12 (15k), should be changed to 1.5k and connected to +3.3V

(*2*) Originally pulled up to +5V via R13, should be removed totally.

(*3*) USB D+ and D- are reversed on the rear connector board, must be re-reversed...

USB lines are protected with a [TPD2E001 Transient Voltage Suppressor](https://www.ti.com/lit/ds/symlink/tpd2e001.pdf) (U10).

6-pin bootloader pinheader (CO2)
================================

When PCB is held upright, pin 1 is on the left side closest to the large screw hole in the PCB.

CO2 pin | MCU pin          | Function
--------|------------------|----------
1       | 31/PA10 thru R22 | USART0_RX
2       | 30/PA9 thru R17  | USART0_TX
3       |                  |
4       | 44/BOOT0         | High level activates bootloader
5       |                  | GND
6       |                  | 3.3V supply

~~A button can be connected between 3.3V and BOOT0, and holding it down on power-on will activate the built-in GD32 serial bootloader that can be used with e.g. [stm32flash](https://github.com/stm32duino/stm32flash).~~
Using the custom Owon bootloader with scripts in [bootloader folder](../bootloader) is easier and requires no modifications.

It seems the RS232 level translator overrides the RX pin on this connector if +5V is provided, so flashing through the backpanel RS232 port is better.



