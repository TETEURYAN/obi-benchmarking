import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    piles = list(map(int, data[2:2+n]))
    
    # Count frequency of each distinct value
    from collections import Counter
    freq = Counter(piles)
    distinct_values = sorted(freq.keys())
    num_distinct = len(distinct_values)
    
    if num_distinct <= k:
        print(0)
        return
    
    # We need to reduce distinct values to at most k
    # We can only increase pile heights (add coins)
    # We want to minimize total coins added
    
    # Strategy: choose which distinct values to KEEP (at most k of them)
    # For values not kept, we must raise all their piles to some kept value >= that value
    # We want to minimize total additions
    
    # For each subset of k values to keep from distinct_values,
    # compute the cost of converting all other piles to one of the kept values
    # Each pile with value v (not kept) must be raised to the smallest kept value >= v
    # If no kept value >= v exists, it's impossible (we can't lower piles)
    
    # Since N, values <= 500, we can try all combinations of k values from distinct_values
    # But num_distinct can be up to 500, and k can be 1, so C(500,1) is fine
    # C(500, 250) is too large... need smarter approach
    
    # Key insight: the kept values must be chosen such that for every non-kept value,
    # there exists a kept value >= it. So the minimum kept value must be <= minimum of all values,
    # OR all values below the minimum kept value must be "absorbed" upward.
    # Actually: for a pile of height v not kept, we raise it to the smallest kept value >= v.
    # If no kept value >= v, impossible. So we must keep at least one value >= every non-kept value.
    # This means: the maximum value must always be kept (or we can raise to it).
    # Actually the largest value must be kept, because we can't raise beyond it without keeping something larger.
    # Wait - we CAN add coins to raise to any value, not just existing ones!
    # But we want to keep only k distinct values in the end. Those k values can be ANY values >= original.
    # However, to minimize coins, the target values should be existing values (no point going higher than needed).
    
    # So optimal: choose k target values from existing distinct values (sorted),
    # and each pile goes to the smallest target value >= its current value.
    # The largest distinct value must be one of the targets (otherwise piles at max value have nowhere to go).
    
    distinct_sorted = sorted(distinct_values)
    
    # We must always include the maximum value as a target
    # Then choose k-1 more from the remaining distinct values
    # For each combination, compute cost
    
    max_val = distinct_sorted[-1]
    remaining = distinct_sorted[:-1]  # exclude max_val
    
    # Number of remaining distinct values
    r = len(remaining)
    need_choose = k - 1  # how many more to choose from remaining
    
    if need_choose >= r:
        # We keep all values, cost = 0 (already handled above, but just in case)
        print(0)
        return
    
    # For each combination of need_choose values from remaining, plus max_val:
    # compute cost
    
    best = float('inf')
    
    for chosen in combinations(range(r), need_choose):
        targets = sorted([remaining[i] for i in chosen] + [max_val])
        
        cost = 0
        feasible = True
        for v in distinct_sorted:
            if v in set(targets):
                continue
            # find smallest target >= v
            found = False
            for t in targets:
                if t >= v:
                    cost += (t - v) * freq[v]
                    found = True
                    break
            if not found:
                feasible = False
                break
        
        if feasible and cost < best:
            best = cost
    
    print(best)

solve()