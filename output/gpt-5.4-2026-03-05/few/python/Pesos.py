import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    exit()

n = data[0]
w = data[1:1+n]

reachable = 1  # bit i set => possible to have exactly i boxes already on 2nd floor, with elevator at 1st floor
for i in range(n):
    wi = w[i]
    mask = 0
    j = i
    while j >= 0 and wi - w[j] <= 8:
        mask |= 1 << j
        j -= 1
    if i <= 8:
        mask |= 1 << (i + 1)  # send wi up with empty cabin down
    if reachable & mask:
        reachable |= 1 << (i + 1)

print('S' if (reachable >> n) & 1 else 'N')