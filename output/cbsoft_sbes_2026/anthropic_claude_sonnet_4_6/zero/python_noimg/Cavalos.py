import sys

def solve():
    M, N = map(int, input().split())
    
    # Make sure M <= N for simplicity (we can swap)
    if M > N:
        M, N = N, M
    
    # Special cases
    # If M == 1: no knight attacks in a single row, place all N
    # If M == 2: knights in same row don't attack each other
    # Pattern for 2 rows: in groups of 4 columns, we can place 4 knights
    # For general case: color the board like checkerboard
    # Knights always move from white to black and vice versa
    # So we can place all knights of one color = ceil(M*N/2)
    # But wait, that's not always optimal for small boards
    
    # For M=1 or N=1: all cells, no attacks possible
    if M == 1:
        print(N)
        return
    
    # For M=2 (after swap, M<=N, so M=2 means 2 rows)
    # In a 2xN board:
    # Knights in 2 rows: a knight at (r,c) attacks (r±1, c±2) and (r±2, c±1)
    # Since only 2 rows, attacks are only (r±1, c±2)
    # Pattern: place in groups of 4 columns: 
    # cols 0,1: place all 4, cols 2,3: place all 4, etc.
    # Actually for 2xN: answer is 4*(N//4) + min(4, 2*(N%4)) if N%4 != 0
    # Wait let me think again
    # 2x1: 2, 2x2: 4, 2x3: 4, 2x4: 8, 2x5: 8, 2x6: 8... no
    # test case 2x6 = 8
    # 2x4 = 8? Let's check: place all in cols 0,1 (4 knights), all in cols 4,5 (4 knights) = 8 for 2x6
    # Pattern repeats every 4 columns with 4 knights
    if M == 2:
        full_groups = N // 4
        remainder = N % 4
        ans = full_groups * 4
        if remainder == 1:
            ans += 2
        elif remainder == 2:
            ans += 4
        elif remainder == 3:
            ans += 4
        print(ans)
        return
    
    # For M >= 3 and N >= 3:
    # The answer is ceil(M*N / 2)
    # Because we can color the board and place all of one color
    # Knights always attack opposite color, so placing all same color = no attacks
    print((M * N + 1) // 2)

solve()