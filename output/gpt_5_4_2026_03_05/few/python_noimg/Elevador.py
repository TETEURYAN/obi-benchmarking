import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
w = data[1:1+n]

w.sort()

reachable = 0
i = 0
while i < n:
    if w[i] > reachable + 8:
        print('N')
        sys.exit()
    if w[i] > reachable:
        reachable = w[i]
    i += 1

print('S')