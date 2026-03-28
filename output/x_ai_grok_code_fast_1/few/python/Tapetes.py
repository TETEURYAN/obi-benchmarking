import sys

L, N = map(int, sys.stdin.read().split())
small = N - 1
big = L - small
area = small * 1 + big ** 2
print(area)