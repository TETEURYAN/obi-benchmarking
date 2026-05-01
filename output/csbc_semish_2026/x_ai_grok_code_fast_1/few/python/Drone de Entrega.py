import sys

data = list(map(int, sys.stdin.read().split()))
A, B, C, H, L = data

if (A <= H and B <= L) or (A <= L and B <= H) or \
   (A <= H and C <= L) or (A <= L and C <= H) or \
   (B <= H and C <= L) or (B <= L and C <= H):
    print('S')
else:
    print('N')