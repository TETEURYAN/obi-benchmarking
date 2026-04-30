import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    v = [int(input_data[i+1]) for i in range(n)]
    
    # We need to find maximum subsequence (preserving order) such that:
    # 1. No two consecutive elements are equal
    # 2. At most 2 distinct values
    
    # Get all distinct values
    distinct = list(set(v))
    
    best = 0
    
    # Try all pairs of distinct values (including single values)
    # For a single value a: subsequence can have at most 1 element (since no two consecutive equal)
    # Actually for single value, we can only pick 1 element
    
    # For pair (a, b): pick subsequence from v using only a and b, no two consecutive equal
    # This is equivalent to: filter v keeping only a and b, then from that filtered sequence,
    # pick maximum subsequence with no two consecutive equal
    # But we can also skip elements in the filtered sequence
    
    # Wait - we need to pick a subsequence of the original sequence.
    # The subsequence must use only values from {a} or {a, b}
    # and no two consecutive elements in the subsequence are equal.
    
    # For a fixed set of at most 2 values, we filter the original sequence to keep only those values.
    # Then we want the longest subsequence of this filtered sequence with no two consecutive equal elements.
    # Since we can skip elements, the optimal strategy is greedy:
    # go through filtered sequence and add element if it differs from last added.
    
    # For single value a: filtered sequence is all a's, longest subsequence with no two consecutive = 1
    # For pair (a, b): filtered sequence alternates or has runs, greedy gives max
    
    # Single values
    for a in distinct:
        # Can only pick 1
        best = max(best, 1)
    
    # Pairs
    if len(distinct) >= 2:
        for a, b in combinations(distinct, 2):
            # Filter sequence to only a and b
            filtered = [x for x in v if x == a or x == b]
            # Greedy: pick elements with no two consecutive equal
            count = 0
            last = -1
            for x in filtered:
                if x != last:
                    count += 1
                    last = x
            best = max(best, count)
    
    print(best)

solve()