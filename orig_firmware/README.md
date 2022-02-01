Owon XDM-2041 firmware memory map
=================================

* `0x0000` to `0x27FF` (10 kB): Bootloader
* `0x2800` to `0x1F5FF` (114 kB): Main code
* `0x1F600` to `0x1F7FF` (2 kB): Unknown, handled separately by bootloader
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

For each constant, the table has the following information:
* Memory address in flash
* Value it has on my device
* ADC scaler used by firmware when calibration is set to 1000000. ADC value is converted to -1..+1 range first, i.e. the scaler in the table is the full scale measurement value.
* Which range the calibration constant affects

| Address    |Example value| ADC scaler  | Description
| ---------- | -------- | -------------- | --------------------------------------
| `0001f9f8` | 1025169  | 0.0683207      | **Scale for 50 mVDC**
| `0001f9fc` | 1024832  | 0.683336       | **Scale for 500 mVDC**
| `0001fa00` | 1029822  | 7.51667        | **Scale for 5 VDC, tested**
| `0001fa04` | 1040282  | 68.3336        | **Scale for 50 VDC, tested**
| `0001fa08` | 1030766  | 683.331        | **Scale for 500 VDC, tested**
| `0001fa0c` | 1032113  | 1366.68        | **Scale for 1000 VDC**
|            |          |                |  
| `0001fa20` | 1027002  | 78.7208        | **Scale for 500 mVAC, tested**, relative to sqrt(RMS_DATA)
| `0001fa24` | 1032333  | 865.928        | **Scale for 5 VAC, tested**
| `0001fa28` | 1042326  | 7872.03        | **Scale for 50 VAC, tested**
| `0001fa2c` | 1026557  | 78720.9        | **Scale for 500 VAC, tested**
|            |          |                |  
| `0001fa48` | 1017067  | 0.00068358     | **Scale for 500uADC**
| `0001fa4c` | 1016822  | 0.00683302     | **Scale for 5mADC**
| `0001fa50` | 1027919  | 0.0683327      | **Scale for 50mADC, tested**
| `0001fa54` | 1027625  | 0.683336       | **Scale for 500mADC, tested**
| `0001fa58` | 1123798  | 6.83335        | **Scale for 5ADC**
| `0001fa5c` | 1124657  | 13.6667        | **Scale for 10ADC**
|            |          |                |  
| `0001fa74` | 1017299  |                | **Unknown**
| `0001fa78` | 1028111  |                | **Unknown**
| `0001fa7c` | 1027737  |                | **Scale for AC current measurements, on top of DC**
|            |          |                |  
| `0001faa4` | 917632   | 1.1128e+06     | **Scale for 500kohm, tested**
| `0001faa8` | 1033222  | 6.67625e+06    | **Scale for 5Mohm, tested**
| `0001faac` | 1037738  | 6.7351e+07     | **Scale for 50Mohm, tested**
|            |          |                |  
| `0001fac0` | 1009899  |  1112.13       | **Scale for 500ohm, tested**
| `0001fac4` | 1009479  | 11198.8        | **Scale for 5kohm, tested**
| `0001fac8` | 999549   |112494          | **Scale for 50kohm, tested**
|            |          |                |  
| `0001fb38` | 946991   |                | **Scale for 50nF, tested**
| `0001fb3c` | 948413   |                | **Scale for 500nF, tested**
| `0001fb40` | 1006721  |                | **Scale for 5uF**
| `0001fb44` | 1026230  |                | **Scale for 50uF, tested**
| `0001fb48` | 1326464  |                | **Scale for 500uF**
| `0001fb4c` | 958559   |                | **Scale for 5mF**
| `0001fb50` | 1010442  |                | **Scale for 50mF**
|            |          |                |  
| `0001fbb0` | -200598  |                | **Offset for 50 mVDC range in nanovolts**
| `0001fbb4` | -187438  |                | **Offset for 500 mVDC range in nanovolts**

