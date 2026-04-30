import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(input_data):
        N = int(input_data[idx]); idx += 1
        
        if N == 0:
            break
        
        # Read first rectangle
        X, Y, U, V = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])
        idx += 4
        
        # Normalize: left, top, right, bottom
        # X,Y = upper-left, U,V = lower-right
        # In coordinate system: upper-left means smaller x, larger y (or just use as given)
        # left = X, right = U, top = Y, bottom = V
        left = X
        right = U
        top = Y
        bottom = V
        
        for _ in range(N - 1):
            x, y, u, v = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])
            idx += 4
            
            left = max(left, x)
            right = min(right, u)
            top = min(top, y)
            bottom = max(bottom, v)
        
        print(f"Teste {test_num}")
        
        # Check if intersection is valid
        # left <= right and top >= bottom (since top is upper-left y, bottom is lower-right y)
        # upper-left y >= lower-right y means valid rectangle in standard screen coords
        # But we need to check: X <= U and Y >= V for valid rectangle
        # intersection: left <= right and top >= bottom
        if left <= right and top >= bottom:
            print(f"{left} {top} {right} {bottom}")
        else:
            print("nenhum")
        
        print()
        test_num += 1

solve()