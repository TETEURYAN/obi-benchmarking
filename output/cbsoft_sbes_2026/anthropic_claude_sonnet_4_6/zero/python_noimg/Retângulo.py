import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    L = list(map(int, input_data[1:n+1]))
    
    total = sum(L)
    half = total
    
    # For a rectangle inscribed in a circle, opposite sides must subtend equal arcs
    # and the sum of arcs for each pair of opposite vertices must equal half the circumference
    # Actually, for a rectangle inscribed in a circle:
    # The diagonals are diameters, so each diagonal divides the circle into two equal halves
    # We need to find 4 trees at positions i, j, k, l (in order) such that
    # arc(i to k) = arc(k to i) = total/2 (diagonals are diameters)
    # AND arc(i to j) = arc(k to l) AND arc(j to k) = arc(l to i)
    # 
    # Actually for a rectangle inscribed in a circle, we just need:
    # arc(i to k) = total/2 AND arc(j to l) = total/2
    # where i,j,k,l are in order around the circle
    # This means: sum of arcs from i to k (going one way) = total/2
    # AND sum of arcs from j to l (going one way) = total/2
    
    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + L[i]
    
    # total must be even for any rectangle to exist
    if total % 2 != 0:
        print("N")
        return
    
    half = total // 2
    
    # Find all pairs (i, j) where sum of arcs from i to j = half
    # i.e., prefix[j] - prefix[i] = half for some i < j
    # These represent pairs of antipodal points (diametrically opposite)
    
    # We need two such pairs that interleave on the circle
    # i.e., pairs (i,k) and (j,l) where i < j < k < l
    
    # Find all starting indices where a half-arc begins
    # For each i, check if there's a j such that prefix[j] - prefix[i] = half
    
    prefix_set = {}
    for i in range(n + 1):
        prefix_set[prefix[i]] = i
    
    # Find all pairs
    antipodal_pairs = []
    for i in range(n):
        target = prefix[i] + half
        if target in prefix_set:
            j = prefix_set[target]
            if j <= n and j > i:
                antipodal_pairs.append((i, j))
    
    # Now check if any two pairs interleave
    # Pairs (i, k) and (j, l) interleave if i < j < k < l
    # Since all pairs have form (i, j) with i < j, we need two pairs (a,b) and (c,d)
    # such that a < c < b < d or c < a < d < b
    
    if len(antipodal_pairs) < 2:
        print("N")
        return
    
    # Sort by first element
    antipodal_pairs.sort()
    
    # For each pair (a, b), find if there's another pair (c, d) with a < c < b < d
    # or c < a < d < b
    
    # Use a sweep: for pairs sorted by start, check if any pair starts inside another
    m = len(antipodal_pairs)
    
    # Check all pairs of antipodal pairs for interleaving
    # With up to n pairs, we need efficient check
    # Sort by first element, then for each pair check if there's a pair starting in (a, b)
    # with end > b
    
    # Build sorted list of (start, end)
    pairs = antipodal_pairs
    
    # For each pair (a, b), we want to know if there exists (c, d) with a < c < b and d > b
    # Since d = c + (n - something)... actually d is fixed given c
    # 
    # Sort pairs by start. For each pair i=(a,b), binary search for pairs with start in (a,b)
    # and check if their end > b
    
    starts = [p[0] for p in pairs]
    
    for i in range(m):
        a, b = pairs[i]
        # Find pairs with start in (a, b)
        lo = bisect_right(starts, a)
        hi = bisect_left(starts, b)
        for j in range(lo, hi):
            c, d = pairs[j]
            if d > b:
                print("S")
                return
    
    print("N")

from bisect import bisect_left, bisect_right
solve()