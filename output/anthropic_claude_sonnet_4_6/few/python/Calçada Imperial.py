import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    seq = [int(data[i+1]) for i in range(n)]
    
    best = 0
    
    # Try all pairs (a, b) where a != b, and also single values
    values = list(set(seq))
    
    # Single value case
    for a in values:
        count = 0
        prev = -1
        for v in seq:
            if v == a:
                if v != prev:
                    count += 1
                    prev = v
                # if v == prev, skip (can't mark consecutive equal)
                # but wait - we can choose to skip or not
                # We want maximum subsequence with at most 2 distinct values
                # and no two consecutive equal
                # For single value: we can mark at most 1 (since all same, consecutive would repeat)
                # Actually we can mark every other occurrence... no wait
                # The subsequence must have no two consecutive equal
                # For single value a: we can only mark 1 element
        # Actually for single value, max is 1
        best = max(best, 1)
    
    # For pairs (a, b)
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            a, b = values[i], values[j]
            # Find maximum subsequence using only a and b, no two consecutive equal
            # Greedy: go through seq, pick elements that are a or b, 
            # and don't equal the last picked
            count = 0
            prev = -1
            for v in seq:
                if v == a or v == b:
                    if v != prev:
                        count += 1
                        prev = v
            best = max(best, count)
    
    print(best)

solve()