import sys

a = list(map(int, sys.stdin.read().split()))

def triangle(x, y, z):
    return x < y + z and y < x + z and z < x + y

ans = (
    triangle(a[0], a[1], a[2]) or
    triangle(a[0], a[1], a[3]) or
    triangle(a[0], a[2], a[3]) or
    triangle(a[1], a[2], a[3])
)

print('S' if ans else 'N')