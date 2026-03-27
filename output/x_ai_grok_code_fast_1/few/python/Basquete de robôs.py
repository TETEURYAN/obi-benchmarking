import sys

data = sys.stdin.read().strip()
D = int(data)

if D <= 800:
    print(1)
elif D <= 1400:
    print(2)
else:
    print(3)