Looking at this problem:

- We have a bar with N positions
- The control slides between consecutive positions in the sequence
- We need to count how many times each digit (0-9) appears "inside the control" as it moves

Key insight: When the control moves from position A to position B, it covers all positions between A and B (inclusive of both endpoints, but we need to be careful about double-counting endpoints since they're shared between consecutive moves).

Actually, let me think more carefully. The control starts at position 1, then moves to each position in sequence. Each "slide" covers a range. The total coverage is the union... but wait, the problem says "quantas vezes cada inteiro vai aparecer dentro do controle" - it counts appearances, not unique positions.

So each time the control passes through a position (in any slide), that position's digit is counted. But endpoints are shared between consecutive slides - position 1 is the start, then we go to 9 (covering 1-9), then to 4 (covering 4-9), then to 11 (covering 4-11), then to 13 (covering 11-13).

Let me verify with the example:
- 1→9: positions 1,2,3,4,5,6,7,8,9 → digits: 9,4,3,9,1,2,4,5,1
- 9→4: positions 4,5,6,7,8,9 (9 already counted) → digits: 9,1,2,4,5,1
- 4→11: positions 4,5,6,7,8,9,10,11 (4 already counted) → digits: 1,2,4,5,1,1,9,7
- 11→13: positions 11,12,13 (11 already counted) → digits: 9,7,0... wait

Let me recount. Each segment: start is shared with previous end, so we count start only for the first segment, then for subsequent segments we skip the start (it was the end of previous).

Segment 1→9: positions 1..9
Segment 9→4: positions 5..9 (skip 9, go backwards to 4, so positions 4..8, skip 9) → actually 4,5,6,7,8
Segment 4→11: positions 5..11 (skip 4)
Segment 11→13: positions 12,13 (skip 11)

Let me use prefix sums for efficiency.

import sys
from itertools import accumulate

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N, M = int(input_data[idx]), int(input_data[idx+1])
    idx += 2
    bar = [int(input_data[idx+i]) for i in range(N)]
    idx += N
    positions = [int(input_data[idx+i]) for i in range(M)]
    idx += M
    
    # prefix count for each digit
    # prefix[i][d] = count of digit d in bar[0..i-1]
    prefix = [[0]*10 for _ in range(N+1)]
    for i in range(N):
        for d in range(10):
            prefix[i+1][d] = prefix[i][d]
        prefix[i+1][bar[i]] += 1
    
    def range_count(l, r):
        # count digits in positions l..r (1-indexed)
        res = [0]*10
        for d in range(10):
            res[d] = prefix[r][d] - prefix[l-1][d]
        return res
    
    total = [0]*10
    
    # First segment: full range from positions[0] to positions[1]
    prev = positions[0]
    # Add first position
    for d in range(10):
        total[d] += prefix[prev][d] - prefix[prev-1][d]
    
    for i in range(1, M):
        curr = positions[i]
        l = min(prev, curr)
        r = max(prev, curr)
        # count l..r but skip prev (already counted)
        # so count l..r minus position prev
        cnt = range_count(l, r)
        for d in range(10):
            total[d] += cnt[d]
        # subtract prev position
        total[bar[prev-1]] -= 1
        prev = curr
    
    print(*total)

solve()