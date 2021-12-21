Information collected from Owon XDM2041
=======================================

The goal of this project is to collect enough information about the XDM2041
hardware to facilitate writing an open source firmware for it.

Also sold as PeakTech 4095 and VoltCraft VC-7055.


Hidden SCPI commands
--------------------

Following SCPI commands are not mentioned in the main documentation:

* `INT:VERSION xxxx` Sets the software version number in flash
* `INT:MODEL xxxx` Sets the software model number in flash
* `INT:CHECKSUM?` Queries checksum of something
* `INT:HYREG` Probably used to set HY3131 registers, arguments unknown
* `INT:DOWNLOAD` Enters bootloader mode. Send `\r\n\r\n` to exit bootloader mode.
