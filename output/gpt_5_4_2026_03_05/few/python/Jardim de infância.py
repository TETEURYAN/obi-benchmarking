import sys

data = list(map(int, sys.stdin.read().split()))
pts = [(data[i], data[i + 1]) for i in range(0, 14, 2)]
P1, P2, P3, P4, P5, P6, P7 = pts

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def norm2(a):
    return a[0] * a[0] + a[1] * a[1]

ok = True

v12 = sub(P2, P1)
v13 = sub(P3, P1)
if dot(v12, v13) <= 0:
    ok = False

if norm2(v12) != norm2(v13):
    ok = False

d23 = sub(P3, P2)
if cross(d23, sub(P4, P2)) != 0 or cross(d23, sub(P5, P2)) != 0:
    ok = False

if P2[0] + P3[0] != P4[0] + P5[0] or P2[1] + P3[1] != P4[1] + P5[1]:
    ok = False

if norm2(d23) <= norm2(sub(P5, P4)):
    ok = False

d46 = sub(P6, P4)
d57 = sub(P7, P5)
if dot(d46, d23) != 0 or dot(d57, d23) != 0:
    ok = False

if norm2(d46) != norm2(d57):
    ok = False

s1 = cross(d23, sub(P1, P2))
s6 = cross(d23, sub(P6, P2))
if s1 == 0 or s6 == 0 or s1 * s6 >= 0:
    ok = False

print("S" if ok else "N")