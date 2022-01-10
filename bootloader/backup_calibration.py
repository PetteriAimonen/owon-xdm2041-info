#!/usr/bin/python3

'''Owon XDM2041 calibration backup script

This script uses the INT:TXT command to read out the calibration data.
'''

import sys
import time
import serial
import math
import struct

if len(sys.argv) < 2:
    sys.stderr.write("Usage: bootloader.py <serialport>\n")
    sys.exit(1)

port = serial.Serial(sys.argv[1], 115200, timeout = 1.0)

port.read()
port.write(b"INT:TXT\r\n")
data = port.read(16384)
data = data[0x18:]
open("calibration.bin", "wb").write(data)

print("Saved calibration.bin (%d bytes)" % len(data))

if len(data) != 2048:
    print("WARNING: Calibration length is not 2048 bytes")

for addr in [0x1f8, 0x22c, 0x350]:
    v = struct.unpack("<i", data[addr:addr+4])[0]
    if abs(v - 1000000) > 500000:
        print("WARNING: Calibration value %d at 0x%04x seems suspect, calibration may be corrupted" % (v, addr))

