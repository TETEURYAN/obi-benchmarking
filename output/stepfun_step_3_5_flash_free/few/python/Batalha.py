import sys

data = sys.stdin.read().split()
if not data:
    exit()

A1 = int(data[0])
D1 = int(data[1])
A2 = int(data[2])
D2 = int(data[3])

p1_ok = (D1 == A2)
p2_ok = (D2 == A1)

if p1_ok and not p2_ok:
    print(1)
elif p2_ok and not p1_ok:
    print(2)
else:
    print(-1)