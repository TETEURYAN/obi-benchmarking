import sys

def solve():
    data = sys.stdin.read().split()
    pts = []
    for i in range(7):
        x = int(data[2*i])
        y = int(data[2*i+1])
        pts.append((x, y))
    
    P1, P2, P3, P4, P5, P6, P7 = pts
    
    def dot(ax, ay, bx, by):
        return ax*bx + ay*by
    
    def cross(ax, ay, bx, by):
        return ax*by - ay*bx
    
    def dist2(A, B):
        return (A[0]-B[0])**2 + (A[1]-B[1])**2
    
    # Condition 1: angle P2P1P3 is acute (vertex at P1)
    # vectors P1->P2 and P1->P3, dot product > 0
    v12x = P2[0] - P1[0]
    v12y = P2[1] - P1[1]
    v13x = P3[0] - P1[0]
    v13y = P3[1] - P1[1]
    
    dot_val = dot(v12x, v12y, v13x, v13y)
    if dot_val <= 0:
        print("N")
        return
    
    # Condition 2: |P1P2| == |P1P3|
    if dist2(P1, P2) != dist2(P1, P3):
        print("N")
        return
    
    # Condition 3: P2, P3, P4, P5 are collinear
    # Check cross products
    # Vector P2->P3
    d23x = P3[0] - P2[0]
    d23y = P3[1] - P2[1]
    
    # P2->P4
    d24x = P4[0] - P2[0]
    d24y = P4[1] - P2[1]
    
    # P2->P5
    d25x = P5[0] - P2[0]
    d25y = P5[1] - P2[1]
    
    if cross(d23x, d23y, d24x, d24y) != 0:
        print("N")
        return
    if cross(d23x, d23y, d25x, d25y) != 0:
        print("N")
        return
    
    # Condition 4: midpoints of P2P3 and P4P5 are coincident
    # midpoint P2P3: (P2+P3)/2, midpoint P4P5: (P4+P5)/2
    # Use integer arithmetic: 2*mid
    mid23x = P2[0] + P3[0]
    mid23y = P2[1] + P3[1]
    mid45x = P4[0] + P5[0]
    mid45y = P4[1] + P5[1]
    
    if mid23x != mid45x or mid23y != mid45y:
        print("N")
        return
    
    # Condition 5: |P2P3| > |P4P5|
    len23_2 = dist2(P2, P3)
    len45_2 = dist2(P4, P5)
    
    if len23_2 <= len45_2:
        print("N")
        return
    
    # Condition 6: P4P6 and P5P7 are perpendicular to P2P3
    # P2P3 direction: (d23x, d23y)
    # P4->P6 direction: (P6-P4)
    d46x = P6[0] - P4[0]
    d46y = P6[1] - P4[1]
    d57x = P7[0] - P5[0]
    d57y = P7[1] - P5[1]
    
    # Perpendicular to P2P3 means dot with P2P3 direction = 0
    if dot(d23x, d23y, d46x, d46y) != 0:
        print("N")
        return
    if dot(d23x, d23y, d57x, d57y) != 0:
        print("N")
        return
    
    # Condition 7: |P4P6| == |P5P7|
    if dist2(P4, P6) != dist2(P5, P7):
        print("N")
        return
    
    # Condition 8: P1 and P6 are on opposite sides of the line containing P2P3
    # Line P2P3: direction (d23x, d23y)
    # Sign of cross(P2P3, P2->point) for P1 and P6
    # P2->P1
    d21x = P1[0] - P2[0]
    d21y = P1[1] - P2[1]
    # P2->P6
    d26x = P6[0] - P2[0]
    d26y = P6[1] - P2[1]
    
    sign1 = cross(d23x, d23y, d21x, d21y)
    sign6 = cross(d23x, d23y, d26x, d26y)
    
    # They must be on opposite sides: sign1 * sign6 < 0
    # Also neither should be on the line (sign != 0)
    if sign1 == 0 or sign6 == 0:
        print("N")
        return
    
    if sign1 * sign6 >= 0:
        print("N")
        return
    
    print("S")

solve()