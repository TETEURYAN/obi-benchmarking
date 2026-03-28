import sys

L = int(sys.stdin.read().strip())

pieces = 1
while L >= 2:
    pieces *= 4
    L //= 2

print(pieces)