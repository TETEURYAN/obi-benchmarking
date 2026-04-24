import sys

data = sys.stdin.read().split()
if not data:
    exit()

P, R = map(int, data)

if P == 0:
    print("C")
elif R == 0:
    print("B")
else:
    print("A")