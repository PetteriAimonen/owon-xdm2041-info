XDM2041 default bootloader
==========================

XDM2041 contains a bootloader that can be activated by command `INT:DOWNLOAD`.
It then stays active even after restart until `\r\n\r\n` is sent to return to normal mode.

Alternative way to activate bootloader is to send `start` immediately after power-on.

Bootloader protocol
-------------------

Dumped from [XDM1041 update program](https://github.com/PetteriAimonen/OWON-XDM1041)

    00000000  73 74 61 72 74                                     start
    00000005  73 74 61 72 74                                     start
    ... retry bootloader activation ....
    00000073  73 74 61 72 74                                     start
    00000078  73 74 61 72 74                                     start
    0000007D  73 74 61 72 74                                     start
        00000000  37                                                 7   <-- Bootloader reply
    00000082  05                                                 .       <-- Binary area 5
        00000001  37                                                 7
    00000083  0c                                                 .       <-- Number of 10 kB packets to send
        00000002  37                                                 7
    00000084  08 4b 00 20 01 29 00 08  2d 47 00 08 2f 47         .K. .).. -G../G
    00000092  00 08 31 47 00 08 33 47  00 08 35 47 00 08         ..1G..3G ..5G..
    000000A0  00 00 00 00 00 00 00 00  00 00 00 00 00 00         ........ ......
    000000AE  00 00 37 47 00 08 39 47  00 08 00 00 00 00         ..7G..9G ......
    000000BC  3b 47 00 08 3d 47 00 08  1b 29 00 08 1b 29         ;G..=G.. .)...)
    000000CA  00 08 1b 29 00 08 47 49  00 08 1b 29 00 08         ...)..GI ...)..
    000000D8  1b 29 00 08 1b 29 00 08  1b 29 00 08 1b 29         .)...).. .)...)

Bootloader script
-----------------

A Python script `xdm2041_bootloader.py` is provided to flash firmware.
No guarantees, but for me it seems to work and not damage calibration.
