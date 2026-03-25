import sys
import math

def read_points():
    data = sys.stdin.read().strip().split()
    if not data:
        return []
    pts = []
    for i in range(0, 14, 2):
        x = int(data[i])
        y = int(data[i+1])
        pts.append((x, y))
    return pts

def vec(p, q):
    return (q[0] - p[0], q[1] - p[1])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]

def cross(u, v):
    return u[0]*v[1] - u[1]*v[0]

def dist2(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx*dx + dy*dy

def collinear(p, q, r):
    return cross(vec(p, q), vec(p, r)) == 0

def midpoint(p, q):
    return ((p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0)

def perpendicular(u, v):
    return dot(u, v) == 0

def segments_intersect(a, b, c, d):
    # a-b segment, c-d line (infinite)
    # check if segment a-b intersects line c-d at exactly one point
    # and that point is strictly between a and b (not at endpoints for this problem? 
    # condition says "interceptar a reta que contém o segmento P2P3 em um único ponto"
    # we interpret as: line through P2P3 intersects segment P1P6 at exactly one point,
    # and that point is interior to segment P1P6 (not at endpoints).
    # Use orientation test.
    def orient(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0
    o1 = orient(c, d, a)
    o2 = orient(c, d, b)
    if o1 == 0 and o2 == 0:
        # colinear
        return False
    if o1 == o2:
        # both on same side of line
        return False
    # now check if intersection point is strictly between a and b
    # line intersection parameter t for segment a + t*(b-a)
    # solve: a + t*(b-a) = c + s*(d-c)
    # we only need t
    denom = (b[0]-a[0])*(d[1]-c[1]) - (b[1]-a[1])*(d[0]-c[0])
    if denom == 0:
        return False
    t = ((a[0]-c[0])*(d[1]-c[1]) - (a[1]-c[1])*(d[0]-c[0])) / denom
    return 0.0 < t < 1.0

def main():
    pts = read_points()
    if len(pts) != 7:
        return
    P1, P2, P3, P4, P5, P6, P7 = pts

    # 1. angle P2 P1 P3 is acute (vertex at P1)
    v12 = vec(P1, P2)
    v13 = vec(P1, P3)
    if dot(v12, v13) <= 0:
        print("N")
        return

    # 2. P1P2 == P1P3
    if dist2(P1, P2) != dist2(P1, P3):
        print("N")
        return

    # 3. P2, P3, P4, P5 are collinear
    if not (collinear(P2, P3, P4) and collinear(P2, P3, P5)):
        print("N")
        return

    # 4. midpoints of P2P3 and P4P5 coincide
    m23 = midpoint(P2, P3)
    m45 = midpoint(P4, P5)
    if abs(m23[0] - m45[0]) > 1e-9 or abs(m23[1] - m45[1]) > 1e-9:
        print("N")
        return

    # 5. length P2P3 > length P4P5
    if dist2(P2, P3) <= dist2(P4, P5):
        print("N")
        return

    # 6. P4P6 ⟂ P2P3 and P5P7 ⟂ P2P3
    v23 = vec(P2, P3)
    v46 = vec(P4, P6)
    v57 = vec(P5, P7)
    if not (perpendicular(v46, v23) and perpendicular(v57, v23)):
        print("N")
        return

    # 7. P4P6 == P5P7
    if dist2(P4, P6) != dist2(P5, P7):
        print("N")
        return

    # 8. P1 and P6 are separated by line through P2P3 (segment P1P6 intersects line P2P3)
    if not segments_intersect(P1, P6, P2, P3):
        print("N")
        return

    print("S")

if __name__ == "__main__":
    main()