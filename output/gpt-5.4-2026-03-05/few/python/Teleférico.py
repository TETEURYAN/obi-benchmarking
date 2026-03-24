import sys

data = sys.stdin.read().split()
if not data:
    exit()

C = int(data[0])
A = int(data[1])

print((A + (C - 2)) // (C - 1))