import sys

data = sys.stdin.read().split()
if not data:
    exit()
x = int(data[0])
y = int(data[1])

if -8 <= x <= 8 and 0 <= y <= 8:
    print('S')
else:
    print('N')