Owon XDM-2041 firmware memory map
=================================

* `0x0000` to `0x27FF` (10 kB): Bootloader
* `0x2800` to `0x1F7FF` (116 kB): Main code
* `0x1F800` to `0x1FFFF` (2 kB): Calibration area

Calibration area map
--------------------

* `0x1F800`: Text string model number, e.g. `XDM2041`
* `0x1F814`: Text string version, e.g. `V1.7.2`
* `0x1F824`: Serial number?
* `0x1F850`: Model number again
* `0x1F864`: Vendor name, e.g. `OWON`
* `0x1F86C` to `0x1F95B`: Small byte values 0x00 or 0x01, followed by version number
* `0x1F9F8` to `0x1FBB4`: Numeric values around 1000000, these are probably the calibration constants.

Calibration constant list
-------------------------
* `0001f9f8`: 1025169 
* `0001f9fc`: 1024832 
* `0001fa00`: 1029822 
* `0001fa04`: 1040282 
* `0001fa08`: 1030766 
* `0001fa0c`: 1032113 
* `0001fa20`: 1027002 
* `0001fa24`: 1032333 
* `0001fa28`: 1042326 
* `0001fa2c`: 1026557 
* `0001fa48`: 1017067 
* `0001fa4c`: 1016822 
* `0001fa50`: 1027919 
* `0001fa54`: 1027625 
* `0001fa58`: 1123798 
* `0001fa5c`: 1124657 
* `0001fa74`: 1017299 
* `0001fa78`: 1028111 
* `0001fa7c`: 1027737 
* `0001faa4`: 917632 
* `0001faa8`: 1033222 
* `0001faac`: 1037738 
* `0001fac0`: 1009899 
* `0001fac4`: 1009479 
* `0001fac8`: 999549 
* `0001fb38`: 946991 
* `0001fb3c`: 948413 
* `0001fb40`: 1006721 
* `0001fb44`: 1026230 
* `0001fb48`: 1326464 
* `0001fb4c`: 958559 
* `0001fb50`: 1010442 
* `0001fbb0`: -200598 
* `0001fbb4`: -187438 

