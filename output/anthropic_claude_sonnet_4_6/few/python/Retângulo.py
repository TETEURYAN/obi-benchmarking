import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    L = list(map(int, data[1:n+1]))
    
    total = sum(L)
    
    # A rectangle inscribed in a circle must have its diagonals as diameters.
    # So we need to find 4 trees that form a rectangle.
    # For a rectangle inscribed in a circle, opposite vertices are diametrically opposite.
    # This means: if we pick 4 trees at positions i, j, k, l (in order around circle),
    # the arc from i to k (going through j) must equal total/2,
    # and the arc from j to l (going through k) must equal total/2.
    
    # So we need to find two pairs of trees such that each pair is diametrically opposite
    # (arc between them = total/2), and the four trees are distinct and alternate.
    
    # First check: total must be even? No, total/2 just needs to match arc sums.
    # Actually total/2 doesn't need to be integer if arcs are integers... wait arcs are integers.
    # If total is odd, no pair can sum to total/2, so answer is N.
    
    if total % 2 != 0:
        print("N")
        return
    
    half = total // 2
    
    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + L[i]
    
    # For each starting tree i, find if there's a tree j such that arc from i to j = half
    # Arc from tree i to tree j (going counterclockwise, j > i) = prefix[j] - prefix[i]
    # We need prefix[j] - prefix[i] = half
    # i.e., prefix[j] = prefix[i] + half
    
    # Build a set of prefix values with their indices
    # prefix[0], prefix[1], ..., prefix[n-1] are the cumulative arcs starting from tree 0
    # Tree i starts at prefix[i]
    
    prefix_set = {}
    for i in range(n):
        val = prefix[i]
        if val not in prefix_set:
            prefix_set[val] = i
    
    # Find all pairs (i, j) where arc from i to j = half
    # These are "diameter" pairs
    diameter_pairs = []
    
    for i in range(n):
        target = prefix[i] + half
        if target in prefix_set:
            j = prefix_set[target]
            if j != i:
                diameter_pairs.append((i, j))
    
    # Now we need two diameter pairs (i,j) and (k,l) such that they interleave:
    # i < k < j < l or k < i < l < j (when arranged on circle)
    # i.e., one tree from each pair separates the other pair
    
    # For pairs to form a rectangle, the four points must be distinct and interleaved.
    # Given pair (i, j) with i < j, and pair (k, l) with k < l:
    # They interleave if i < k < j < l or k < i < l < j
    
    if len(diameter_pairs) < 2:
        print("N")
        return
    
    # We need to check if any two diameter pairs interleave
    # With up to N diameter pairs, we need efficient check
    # But N can be 10^5, so O(N^2) might be too slow
    
    # Key insight: pairs (i,j) where i < j and prefix[j]-prefix[i]=half
    # Sort pairs by first element
    # For two pairs (a,b) and (c,d) with a<b, c<d, a<c:
    # They interleave iff a < c < b < d
    # i.e., c < b and d > b (since a<c already, and b<d means d>b)
    # i.e., c is between a and b, and d > b
    
    # Sort pairs by i
    diameter_pairs.sort()
    
    # For each pair (i,j), check if there's another pair (k,l) with i < k < j < l
    # We can use a sweep: for pairs sorted by i, maintain a structure
    
    # Actually, let's think differently:
    # Sort pairs by first element. For pair p=(a,b), we want another pair q=(c,d) with a<c<b and d>b.
    # Equivalently c in (a,b) and d > b.
    # 
    # Since each pair has j = prefix_set[prefix[i]+half], and i<j always (by construction),
    # we can check:
    
    # Simple O(N log N) approach:
    # For each pair (i,j), i<j, we want to know if there's a pair (k,l) with i<k<j and l>j.
    # Sort pairs. Use a segment tree or binary search.
    
    # Given constraints N<=10^5, number of diameter pairs <= N.
    # Let's do O(M^2) where M = number of pairs. In worst case M=N/2... too slow.
    
    # Better: sort pairs by i. For each pair (i,j), binary search for pairs with k in (i,j).
    # Among those, check if any has l > j. Track max l for ranges.
    
    pairs = diameter_pairs  # sorted by first element (i)
    
    # For each pair index p, pairs[p] = (i, j), i < j
    # We want pairs[q] = (k, l) with i < k < j and l > j
    
    # Build array of (i, j) sorted by i
    # For a given (i, j), find all k in (i, j) using binary search on first elements
    # Among those pairs, check if max(l) > j
    
    # Precompute: for pairs sorted by i, build a sparse table or segment tree on j values
    # to query max j in a range of indices.
    
    import bisect
    
    firsts = [p[0] for p in pairs]
    seconds = [p[1] for p in pairs]
    
    # Build sparse table for range max on seconds
    m = len(pairs)
    LOG = m.bit_length()
    sparse = [seconds[:]]
    for k in range(1, LOG + 1):
        prev = sparse[k-1]
        curr = []
        for idx in range(m - (1 << k) + 1):
            curr.append(max(prev[idx], prev[idx + (1 << (k-1))]))
        sparse.append(curr)
    
    def query_max(l, r):  # inclusive indices
        if l > r:
            return -1
        length = r - l + 1
        k = length.bit_length() - 1
        return max(sparse[k][l], sparse[k][r - (1 << k) + 1])
    
    found = False
    for p in range(m):
        i, j = pairs[p]
        # Find pairs with first element in (i, j) exclusive
        lo = bisect.bisect_right(firsts, i)
        hi = bisect.bisect_left(firsts, j) - 1
        if lo <= hi:
            max_l = query_max(lo, hi)
            if max_l > j:
                found = True
                break
    
    print("S" if found else "N")

solve()