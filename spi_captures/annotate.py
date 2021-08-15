# Usage:
# (grep 'transfers:..' hy3131.txt | sed 's/SPI/HY3131/' | cut -d '-' -f 2- | python annotate.py ; grep 'MOSI transfers:..' 74hc595.txt | sed 's/SPI/74HC595/' | cut -d '-' -f 2-; grep 'RX data' uart.txt | python annotate_uart.py) | sort -g > all_modes.txt

import sys

registers = {
    0x00: 'AD1_DATA',
    0x03: 'AD2_DATA',
    0x06: 'LPF_DATA',
    0x09: 'RMS_DATA',
    0x0E: 'PKHMIN',
    0x11: 'PKHMAX',
    0x14: 'CTSTA',
    0x15: 'CTC',
    0x18: 'CTB',
    0x1B: 'CTA',
    0x1E: 'INTF',
    0x1F: 'INTE'
}

for line in sys.stdin:
    if not 'MOSI transfers' in line:
        sys.stdout.write(line)
    else:
        data = [int(x,16) for x in line[line.index('MOSI transfers'):].split(':')[1].split()]
        read = data[0] & 1
        addr = data[0] >> 1
        regname = registers.get(addr, 'R%02x' % addr)
        
        if len(data) > 10 and addr == 0 and not read:
            sys.stdout.write(line.strip('\n').ljust(60) + " # Bulk write\n")
        elif read:
            sys.stdout.write(line.strip('\n').ljust(60) + " # Read " + regname + "\n")
        else:
            sys.stdout.write(line.strip('\n').ljust(60) + " # Write " + regname + "\n")

