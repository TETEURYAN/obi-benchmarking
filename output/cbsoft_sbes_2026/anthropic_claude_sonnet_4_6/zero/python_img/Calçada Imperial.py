import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    seq = [int(input_data[i+1]) for i in range(n)]
    
    # Get all distinct values
    distinct = list(set(seq))
    
    best = 0
    
    # Try all pairs of distinct values (including single values)
    # For each pair (a, b), find the longest subsequence using only a and b
    # with no two consecutive equal elements
    
    def max_subseq(a, b):
        # Find longest subsequence from seq using only values a and b
        # with no two consecutive equal
        # We can use DP: dp[i][last] = max length ending at index i with last value being 'last'
        # But since we just need max length, we can greedily pick elements
        
        # Filter positions where value is a or b
        filtered = [v for v in seq if v == a or v == b]
        
        if not filtered:
            return 0
        
        # Now find longest subsequence with no two consecutive equal
        # Since we can pick any subset (maintaining order), we want to maximize count
        # Greedy: always pick if it's different from last picked
        # But we can also skip elements to pick more later
        # Actually, since we want maximum, we should pick every element that differs from previous
        # Wait - we're picking a subsequence, so we can skip elements
        # The maximum subsequence with no two consecutive equal from filtered:
        # We can always pick all elements except when there are consecutive duplicates
        # For consecutive duplicates in filtered, we can only pick one
        # So the answer is: count of elements in filtered minus the number of "extra" consecutive duplicates
        
        count = 0
        last = -1
        for v in filtered:
            if v != last:
                count += 1
                last = v
            # if v == last, skip it (we can't pick it without violating constraint)
            # But wait - can we skip the previous one and pick this one instead?
            # No, because we already committed to picking the previous one
            # Actually in a subsequence problem, we need to think more carefully
            # But here: if we have [a, a, b], we can pick [a, b] = 2
            # Greedy picks first a, skips second a, picks b = 2. Correct.
            # If we have [a, b, a], greedy picks all 3. Correct.
            # The greedy of "pick if different from last" is optimal here
            # because picking current doesn't prevent future picks any more than skipping would
        
        return count
    
    # Single value case
    for a in distinct:
        # Only one distinct value: can only pick 1 (no two consecutive equal)
        # Actually if sequence has only 'a', we can pick at most 1
        count = 1 if a in set(seq) else 0
        best = max(best, count)
    
    # Two distinct values
    if len(distinct) == 1:
        best = 1
    else:
        for i in range(len(distinct)):
            for j in range(i, len(distinct)):
                a = distinct[i]
                b = distinct[j]
                res = max_subseq(a, b)
                best = max(best, res)
    
    print(best)

solve()