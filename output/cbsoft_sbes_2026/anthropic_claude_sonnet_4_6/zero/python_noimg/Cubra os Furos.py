import math
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 0
    
    while idx < len(input_data):
        n = int(input_data[idx]); idx += 1
        if n == 0:
            break
        
        test_num += 1
        holes = []
        for _ in range(n):
            x = int(input_data[idx]); idx += 1
            y = int(input_data[idx]); idx += 1
            holes.append((x, y))
        
        if n == 1:
            # Only one hole, the piece just needs to cover itself
            # diameter = 5 (just the axis fits in the hole)
            print(f"Teste {test_num}")
            print(5)
            print()
            continue
        
        # For each hole as the axis hole, find the maximum distance to any other hole
        # The piece diameter must be at least 2 * max_dist + 5
        # (center of piece at axis hole, must cover all other holes including their radius 2.5mm)
        # Actually: the piece is circular centered at axis hole
        # A hole at distance d from axis is covered if the piece radius >= d + 2.5
        # So piece diameter >= 2*(d + 2.5) = 2*d + 5
        # We want to minimize over all choices of axis hole the maximum required diameter
        
        min_diameter = float('inf')
        
        for i in range(n):
            ax, ay = holes[i]
            max_dist = 0.0
            for j in range(n):
                if i == j:
                    continue
                dx = holes[j][0] - ax
                dy = holes[j][1] - ay
                dist = math.sqrt(dx*dx + dy*dy)
                if dist > max_dist:
                    max_dist = dist
            
            # diameter needed = 2 * max_dist + 5
            diameter = 2 * max_dist + 5
            if diameter < min_diameter:
                min_diameter = diameter
        
        print(f"Teste {test_num}")
        print(round(min_diameter))
        print()

solve()