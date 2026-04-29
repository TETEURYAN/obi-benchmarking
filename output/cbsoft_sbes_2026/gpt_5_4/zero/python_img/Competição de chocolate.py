import sys

n, m = map(int, sys.stdin.readline().split())

if n % (m + 1) == 0:
    print("Carlos")
else:
    print("Paula")