import sys

def solve():
    M, N = map(int, input().split())
    
    # Make sure M <= N for easier handling (we'll work with rows = min, cols = max)
    # Actually let's keep M as rows, N as cols
    # 
    # Key insight: knights on a chessboard don't attack if we color in 2x... blocks
    # 
    # The optimal strategy:
    # If min(M,N) == 1: all N (or M) knights can be placed (no attacks possible in 1 row)
    # If min(M,N) == 2: pattern of 2 filled, 2 empty columns (or rows)
    # Otherwise: ceil(M*N/2) - checkerboard coloring (place on all white or black squares)
    #   Actually for larger boards, the answer is ceil(M*N/2)
    
    # Let's think more carefully:
    # For 1xN: answer is N (knights in same row never attack each other)
    # For 2xN: 
    #   Pattern: fill 2 cols, skip 2 cols, fill 2 cols...
    #   For 2 cols: 4 knights
    #   For each group of 4 cols: 4 knights
    #   Remaining cols after groups of 4:
    #     0 rem: 0
    #     1 rem: 2
    #     2 rem: 4
    #     3 rem: 4
    # For MxN where M>=3 and N>=3: ceil(M*N/2)
    
    r, c = M, N
    
    if r > c:
        r, c = c, r
    
    # Now r <= c
    if r == 1:
        print(c)
    elif r == 2:
        # groups of 4 columns
        full_groups = c // 4
        rem = c % 4
        ans = full_groups * 4
        if rem == 1:
            ans += 2
        elif rem == 2:
            ans += 4
        elif rem == 3:
            ans += 4
        print(ans)
    else:
        # r >= 3, c >= 3
        # Answer is ceil(r*c / 2)
        print((r * c + 1) // 2)

solve()