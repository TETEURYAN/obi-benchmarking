Looking at this problem:

- We have N buildings, building j has A[j] apartments
- If someone in apartment i of building j emits sound, it's heard in apartment a of building b if b < j and a - i = j - b
- This means a = i + (j - b), so as we go left from building j, the floor increases
- We need to find the maximum number of apartments (including initial) that can hear the sound

For a sound emitted at apartment i of building j, the apartments that hear it are:
- Building j, apartment i (initial)
- Building j-1, apartment i+1 (if i+1 <= A[j-1])
- Building j-2, apartment i+2 (if i+2 <= A[j-2])
- ...
- Building j-k, apartment i+k (if i+k <= A[j-k])

So we're going diagonally up-left. The count is the number of buildings b (from j going left) where A[b] >= i + (j - b).

For building b at distance d = j - b from j, we need A[b] >= i + d.

To maximize the count, we want to choose j and i optimally.

Key insight: The diagonal is characterized by the value (i - j) = constant = i + (j-b) - j... Let me think differently.

For a fixed starting position (j, i), the count along the diagonal going left is the number of consecutive buildings (including j itself) where A[b] >= i + (j-b).

Let's define for each building b, the "diagonal value" d = apartment - building_index = i - j (constant along a diagonal). For building b on this diagonal, the apartment number is i + (j-b) = (i-j) + b... wait: a = i + (j-b) = i - j + j - b + j... 

Actually a = i + (j - b). If we let c = i - j (can be negative), then a = c + j - b + j... no: a = i + j - b = (i-j) + j + j - b... 

Let me re-index: a = i + (j - b). Let k = j - b (distance), then a = i + k. The diagonal is defined by (i - k) being constant... no, i is fixed, k varies.

The diagonal going left from (j, i): at building j-k, need apartment i+k <= A[j-k].

So count = number of k in {0, 1, ..., j-1} such that A[j-k] >= i+k, and we want consecutive from k=0.

For each building j and each possible starting floor i (1 to A[j]), we want the length of the consecutive run going left where A[j-k] >= i+k.

This is equivalent to: for each diagonal (characterized by value v = i - j, i.e., apartment minus building index), count consecutive buildings from right where A[b] - b >= v... wait: A[b] >= i + k = i + j - b, so A[b] + b >= i + j = constant along the diagonal.

So for diagonal constant C = i + j, we need A[b] + b >= C for buildings b going left from j.

We want to maximize the length of consecutive run of buildings b = j, j-1, j-2, ... where A[b] + b >= C, with C = i + j, 1 <= i <= A[j], so C ranges from 1+j to A[j]+j.

To maximize count, for each building j, we want the longest consecutive run ending at j (going left) where A[b] + b >= some threshold C, and C <= A[j] + j (C >= j+1 means i >= 1).

The best C to pick is the minimum A[b]+b in the run (to include as many as possible). We want the longest suffix ending at j where all A[b]+b >= some C >= j+1.

So for each j, find the longest consecutive sequence ending at j where min(A[b]+b) >= j+1 (since C must be at least j+1).

Let me compute for each j: extend left while A[b]+b >= j+1... but C also must be <= A[j]+j.

Actually C = i+j with i>=1 means C >= j+1, and i <= A[j] means C <= A[j]+j. The constraint is A[b]+b >= C for all b in run, so we need min of A[b]+b in run >= C >= j+1. So as long as min(A[b]+b in run) >= j+1, we can pick C = j+1 (i=1).

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    val = [A[i] + (i+1) for i in range(N)]  # A[i] + building_number (1-indexed)
    
    ans = 0
    # For each building j (1-indexed), find longest run ending at j going left
    # where val[b] >= j+1 (building j is 1-indexed, so threshold = j+1)
    # and val[j-1] >= j+1 (i.e., A[j] >= 1)
    
    length = 0
    for j in range(1, N+1):
        idx = j - 1
        if A[idx] == 0:
            length = 0
        else:
            # val[idx] = A[idx] + j, threshold = j+1, so A[idx] >= 1 which is true
            # But we also need previous buildings: val[b] >= j+1
            # When we move to next j, threshold increases by 1
            # We need to recheck... this greedy won't work directly
            length += 1
            # Check if the leftmost building in current run still satisfies
            # Actually need to track minimum in window
            pass
    
    print(ans)

# Need segment tree or sparse table for range minimum queries
# For each j, binary search on length, check min(val[j-len..j-1]) >= j+1

import sys
from math import log2
input = sys.stdin.readline

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    if N == 0:
        print(0)
        return
    
    val = [A[i] + (i+1) for i in range(N)]
    
    # Sparse table for range minimum
    LOG = max(1, int(log2(N)) + 1) if N > 0 else 1
    sparse = [val[:]]
    for k in range(1, LOG+1):
        prev = sparse[k-1]
        curr = []
        for i in range(N - (1<<k) + 1):
            curr.append(min(prev[i], prev[i + (1<<(k-1))]))
        sparse.append(curr)
    
    def query_min(l, r):  # inclusive
        if l > r:
            return float('inf')
        length = r - l + 1
        k = int(log2(length))
        return min(sparse[k][l], sparse[k][r - (1<<k) + 1])
    
    ans = 0
    for j in range(1, N+1):
        idx = j - 1
        if A[idx] == 0:
            continue
        # Binary search for longest run ending at idx
        lo, hi = 1, j
        while lo < hi:
            mid = (lo + hi + 1) // 2
            # run from idx-mid+1 to idx
            l = idx - mid + 1
            if query_min(l, idx) >= j + 1:
                lo = mid
            else:
                hi = mid - 1
        ans = max(ans, lo)
    
    print(ans)

solve()