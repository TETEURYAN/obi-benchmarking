import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])
SA = list(map(int, data[2:2+A]))
SB = list(map(int, data[2+A:2+A+B]))

i = 0
for num in SA:
    if i < B and num == SB[i]:
        i += 1

if i == B:
    print('S')
else:
    print('N')