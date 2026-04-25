import sys

data = sys.stdin.read().split()
N = int(data[0])
X = int(data[1])
Y = int(data[2])
Z = int(data[3])

max_evolve = 0
if X <= N or Y <= N or Z <= N:
    max_evolve = 1
if X + Y <= N or X + Z <= N or Y + Z <= N:
    max_evolve = 2
if X + Y + Z <= N:
    max_evolve = 3
print(max_evolve)