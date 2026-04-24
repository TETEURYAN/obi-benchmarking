import sys

data = sys.stdin.read().split()
if not data:
    exit()
P = int(data[0])
R = int(data[1])

if P == 0:
    print('C')
else:
    if R == 0:
        print('B')
    else:
        print('A')