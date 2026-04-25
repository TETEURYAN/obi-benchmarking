import sys

data = list(map(int, sys.stdin.read().split()))
p, d1, d2 = data[0], data[1], data[2]

soma_par = (d1 + d2) % 2 == 0

if soma_par:
    print(p)
else:
    print(1 - p)