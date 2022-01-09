#!/usr/bin/python3

'''Owon XDM2041 calibration area loader script.

This script *will* overwrite the calibration data (last 2 kB of flash).
'''

import sys
import time
import serial
import math
import struct

if len(sys.argv) < 3:
    sys.stderr.write("Usage: xdm2041_load_calibration.py <serialport> <filename.bin>\n")
    sys.exit(1)

port = serial.Serial(sys.argv[1], 115200, timeout = 0.1)
bindata = open(sys.argv[2], 'rb').read()

print("WARNING: This script will overwrite calibration data")
print("Trying to enter bootloader. Restart XDM2041 now.")
while True:
    sys.stdout.write('.')
    sys.stdout.flush()
    
    port.write(b'start')
    time.sleep(0.1)
    if b'7' in port.read(1024):
        break

print("Bootloader active!")
port.timeout = 10.0

print("Will send 1 pack to area 2")
print("Erasing flash..")

port.write(b'\x02')
if b'7' not in port.read(16):
    sys.stderr.write("ERROR: No acknowledge to write area\n")
    sys.exit(2)

port.write(b'\x01')
if b'7' not in port.read(16):
    sys.stderr.write("ERROR: No acknowledge to pack count\n")
    sys.exit(3)

print("Programming calibration data");
port.write(bindata)

if b'7' not in port.read(16):
    sys.stderr.write("ERROR: No acknowledge to calibration write")
    sys.exit(4)

print("Exiting bootloader..")
port.write(b'\x14')

port.timeout=1.0
port.read()
time.sleep(10)
port.write(b'*IDN?\r\n')
response = port.read(1024)

print("All done, SCPI IDN response: " + repr(response))

