import sys

data = sys.stdin.read().strip().split()
if not data:
    exit()

x = int(data[0])
y = int(data[1])

if 0 <= x <= 16 and 0 <= y <= 8:
    print('S')
else:
    print('N')