import sys

data = sys.stdin.read().split()
if not data:
    exit()

A, B, C = map(int, data[:3])
H, L = map(int, data[3:5])

dim = sorted([A, B, C])
window = sorted([H, L])

if dim[0] <= window[0] and dim[1] <= window[1]:
    print('S')
else:
    print('N')