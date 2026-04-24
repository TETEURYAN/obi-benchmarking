import sys

data = sys.stdin.read().split()
if not data:
    exit()

A = int(data[0])
B = int(data[1])
C = int(data[2])
D = int(data[3])

if A == B + C + D and B + C == D and B == C:
    print('S')
else:
    print('N')