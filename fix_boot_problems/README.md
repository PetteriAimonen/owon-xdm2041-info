Fixing Owon XDM 2041 / Voltcraft VC7055 boot problems
=====================================================

A surprisingly common problem with these multimeters appears to be that they
corrupt the internal microcontroller flash memory. The symptom is that boot
stops at the progress bar.

The same symptom (stuck at progress bar) happens if the flex cable between
the microcontroller board and the ADC board is not properly connected, so
check that first.

Repair is complicated because the microcontroller flash memory is read-protected.
The protection can be disabled, but it will also erase the flash.
The factory calibration information is stored in the last 2 kB of the flash
memory, so it has to be saved before erasing the device.

Simple method: Trying if it just needs bootloader exit
------------------------------------------------------

The OWON XDM2041 appears to have an internal bootloader that is entered by command `INT:DOWNLOAD`.
It writes bootloader enable to flash and will stay at empty progressbar on every boot after that.
To exit the bootloader, write `\r\n\r\n` to the serial port at 115200 bps.

Intermediate method: Trying to flash firmware through bootloader
----------------------------------------------------------------

Main firmware can be rewritten without destroying calibration data by using the bootloader. See [bootloader folder](../bootloader).

1. Install Python 3. On Windows you may need to type `py` instead of `python` below.
2. Install pyserial: `python -m pip install pyserial`
3. Upload firmware: `python xdm2041_bootloader.py COMx XDM2041.bin`


Complex method: Reading out flash memory
----------------------------------------

**NOTE: This was the original method first discovered to restore these devices. The bootloader method described above doesn't need opening the device and is easier.**

If all else fails, one can open up the multimeter and solder in wires to connect a SWD-based debugger attachment.
The XDM2041 is also readout protected so this gets pretty complex.

This method to defeat the read-protection is based on work by [Johannes Obermaier](https://github.com/JohannesObermaier/f103-analysis).

For this step, a SWD debugger adapter supported by [openocd](http://openocd.org/)
is needed. FT2232H or FT232H based adapter is recommended, though there are
some reports of success with ST-Link also.

A modified version of OpenOCD is needed so that it does not automatically set the `C_DEBUGEN` bit that blocks the flash.
It is available from [here](https://github.com/PetteriAimonen/openocd/tree/hack_no_C_DEBUGEN).

It may be necessary to pull BOOT0 pin high to be able to get connection to debugger.

Connect the debugger to SWDIO and SWCLK pins on the microcontroller.
If using a bare FT232H breakout board, an external resistor is needed as described [here](https://github.com/unprovable/FTDI-Oh-My/blob/master/FT232H-JTAG-SWD.txt).

This command should read out the flash and write it out to files under `/tmp/`:

    openocd  -f scripts/interface/ftdi/ft232h-module-swd.cfg  -f GD32F103.cfg -c init -f GD32F103_dump_script.txt

After that, the files can be combined and the last 2 kB can be taken and combined with a working firmware file, available [here](https://jpa.kapsi.fi/stuff/other/owon_xdm2041_firmware.bin).


