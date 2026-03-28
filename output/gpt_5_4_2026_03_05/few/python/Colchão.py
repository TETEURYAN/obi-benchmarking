import sys

data = list(map(int, sys.stdin.read().split()))
A, B, C, H, L = data

door1, door2 = sorted((H, L))
dims = [A, B, C]

ok = False
pairs = [(dims[0], dims[1]), (dims[0], dims[2]), (dims[1], dims[2])]
for x, y in pairs:
    p, q = sorted((x, y))
    if p <= door1 and q <= door2:
        ok = True
        break

print('S' if ok else 'N')