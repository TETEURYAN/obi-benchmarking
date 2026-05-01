
import math

def read_points():
    points = []
    for _ in range(7):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def dist2(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def sub(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

def main():
    pts = read_points()
    P1, P2, P3, P4, P5, P6, P7 = pts
    
    # Condition 1: angle P2P1P3 is acute (vertex at P1)
    v12 = sub(P2, P1)
    v13 = sub(P3, P1)
    dot_val = dot(v12, v13)
    if dot_val <= 0:
        print("N")
        return
    
    # Condition 2: |P1P2| == |P1P3|
    if dist2(P1, P2) != dist2(P1, P3):
        print("N")
        return
    
    # Condition 3: P2, P3, P4, P5 are collinear
    # Check P2P3P4 collinear and P2P3P5 collinear
    v23 = sub(P3, P2)
    v24 = sub(P4, P2)
    v25 = sub(P5, P2)
    if cross(v23, v24) != 0:
        print("N")
        return
    if cross(v23, v25) != 0:
        print("N")
        return
    
    # Condition 4: midpoints of P2P3 and P4P5 are coincident
    # mid P2P3 = ((P2x+P3x)/2, (P2y+P3y)/2)
    # mid P4P5 = ((P4x+P5x)/2, (P4y+P5y)/2)
    # Use integer arithmetic: 2*mid
    if (P2[0]+P3[0]) != (P4[0]+P5[0]):
        print("N")
        return
    if (P2[1]+P3[1]) != (P4[1]+P5[1]):
        print("N")
        return
    
    # Condition 5: |P2P3| > |P4P5|
    if dist2(P2, P3) <= dist2(P4, P5):
        print("N")
        return
    
    # Condition 6: P4P6 and P5P7 are perpendicular to P2P3
    # P2P3 direction: v23
    # P4P6 direction: sub(P6, P4)
    v46 = sub(P6, P4)
    v57 = sub(P7, P5)
    
    if dot(v23, v46) != 0:
        print("N")
        return
    if dot(v23, v57) != 0:
        print("N")
        return
    
    # Condition 7: |P4P6| == |P5P7|
    if dist2(P4, P6) != dist2(P5, P7):
        print("N")
        return
    
    # Condition 8: P1 and P6 are on opposite sides of the line containing P2P3
    # The line through P2P3: direction v23
    # Sign of cross(v23, sub(P1, P2)) and cross(v23, sub(P6, P2))
    # They must have opposite signs (product < 0)
    sign1 = cross(v23, sub(P1, P2))
    sign6 = cross(v23, sub(P6, P2))
    
    if sign1 == 0 or sign6 == 0:
        print("N")
        return
    
    # Opposite sides means product < 0
    if sign1 * sign6 >= 0:
        print("N")
        return
    
    print("S")

main()
