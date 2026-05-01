import math
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(input_data):
        N = int(input_data[idx]); idx += 1
        if N == 0:
            break
        
        holes = []
        for _ in range(N):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            holes.append((x, y))
        
        if N == 1:
            # Only one hole, the piece just needs to cover itself
            # diameter = 5 (the axis fits in the hole, no other holes to cover)
            print(f"Teste {test_num}")
            print(5)
            print()
            test_num += 1
            continue
        
        # For each hole as the axis hole, find the maximum distance to any other hole
        # The piece must cover all other holes completely
        # A hole is covered if the circular piece covers the entire hole circle (radius 2.5mm)
        # The piece center is at the axis hole, radius R of piece
        # To cover a hole at distance d from axis: R >= d + 2.5
        # The piece diameter = 2*R >= 2*d + 5
        # Also the axis hole itself has diameter 5, so piece diameter >= 5
        
        min_diameter = float('inf')
        
        for i in range(N):
            ax, ay = holes[i]
            max_dist = 0
            for j in range(N):
                if i == j:
                    continue
                bx, by = holes[j]
                dist = math.sqrt((ax - bx)**2 + (ay - by)**2)
                if dist > max_dist:
                    max_dist = dist
            # diameter needed = 2 * (max_dist + 2.5) = 2*max_dist + 5
            diameter = 2 * max_dist + 5
            if diameter < min_diameter:
                min_diameter = diameter
        
        # Round to nearest integer (ceiling based on problem)
        diameter_int = math.ceil(min_diameter - 1e-9)
        # Actually based on errata, various roundings are accepted
        # Let's use round
        diameter_int = int(math.ceil(min_diameter - 1e-9))
        
        print(f"Teste {test_num}")
        print(diameter_int)
        print()
        test_num += 1

solve()