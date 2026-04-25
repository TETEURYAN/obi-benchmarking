Looking at this problem, I need to count the number of contiguous subsequences in a range [E, D] where GCD > 1, with point updates.

**Key Insight:** For a range [E, D] of length L, total subsequences = L*(L+1)/2. I need to subtract the number of "non-candidate" subsequences (where GCD = 1).

Actually, let me think differently. Count subsequences where GCD > 1 = total - subsequences where GCD = 1.

But this is complex. Let me think about what makes a subsequence have GCD = 1 vs > 1.

**Alternative approach:** For each position j, find the leftmost position where GCD(S[i..j]) > 1. Actually, let me think about the structure of GCDs.

For a fixed right endpoint j, as we extend left, the GCD values form at most O(log(max_val)) distinct values. A subarray [i,j] is candidate iff GCD > 1.

For a query [E,D], I need sum over j from E to D of (number of i in [E,j] such that GCD(S[i..j]) > 1).

With N, M up to 10^5, I need an efficient approach. Given the constraints, O(N * sqrt(N)) or O(N * log^2(N)) might work.

Since M and N are both 10^5, and updates happen, a segment tree with each node storing enough info seems hard due to GCD complexity.

**Practical approach:** For each query [E,D], iterate j from E to D, maintain the set of distinct GCDs ending at j (at most O(log V) distinct values), count how many have GCD > 1 and start >= E. This is O((D-E+1) * log(V)) per query = O(N log V) per query = O(10^5 * 30) = 3*10^6 per query, times 10^5 queries = too slow.

But in practice, queries might not all be full range. Let me check: worst case is bad. However, for competitive programming at this level with Python, maybe O(N log V) per query with fast I/O is intended, or there's a smarter structure.

Given N=M=10^5 and time limits typical for OBI, let me implement the O(L log V) per query solution and hope it's fast enough, or use PyPy-style optimizations.

For each query [E,D]: iterate right endpoint, maintain list of (gcd_value, leftmost_index) pairs, count those with gcd>1 and left>=E.

import sys
from math import gcd

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    S = [0] + [int(data[idx+i]) for i in range(N)]
    idx += N
    
    out = []
    
    for _ in range(M):
        T = int(data[idx]); idx+=1
        a = int(data[idx]); idx+=1
        b = int(data[idx]); idx+=1
        
        if T == 1:
            S[a] = b
        else:
            E, D = a, b
            # Count candidate subsequences in [E, D]
            # For each right endpoint j, track distinct gcds with their leftmost start
            count = 0
            # current list: list of (gcd_val, start_index) meaning subarray [start..j] has this gcd
            cur = []
            for j in range(E, D+1):
                new_cur = []
                val = S[j]
                # extend all previous
                new_list = []
                for (g, s) in cur:
                    ng = gcd(g, val)
                    if new_list and new_list[-1][0] == ng:
                        # merge: keep leftmost start
                        pass
                    else:
                        new_list.append((ng, s))
                new_list.append((val, j))
                # merge duplicates (same gcd)
                cur = []
                for (g, s) in new_list:
                    if cur and cur[-1][0] == g:
                        pass  # keep first occurrence (leftmost start)
                    else:
                        cur.append((g, s))
                # count subarrays ending at j with gcd > 1
                # cur is sorted by start descending (rightmost first? no, leftmost first)
                # cur[i] covers starts from cur[i][1] to cur[i+1][1]-1
                for i, (g, s) in enumerate(cur):
                    if g > 1:
                        end_s = cur[i+1][1]-1 if i+1 < len(cur) else j
                        count += end_s - s + 1
            out.append(count)
    
    print('\n'.join(map(str, out)))

solve()