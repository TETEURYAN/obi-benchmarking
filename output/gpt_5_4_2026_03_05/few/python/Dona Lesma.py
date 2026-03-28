import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

A = int(data[0])
S = int(data[1])
D = int(data[2])

if A <= S:
    print(1)
else:
    print((A - S + (S - D) - 1) // (S - D) + 1)