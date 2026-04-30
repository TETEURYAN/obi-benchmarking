import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    
    while idx < len(input_data):
        N = int(input_data[idx]); idx += 1
        
        if N == 0:
            break
        
        # Initialize intersection with first rectangle
        # Upper-left corner: max X (leftmost right), min Y (topmost bottom)
        # Wait, need to think about coordinate system
        # X,Y is upper-left, U,V is lower-right
        # So X <= U and Y >= V (since upper is larger Y, lower is smaller Y)
        
        # Intersection:
        # left = max of all X's
        # right = min of all U's
        # top = min of all Y's (smallest top = most restrictive top)
        # bottom = max of all V's (largest bottom = most restrictive bottom)
        
        rects = []
        for _ in range(N):
            X = int(input_data[idx]); idx += 1
            Y = int(input_data[idx]); idx += 1
            U = int(input_data[idx]); idx += 1
            V = int(input_data[idx]); idx += 1
            rects.append((X, Y, U, V))
        
        # X,Y upper-left means X is left coordinate, Y is top coordinate
        # U,V lower-right means U is right coordinate, V is bottom coordinate
        # In standard math: top Y > bottom V
        # Intersection: left = max(X), right = min(U), top = min(Y), bottom = max(V)
        
        left = max(r[0] for r in rects)
        top = min(r[1] for r in rects)
        right = min(r[2] for r in rects)
        bottom = max(r[3] for r in rects)
        
        print(f"Teste {test_num}")
        
        # Check if intersection is valid
        # left < right and bottom < top (since top > bottom in this coordinate system)
        if left < right and bottom < top:
            print(f"{left} {top} {right} {bottom}")
        else:
            print("nenhum")
        
        print()
        test_num += 1

solve()