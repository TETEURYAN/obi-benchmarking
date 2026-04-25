import sys

data = sys.stdin.read().split()
A = int(data[0])
M = int(data[1])
if A + M <= 50:
    print('S')
else:
    print('N')