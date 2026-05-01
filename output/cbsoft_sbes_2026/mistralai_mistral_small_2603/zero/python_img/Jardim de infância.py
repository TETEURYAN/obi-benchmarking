
import math

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dot(o, a, b):
    return (a[0] - o[0]) * (b[0] - o[0]) + (a[1] - o[1]) * (b[1] - o[1])

def norm(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def dist(a, b):
    return norm((a[0]-b[0], a[1]-b[1]))

def angle_acute(p1, p2, p3):
    v1 = (p2[0]-p1[0], p2[1]-p1[1])
    v2 = (p3[0]-p1[0], p3[1]-p1[1])
    dot_product = v1[0]*v2[0] + v1[1]*v2[1]
    if dot_product <= 0:
        return False
    det = v1[0]*v2[1] - v1[1]*v2[0]
    if det == 0:
        return False
    angle = math.atan2(det, dot_product)
    return abs(angle) < math.pi/2

def colinear(p1, p2, p3):
    return abs(cross(p1, p2, p3)) < 1e-9

def perpendicular(a, b, c):
    v1 = (b[0]-a[0], b[1]-a[1])
    v2 = (c[0]-a[0], c[1]-a[1])
    return abs(dot(a, b, c)) < 1e-9

def same_length(a, b, c, d):
    return abs(dist(a, b) - dist(c, d)) < 1e-9

def midpoint(a, b):
    return ((a[0]+b[0])/2, (a[1]+b[1])/2)

def point_on_segment(p, a, b):
    if not colinear(a, p, b):
        return False
    if min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
        return True
    return False

def segments_intersect(a1, a2, b1, b2):
    c1 = cross(a1, a2, b1)
    c2 = cross(a1, a2, b2)
    c3 = cross(b1, b2, a1)
    c4 = cross(b1, b2, a2)
    if (c1 * c2 < 0) and (c3 * c4 < 0):
        return True
    if c1 == 0 and point_on_segment(b1, a1, a2):
        return True
    if c2 == 0 and point_on_segment(b2, a1, a2):
        return True
    if c3 == 0 and point_on_segment(a1, b1, b2):
        return True
    if c4 == 0 and point_on_segment(a2, b1, b2):
        return True
    return False

def point_on_line(p, a, b):
    return abs(cross(a, b, p)) < 1e-9

def point_on_half_plane(p, a, b, c):
    cross_val = cross(a, b, c)
    if cross_val == 0:
        return False
    sign = 1 if cross_val > 0 else -1
    return cross(a, b, p) * sign >= 0

def main():
    points = []
    for _ in range(7):
        x, y = map(int, input().split())
        points.append((x, y))

    P1, P2, P3, P4, P5, P6, P7 = points

    # Condition 1: Angle P2P1P3 is acute
    if not angle_acute(P1, P2, P3):
        print("N")
        return

    # Condition 2: P1P2 and P1P3 have the same length
    if not same_length(P1, P2, P1, P3):
        print("N")
        return

    # Condition 3: P2, P3, P4, P5 are colinear
    if not (colinear(P2, P3, P4) and colinear(P2, P3, P5)):
        print("N")
        return

    # Condition 4: Midpoints of P2P3 and P4P5 are the same
    mid1 = midpoint(P2, P3)
    mid2 = midpoint(P4, P5)
    if not (abs(mid1[0] - mid2[0]) < 1e-9 and abs(mid1[1] - mid2[1]) < 1e-9):
        print("N")
        return

    # Condition 5: P2P3 length > P4P5 length
    len_p2p3 = dist(P2, P3)
    len_p4p5 = dist(P4, P5)
    if len_p2p3 <= len_p4p5:
        print("N")
        return

    # Condition 6: P4P6 and P5P7 are perpendicular to P2P3
    if not (perpendicular(P4, P6, P2) and perpendicular(P5, P7, P2)):
        print("N")
        return

    # Condition 7: P4P6 and P5P7 have the same length
    if not same_length(P4, P6, P5, P7):
        print("N")
        return

    # Condition 8: P1 and P6 are separated by the line P2P3
    # Check if P1 and P6 are on opposite sides of the line P2P3
    cross_p2p3_p1 = cross(P2, P3, P1)
    cross_p2p3_p6 = cross(P2, P3, P6)
    if cross_p2p3_p1 * cross_p2p3_p6 >= 0:
        print("N")
        return

    print("S")

if __name__ == "__main__":
    main()
