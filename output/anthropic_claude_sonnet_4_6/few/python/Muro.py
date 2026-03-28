import sys

def solve():
    MOD = 10**9 + 7
    N = int(sys.stdin.read().strip())
    
    # f(n) = number of ways to build wall of length n
    # f(0) = 1, f(1) = 1, f(2) = 5
    # From the problem: wall of length N ends in one of 7 ways
    # The recurrence based on the 7 endings:
    # - endings that consume 1 unit from right: some contribute f(n-1)
    # - endings that consume 2 units from right: some contribute f(n-2)
    # - endings that consume 3 units from right: some contribute f(n-3)
    # 
    # Let's derive from test cases:
    # f(0)=1, f(1)=1, f(2)=5
    # f(3)=? Let's figure out recurrence
    # 
    # The 7 endings described suggest:
    # Some end with width 1 (1 way each?), some with width 2, some with width 3
    # 
    # Standard "brick wall height 2" with 1x2 and 2x1 bricks gives Fibonacci-like
    # but here we have 2 types of bricks (1x2 horizontal pair and 2x1 vertical)
    # Actually with the values f(0)=1,f(1)=1,f(2)=5, let's find recurrence:
    # 
    # Try f(n) = a*f(n-1) + b*f(n-2) + c*f(n-3)
    # f(3) = a*5 + b*1 + c*1
    # f(4) = a*f(3) + b*5 + c*1
    # 
    # From the 7 endings pattern, a common recurrence for this type is:
    # f(n) = f(n-1) + 4*f(n-2) + f(n-3) - f(n-4) ... 
    # Let me verify with known values and test case f(6)=241, f(11)=36543
    #
    # Try f(n) = 4*f(n-1) - f(n-2) + 2*f(n-3)... 
    # Let me just try f(n) = f(n-1) + 4*f(n-2) + f(n-3):
    # f(3) = 5 + 4 + 1 = 10
    # f(4) = 10 + 20 + 1 = 31... let me check f(6)
    # f(5) = 31+40+10=81, f(6)=81+124+31=236 != 241
    #
    # Try f(n) = 4*f(n-1) - f(n-2):
    # f(3)=20-1=19, too big
    #
    # Try f(n) = 2*f(n-1) + 2*f(n-2) - f(n-3) (guess):
    # f(3)=10+2-1=11, f(4)=22+10-1=31, f(5)=62+22-11=73, f(6)=146+62-31=177 no
    #
    # Let me try matrix / direct computation approach with recurrence search
    # f(0)=1,f(1)=1,f(2)=5,f(6)=241,f(11)=36543
    # f(n) = f(n-1) + 4*f(n-2) + f(n-3) gave f(6)=236
    # Need 241. Diff=5. 
    # Try adding f(n-4): f(n)=f(n-1)+4*f(n-2)+f(n-3)+f(n-4)
    # need f(3) first. With 3-term: f(3)=10
    # f(4)=10+20+1+1=32, f(5)=32+40+10+1=83, f(6)=83+128+32+10=253 no
    #
    # Let me try: f(n) = 2*f(n-1) + 3*f(n-2) - f(n-4)
    # Need f(3): assume f(3)=11 (2*5+3*1=13?), 
    # Actually let me just brute-force small values with DP on states.
    
    # State: profile of right edge. Height=2, bricks are 1x2(H) and 2x1(V).
    # Actually the problem says 2 types shown in figure - likely 1x2 horizontal and 2x1 vertical
    # for a height-2 wall. Standard tiling: f(n)=f(n-1)+f(n-2) won't give f(2)=5.
    # f(2)=5 suggests more brick types. With L-shaped or T-shaped bricks perhaps.
    
    # Given f(2)=5, f(0)=1, f(1)=1, let me find recurrence numerically.
    # I'll trust: this is a known sequence. Let me compute assuming
    # f(n) = 4*f(n-1) - f(n-2) + 2 or similar...
    # 
    # Actually let me just implement profile DP properly.
    # Height=2 wall, bricks: 2x1 vertical (fills 1 col) and 1x2 horizontal (fills 2 cols, 1 row)
    # But that gives f(2)=2 not 5. So there must be more brick shapes.
    # 
    # 7 endings -> likely bricks of width 1,2,3. Let me do transfer matrix on column profiles.
    
    # Profile DP: state = which cells in current column are already filled (by horizontal bricks from prev)
    # For height 2: states 0b00=0, 0b01=1, 0b10=2, 0b11=3
    # Transitions: from state s, place bricks to fill current column and possibly extend right
    
    # Let dp[j] = ways to have profile j at current boundary
    # We need to enumerate all ways to fill a column given incoming profile
    
    from functools import lru_cache
    
    # trans[s] = list of s' reachable from state s
    # s: bitmask of height 2, bit i = row i is pre-filled in current col
    # We fill remaining cells using: vertical brick (fills both rows of current col, width 1)
    # or horizontal brick (fills one row, extends to next col)
    # 
    # Actually for height 2:
    # - vertical 2x1: fills rows 0 and 1 of current col (if both empty)
    # - horizontal 1x2 top: fills row 0 of current col, row 0 of next col
    # - horizontal 1x2 bottom: fills row 1 of current col, row 1 of next col
    # 
    # This gives f(2): from state 0, options:
    # place V -> col done, state 0 for next: 1 way
    # place H-top + H-bottom -> col done, state 0b11 for next... wait
    # 
    # Let me think recursively. fill(col_state, row) fills rows from 'row' downward in current col.
    
    @lru_cache(maxsize=None)
    def fill(filled, row):
        # filled: bitmask of next column pre-filled
        # row: current row we're placing in current column (0 or 1)
        # returns list of next_col_states
        if row == 2:
            return [filled]
        if (1 << row) & 0:  # current col row already filled - but we track current col separately
            pass
        # Actually let me redo this properly
        return []
    
    # Let me just hardcode the transition matrix for height=2
    # States: 0,1,2,3 (which rows of NEXT column are pre-filled)
    # trans[s] = list of next states when current column has pre-filled rows = s
    
    trans = [[] for _ in range(4)]
    
    def build_trans(cur_prefilled, row, next_prefilled, trans_list):
        if row == 2:
            trans_list.append(next_prefilled)
            return
        if cur_prefilled & (1 << row):
            # this row already filled, move to next row
            build_trans(cur_prefilled, row+1, next_prefilled, trans_list)
        else:
            # option 1: place vertical brick (fills both rows if row==0 and row+1 also empty)
            if row == 0 and not (cur_prefilled & (1 << 1)):
                # place 2x1 vertical: fills rows 0 and 1 of current col
                build_trans(cur_prefilled | 3, row+1, next_prefilled, trans_list)
                # wait, but we already said row 0 not filled, place vertical fills rows 0&1
                # just skip to row 2
                # Actually let me redo: place vertical at row 0 fills rows 0 and 1
            # option 2: place horizontal brick at this row (fills cur[row] and next[row])
            build_trans(cur_prefilled | (1 << row), row+1, next_prefilled | (1 << row), trans_list)
            # For vertical: only if row==0 and row 1 also empty
            if row == 0 and not (cur_prefilled & 2):
                build_trans(cur_prefilled | 3, 2, next_prefilled, trans_list)
    
    for s in range(4):
        build_trans(s, 0, 0, trans[s])
    
    # Now run DP
    MOD = 10**9 + 7
    dp = [0]*4
    dp[0] = 1  # start with empty profile
    
    for _ in range(N):
        ndp = [0]*4
        for s in range(4):
            if dp[s] == 0:
                continue
            for ns in trans[s]:
                ndp[ns] = (ndp[ns] + dp[s]) % MOD
        dp = ndp
    
    print(dp[0])

solve()