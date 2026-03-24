import sys

data = sys.stdin.read().split()
if not data:
    exit()

L = int(data[0])
pieces = 1

while L >= 2:
    pieces *= 4
    L //= 2

print(pieces)