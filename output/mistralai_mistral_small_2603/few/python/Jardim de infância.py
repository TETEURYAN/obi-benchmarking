
import sys

def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def dot(o, a, b):
    return (a[0] - o[0])*(b[0] - o[0]) + (a[1] - o[1])*(b[1] - o[1])

def read_point():
    x, y = map(int, sys.stdin.readline().split())
    return (x, y)

def main():
    points = [read_point() for _ in range(7)]

    P1, P2, P3, P4, P5, P6, P7 = points

    # Condition 1: Angle P2P1P3 is acute (vertex at P1)
    v1 = (P2[0] - P1[0], P2[1] - P1[1])
    v2 = (P3[0] - P1[0], P3[1] - P1[1])
    dot_product = v1[0]*v2[0] + v1[1]*v2[1]
    len1 = (v1[0]**2 + v1[1]**2)**0.5
    len2 = (v2[0]**2 + v2[1]**2)**0.5
    if dot_product <= 0 or len1 == 0 or len2 == 0:
        print("N")
        return

    # Condition 2: Segments P1P2 and P1P3 have the same length
    if not (abs(len1 - len2) < 1e-9):
        print("N")
        return

    # Condition 3: Points P2, P3, P4, P5 are colinear
    if cross(P2, P3, P4) != 0 or cross(P3, P4, P5) != 0:
        print("N")
        return

    # Condition 4: Midpoints of P2P3 and P4P5 coincide
    mid1 = ((P2[0] + P3[0])/2, (P2[1] + P3[1])/2)
    mid2 = ((P4[0] + P5[0])/2, (P4[1] + P5[1])/2)
    if not (abs(mid1[0] - mid2[0]) < 1e-9 and abs(mid1[1] - mid2[1]) < 1e-9):
        print("N")
        return

    # Condition 5: Segment P2P3 is longer than P4P5
    len_p2p3 = ((P3[0] - P2[0])**2 + (P3[1] - P2[1])**2)**0.5
    len_p4p5 = ((P5[0] - P4[0])**2 + (P5[1] - P4[1])**2)**0.5
    if len_p2p3 <= len_p4p5 + 1e-9:
        print("N")
        return

    # Condition 6: Segments P4P6 and P5P7 are perpendicular to P2P3
    dir_p2p3 = (P3[0] - P2[0], P3[1] - P2[1])
    len_dir = (dir_p2p3[0]**2 + dir_p2p3[1]**2)**0.5
    if len_dir < 1e-9:
        print("N")
        return
    dir_p2p3 = (dir_p2p3[0]/len_dir, dir_p2p3[1]/len_dir)

    v4p6 = (P6[0] - P4[0], P6[1] - P4[1])
    v5p7 = (P7[0] - P5[0], P7[1] - P5[1])

    dot4 = v4p6[0]*dir_p2p3[0] + v4p6[1]*dir_p2p3[1]
    dot5 = v5p7[0]*dir_p2p3[0] + v5p7[1]*dir_p2p3[1]

    if abs(dot4) > 1e-9 or abs(dot5) > 1e-9:
        print("N")
        return

    # Condition 7: Segments P4P6 and P5P7 have the same length
    len_p4p6 = (v4p6[0]**2 + v4p6[1]**2)**0.5
    len_p5p7 = (v5p7[0]**2 + v5p7[1]**2)**0.5
    if abs(len_p4p6 - len_p5p7) > 1e-9:
        print("N")
        return

    # Condition 8: Points P1 and P6 are on opposite sides of the line P2P3
    side_p1 = cross(P2, P3, P1)
    side_p6 = cross(P2, P3, P6)
    if side_p1 * side_p6 > 0:
        print("N")
        return

    print("S")

if __name__ == "__main__":
    main()
