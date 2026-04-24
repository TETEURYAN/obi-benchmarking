import sys

data = sys.stdin.read().split()
if not data:
    exit()
L = int(data[0])
C = int(data[1])
print(1 if (L + C) % 2 == 0 else 0)