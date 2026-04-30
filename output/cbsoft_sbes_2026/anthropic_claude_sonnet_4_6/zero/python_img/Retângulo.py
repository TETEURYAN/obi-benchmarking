import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    L = list(map(int, input_data[1:n+1]))
    
    total = sum(L)
    half = total
    
    # A rectangle inscribed in a circle must have its diagonals as diameters
    # So we need 4 points on the circle such that opposite vertices are diametrically opposite
    # This means: for 4 points A, B, C, D on circle (in order), arc(A to C) = arc(C to A) = half total
    # and arc(B to D) = arc(D to B) = half total
    
    # We need to find 4 trees i, j, k, l (in order) such that:
    # arc(i to k) = total/2 and arc(j to l) = total/2
    # But total must be even? No, arcs are integers but total/2 might not be integer
    # Actually arcs are integers, so total is integer. For rectangle, we need arc(i to k) = total/2
    # If total is odd, impossible
    
    if total % 2 != 0:
        print("N")
        return
    
    half = total // 2
    
    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + L[i]
    
    # For each starting tree i, find if there's a tree k such that arc from i to k = half
    # arc from tree i to tree k (going counterclockwise) = prefix[k] - prefix[i] (if k > i)
    # or prefix[n] - prefix[i] + prefix[k] (if k < i)
    
    # Build a set of prefix sums mod total
    prefix_set = set()
    for i in range(n):
        prefix_set.add(prefix[i])
    
    # For each tree i, check if prefix[i] + half is in prefix_set (mod total)
    # Collect all pairs (i, k) where arc i->k = half
    
    # We need two such pairs that interleave: i < j < k < l (cyclically)
    # where arc(i->k) = half and arc(j->l) = half
    
    # Find all trees that have a diametrically opposite tree
    diameter_pairs = []
    
    for i in range(n):
        target = prefix[i] + half
        if target in prefix_set:
            # tree i pairs with tree at prefix value target
            # find which tree index has prefix[k] = target
            diameter_pairs.append(i)
    
    # diameter_pairs contains indices i where there exists k with arc(i->k) = half
    # We need two pairs (i, k) and (j, l) that interleave on the circle
    
    # Build mapping from prefix value to tree index
    prefix_to_idx = {}
    for i in range(n):
        prefix_to_idx[prefix[i]] = i
    
    # Get actual pairs
    pairs = []
    for i in diameter_pairs:
        target = prefix[i] + half
        if target in prefix_to_idx:
            k = prefix_to_idx[target]
            if i < k:
                pairs.append((i, k))
    
    # Now check if any two pairs (i,k) and (j,l) interleave
    # Two pairs (a,b) and (c,d) with a<b and c<d interleave if a<c<b<d or c<a<d<b
    
    m = len(pairs)
    if m < 2:
        print("N")
        return
    
    # Sort pairs by first element
    pairs.sort()
    
    # For each pair (a,b), check if there's another pair (c,d) with a<c<b<d or c<a<d<b
    # Use a sweep: for pair (a,b), we need a c in (a,b) such that d = partner(c) > b
    
    # Build set of all 'a' values in pairs for quick lookup
    # Actually let's just check all pairs - but m could be up to n = 1e5, so O(m^2) might be too slow
    
    # Better: sort pairs, for each pair (a,b), check if any pair starts in (a,b) and ends after b
    # Use sorted list and binary search
    
    import bisect
    
    starts = [p[0] for p in pairs]
    ends = [p[1] for p in pairs]
    
    for i in range(m):
        a, b = pairs[i]
        # Find pairs with start in (a, b)
        lo = bisect.bisect_right(starts, a)
        hi = bisect.bisect_left(starts, b)
        # Check if any of these have end > b
        for j in range(lo, hi):
            if pairs[j][1] > b:
                print("S")
                return
    
    print("N")

solve()