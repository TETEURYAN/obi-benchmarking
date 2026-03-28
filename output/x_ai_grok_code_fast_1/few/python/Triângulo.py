import sys

data = sys.stdin.read().split()
a, b, c, d = map(int, data)

def is_triangle(x, y, z):
    sides = sorted([x, y, z])
    return sides[0] + sides[1] > sides[2]

if is_triangle(a, b, c) or is_triangle(a, b, d) or is_triangle(a, c, d) or is_triangle(b, c, d):
    print('S')
else:
    print('N')