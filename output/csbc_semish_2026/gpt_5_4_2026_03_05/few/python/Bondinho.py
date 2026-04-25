import sys

data = sys.stdin.read().split()
if not data:
    exit()

A = int(data[0])
M = int(data[1])

print('S' if A + M <= 50 else 'N')