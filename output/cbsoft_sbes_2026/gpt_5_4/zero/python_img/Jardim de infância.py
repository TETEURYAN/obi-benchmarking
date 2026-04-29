import sys

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def norm2(a):
    return a[0] * a[0] + a[1] * a[1]

pts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(7)]
P1, P2, P3, P4, P5, P6, P7 = pts

ok = True

# 1) angle P2P1P3 is acute
v12 = sub(P2, P1)
v13 = sub(P3, P1)
if dot(v12, v13) <= 0:
    ok = False

# 2) P1P2 == P1P3
if norm2(v12) != norm2(v13):
    ok = False

# Base direction
b = sub(P3, P2)

# 3) P2, P3, P4, P5 are collinear
if cross(b, sub(P4, P2)) != 0 or cross(b, sub(P5, P2)) != 0:
    ok = False

# 4) midpoints of P2P3 and P4P5 coincide
if P2[0] + P3[0] != P4[0] + P5[0] or P2[1] + P3[1] != P4[1] + P5[1]:
    ok = False

# 5) |P2P3| > |P4P5|
if norm2(sub(P3, P2)) <= norm2(sub(P5, P4)):
    ok = False

# 6) P4P6 and P5P7 perpendicular to P2P3
v46 = sub(P6, P4)
v57 = sub(P7, P5)
if dot(v46, b) != 0 or dot(v57, b) != 0:
    ok = False

# 7) P4P6 == P5P7
if norm2(v46) != norm2(v57):
    ok = False

# 8) segment P1P6 intersects the line through P2P3 in exactly one point
c1 = cross(b, sub(P1, P2))
c2 = cross(b, sub(P6, P2))
if c1 == 0 or c2 == 0 or c1 * c2 >= 0:
    ok = False

print("S" if ok else "N")