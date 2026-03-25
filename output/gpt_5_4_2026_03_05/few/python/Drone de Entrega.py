import sys

data = list(map(int, sys.stdin.read().split()))
A, B, C, H, L = data

h, l = sorted((H, L))
faces = [(A, B), (A, C), (B, C)]

ok = False
for x, y in faces:
    a, b = sorted((x, y))
    if a <= h and b <= l:
        ok = True
        break

print('S' if ok else 'N')