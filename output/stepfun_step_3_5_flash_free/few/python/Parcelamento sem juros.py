import sys

data = sys.stdin.read().split()
V = int(data[0])
P = int(data[1])
q = V // P
r = V % P
for _ in range(r):
    print(q + 1)
for _ in range(P - r):
    print(q)