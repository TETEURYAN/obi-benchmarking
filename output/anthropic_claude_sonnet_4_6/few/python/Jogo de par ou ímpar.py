import sys
data = sys.stdin.read().split()
P = int(data[0])
D1 = int(data[1])
D2 = int(data[2])
total = D1 + D2
if total % 2 == 0:
    print(P)
else:
    print(1 - P)