
import sys

input = sys.stdin.read
data = input().split()
points = []
index = 0
for i in range(7):
    x = int(data[index])
    y = int(data[index + 1])
    points.append((x, y))
    index += 2

P1 = points[0]
P2 = points[1]
P3 = points[2]
P4 = points[3]
P5 = points[4]
P6 = points[5]
P7 = points[6]

def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dot(ax, ay, bx, by):
    return ax * bx + ay * by

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])

def is_acute_angle():
    v12 = vec(P1, P2)
    v13 = vec(P1, P3)
    d = dot(v12[0], v12[1], v13[0], v13[1])
    return d > 0

def same_length_p1p2_p1p3():
    return dist2(P1, P2) == dist2(P1, P3)

def collinear_p2_p3_p4_p5():
    v23 = vec(P2, P3)
    v24 = vec(P2, P4)
    v25 = vec(P2, P5)
    c1 = cross(v23[0], v23[1], v24[0], v24[1])
    c2 = cross(v23[0], v23[1], v25[0], v25[1])
    return c1 == 0 and c2 == 0

def midpoints_coincident():
    mx1 = (P2[0] + P3[0]) // 2
    my1 = (P2[1] + P3[1]) // 2
    mx2 = (P4[0] + P5[0]) // 2
    my2 = (P4[1] + P5[1]) // 2
    return mx1 == mx2 and my1 == my2

def p2p3_longer_than_p4p5():
    return dist2(P2, P3) > dist2(P4, P5)

def perpendicular_p4p6():
    v23 = vec(P2, P3)
    v46 = vec(P4, P6)
    d = dot(v23[0], v23[1], v46[0], v46[1])
    return d == 0

def perpendicular_p5p7():
    v23 = vec(P2, P3)
    v57 = vec(P5, P7)
    d = dot(v23[0], v23[1], v57[0], v57[1])
    return d == 0

def same_length_p4p6_p5p7():
    return dist2(P4, P6) == dist2(P5, P7)

def p1_p6_separated_by_line():
    v23 = vec(P2, P3)
    v21 = vec(P2, P1)
    v26 = vec(P2, P6)
    c1 = cross(v23[0], v23[1], v21[0], v21[1])
    c2 = cross(v23[0], v23[1], v26[0], v26[1])
    return c1 * c2 < 0

if (is_acute_angle() and
    same_length_p1p2_p1p3() and
    collinear_p2_p3_p4_p5() and
    midpoints_coincident() and
    p2p3_longer_than_p4p5() and
    perpendicular_p4p6() and
    perpendicular_p5p7() and
    same_length_p4p6_p5p7() and
    p1_p6_separated_by_line()):
    print("S")
else:
    print("N")
