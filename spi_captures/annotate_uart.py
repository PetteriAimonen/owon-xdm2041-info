import sys

s = ''
for line in sys.stdin:
    if not 'RX data' in line or 'bit' in line:
        continue
    
    parts = line.strip().split()
    timestamp = parts[0].split('-')[0]
    data = parts[-1]
    if '[' in data:
        if s:
            print(timestamp, s)
        s = ''
    elif 'data' in data:
        s += ' '
    else:
        s += data

