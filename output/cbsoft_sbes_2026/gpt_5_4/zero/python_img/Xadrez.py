import sys

L = int(sys.stdin.readline())
C = int(sys.stdin.readline())

print(1 if (L + C) % 2 == 0 else 0)