import sys

def solve():
    # Fast I/O reading
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse the 7 points
    points = []
    iterator = iter(input_data)
    try:
        for _ in range(7):
            x = int(next(iterator))
            y = int(next(iterator))
            points.append((x, y))
    except StopIteration:
        return

    P1, P2, P3, P4, P5, P6, P7 = points

    # Helper functions for vector operations
    def sub(p_a, p_b):
        return (p_a[0] - p_b[0], p_a[1] - p_b[1])

    def dot(v_a, v_b):
        return v_a[0] * v_b[0] + v_a[1] * v_b[1]

    def cross(v_a, v_b):
        return v_a[0] * v_b[1] - v_a[1] * v_b[0]

    def dist_sq(p_a, p_b):
        dx = p_a[0] - p_b[0]
        dy = p_a[1] - p_b[1]
        return dx * dx + dy * dy

    # Condition 1: Angle P2 P1 P3 is acute
    # Vectors from P1
    v1_2 = sub(P2, P1)
    v1_3 = sub(P3, P1)
    
    # Acute angle: dot product > 0
    # Not collinear (angle > 0): cross product != 0
    if not (dot(v1_2, v1_3) > 0 and cross(v1_2, v1_3) != 0):
        print("N")
        return

    # Condition 2: Segments P1P2 and P1P3 have the same length
    if dist_sq(P1, P2) != dist_sq(P1, P3):
        print("N")
        return

    # Condition 3: Points P2, P3, P4, P5 are collinear
    # Vector P2 -> P3
    v2_3 = sub(P3, P2)
    # Vector P2 -> P4
    v2_4 = sub(P4, P2)
    # Vector P2 -> P5
    v2_5 = sub(P5, P2)

    if cross(v2_3, v2_4) != 0 or cross(v2_3, v2_5) != 0:
        print("N")
        return

    # Condition 4: Midpoints of P2P3 and P4P5 are coincident
    # P2 + P3 == P4 + P5
    if (P2[0] + P3[0] != P4[0] + P5[0]) or (P2[1] + P3[1] != P4[1] + P5[1]):
        print("N")
        return

    # Condition 5: Segment P2P3 length > P4P5 length
    if not (dist_sq(P2, P3) > dist_sq(P4, P5)):
        print("N")
        return

    # Condition 6: P4P6 and P5P7 perpendicular to P2P3
    # Vector P4 -> P6
    v4_6 = sub(P6, P4)
    # Vector P5 -> P7
    v5_7 = sub(P7, P5)

    if dot(v4_6, v2_3) != 0 or dot(v5_7, v2_3) != 0:
        print("N")
        return

    # Condition 7: Segments P4P6 and P5P7 have the same length
    if dist_sq(P4, P6) != dist_sq(P5, P7):
        print("N")
        return

    # Condition 8: P1 and P6 separated by line P2P3
    # Cross product signs must be opposite
    # v2_3 is P3 - P2
    # v2_1 is P1 - P2
    # v2_6 is P6 - P2
    v2_1 = sub(P1, P2)
    v2_6 = sub(P6, P2)

    cp1 = cross(v2_3, v2_1)
    cp6 = cross(v2_3, v2_6)

    if cp1 * cp6 >= 0:
        print("N")
        return

    print("S")

if __name__ == '__main__':
    solve()