import sys

data = sys.stdin.read().split()
P = int(data[0])
R = int(data[1])

if P == 0:
    if R == 0:
        print('C')
    else:
        print('A')
else:
    if R == 0:
        print('B')
    else:
        print('C')