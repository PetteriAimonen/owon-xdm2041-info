SPI captures from traffic between MCU and ADC board
===================================================

The SPI clock frequency is 2.6 kHz.

* [boot.txt](boot.txt): Initial power-on.
* [all_modes.txt](all_modes.txt): Activating each measurement mode in turn with SCPI commands. There may be some problems here because the SCPI interface does not seem to always behave reliably.


Considerations for max clock rate
---------------------------------

HY3131 is capable of quite high samplerates, but SPI bus speed is limited by the optocoupler speed.
Critical path is from SCK to MISO, because it goes twice through optocouplers.
The observed delay is 50 microseconds.

The original firmware runs SPI in CPHA = 0, CPOL = 0 mode, where slave
writes on falling edge and master reads on rising edge.
Possibly CPHA = 1, CPOL = 1 could work, because then the master would read only
on the following falling edge, giving twice the time for signal to settle.
