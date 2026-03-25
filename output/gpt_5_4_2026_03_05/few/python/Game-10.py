import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    d = int(data[1])
    a = int(data[2])
    print((d - a) % n)