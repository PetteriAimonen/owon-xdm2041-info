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

Reading out flash memory
------------------------

This method to defeat the read-protection is based on work by [Johannes Obermaier](https://github.com/JohannesObermaier/f103-analysis).

For this step, a SWD debugger adapter supported by [openocd](http://openocd.org/)
is needed. FT2232H or FT232H based adapter is recommended, though there are
some reports of success with ST-Link also.

A modified version of OpenOCD is needed so that it does not automatically set the `C_DEBUGEN` bit that blocks the flash.
It is available from [https://github.com/PetteriAimonen/openocd/tree/hack_no_C_DEBUGEN](here).

Connect the debugger to SWDIO and SWCLK pins on the microcontroller.
If using a bare FT232H breakout board, an external resistor is needed as described [https://github.com/unprovable/FTDI-Oh-My/blob/master/FT232H-JTAG-SWD.txt](here).

This command should read out the flash and write it out to files under `/tmp/`:

    openocd  -f scripts/interface/ftdi/ft232h-module-swd.cfg  -f GD32F103.cfg -c init -f GD32F103_dump_script.txt

After that, the files can be combined and the last 2 kB can be taken and combined with a working firmware file, available [here](https://jpa.kapsi.fi/stuff/other/owon_xdm2041_firmware.bin).

**NOTE: This process is very much work-in-progress and while it has worked for several people already, it is not very easy to use.**

