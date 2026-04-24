import sys
data = sys.stdin.read().split()
V = int(data[0])
P = int(data[1])
q = V // P
r = V % P
for i in range(P):
    if i < r:
        print(q + 1)
    else:
        print(q)