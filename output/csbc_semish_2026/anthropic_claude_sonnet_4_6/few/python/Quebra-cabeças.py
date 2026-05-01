import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    
    M1 = int(data[idx]); idx += 1
    row1 = []
    for i in range(M1):
        row1.append(int(data[idx])); idx += 1
    
    M2 = int(data[idx]); idx += 1
    row2 = []
    for i in range(M2):
        row2.append(int(data[idx])); idx += 1
    
    # Each piece in row1 can be placed at positions 0..N-1
    # The pieces must maintain their relative order (left to right)
    # Piece i of row1 must be at position >= i and <= N - M1 + i
    # Similarly for row2
    
    # We need to find placements p1[0..M1-1] and p2[0..M2-1]
    # such that p1 is strictly increasing, p2 is strictly increasing
    # p1[i] in [i, N-1-(M1-1-i)]
    # p2[j] in [j, N-1-(M2-1-j)]
    # maximize sum over columns c of (row1_piece_at_c * row2_piece_at_c)
    
    # DP approach:
    # State: (i, j) = next piece index for row1 and row2 to place
    # We process columns left to right, deciding where to place pieces
    # 
    # Actually, let's think of it as: we choose positions for each piece.
    # The value only comes from pairs that share the same column.
    # 
    # DP: dp[i][j] = max value considering we've placed i pieces from row1
    # and j pieces from row2, and we're now at some column position.
    # 
    # Let's define dp[i][j] = maximum sum achievable when we have placed
    # the first i pieces of row1 and first j pieces of row2,
    # and the "current column pointer" is max(pos1[i-1], pos2[j-1]) + 1
    # 
    # Transition: from state (i, j), next piece placed can be:
    # - row1[i] at some column c1 >= max(i, current_col)
    # - row2[j] at some column c2 >= max(j, current_col)
    # - both at same column c (they overlap)
    
    # Let dp[i][j] = best value when i pieces from row1 and j pieces from row2
    # have been placed, and the minimum next column we can use is tracked.
    # The minimum next column is max(i, j) since piece i needs col >= i and piece j needs col >= j.
    # Actually min next col = max(i, j) naturally.
    
    # dp[i][j]: placed i from row1, j from row2
    # next available col = max(i, j)
    # We need: remaining row1 pieces (M1-i) fit in cols [max(i,j)..N-1]: need N - max(i,j) >= M1-i and M2-j
    
    NEG_INF = float('-inf')
    
    # dp[i][j] = max value with i pieces of row1 placed, j pieces of row2 placed
    # transitions: place row1[i] alone, row2[j] alone, or both together
    
    dp = [[NEG_INF] * (M2 + 1) for _ in range(M1 + 1)]
    dp[0][0] = 0
    
    for i in range(M1 + 1):
        for j in range(M2 + 1):
            if dp[i][j] == NEG_INF:
                continue
            cur = dp[i][j]
            # current minimum column = max(i, j)
            col = max(i, j)
            
            # Check feasibility: remaining pieces must fit
            # row1 has M1-i pieces left, row2 has M2-j pieces left
            # they need cols from col to N-1, that's N-col slots
            # We need N - col >= M1 - i and N - col >= M2 - j
            
            # Option 1: place row1[i] alone at column col (or any col, but best is col for DP)
            # Actually we just need to decide: do row1[i] and row2[j] share a column?
            # If not sharing: place whichever comes "first" alone
            # The key insight: optimal placement means we only care about pairs
            # So we can think: for each pair (i,j) decide if they share a column or not
            
            # Place row1[i] alone (no row2 piece at same col)
            if i < M1:
                ni, nj = i + 1, j
                # need col available for row1[i]: col >= i (satisfied since col=max(i,j)>=i)
                # need remaining to fit: N - (col+1) >= (M1-i-1) and N-(col+1) >= (M2-j)
                if N - (col + 1) >= (M1 - i - 1) and N - (col + 1) >= (M2 - j):
                    val = cur + 0  # row2 is 0 at this col
                    if val > dp[ni][nj]:
                        dp[ni][nj] = val
            
            # Place row2[j] alone
            if j < M2:
                ni, nj = i, j + 1
                if N - (col + 1) >= (M1 - i) and N - (col + 1) >= (M2 - j - 1):
                    val = cur + 0
                    if val > dp[ni][nj]:
                        dp[ni][nj] = val
            
            # Place row1[i] and row2[j] together
            if i < M1 and j < M2:
                ni, nj = i + 1, j + 1
                if N - (col + 1) >= (M1 - i - 1) and N - (col + 1) >= (M2 - j - 1):
                    val = cur + row1[i] * row2[j]
                    if val > dp[ni][nj]:
                        dp[ni][nj] = val
    
    print(dp[M1][M2])

solve()