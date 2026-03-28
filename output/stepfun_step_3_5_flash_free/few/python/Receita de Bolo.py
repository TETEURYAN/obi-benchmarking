import sys

data = sys.stdin.read().split()
if not data:
    exit()

A = int(data[0])
B = int(data[1])
C = int(data[2])

print(min(A // 2, B // 3, C // 5))