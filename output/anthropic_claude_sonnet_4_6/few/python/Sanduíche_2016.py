import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = int(data[1])
    c = list(map(int, data[2:2+n]))
    
    total = sum(c)
    count = 0
    
    # Part 1: contiguous subarray sum = D (sliding window, all Ci >= 1)
    left = 0
    current = 0
    for right in range(n):
        current += c[right]
        while current > d and left <= right:
            current -= c[left]
            left += 1
        if current == d:
            count += 1
    
    # Part 2: prefix from left + suffix from right = D
    # prefix[i] = C1 + ... + Ci (1-indexed), i from 1 to N-1
    # suffix[j] = Cj + ... + CN (1-indexed), j from 2 to N
    # We need pairs (i, j) with 1 <= i < j <= N such that prefix[i] + suffix[j] = D
    # prefix[i] = sum of first i elements
    # suffix[j] = sum of last (N - j + 1) elements = total - sum of first (j-1) elements
    # So prefix[i] + (total - prefix[j-1]) = D
    # prefix[i] - prefix[j-1] = D - total
    # We need i < j, so i <= j-1, meaning prefix[i] is among first i elements
    # and prefix[j-1] is prefix up to j-1 where j-1 >= i (since j > i means j-1 >= i)
    
    # Let's use a set/dict approach:
    # For each j from 2 to N, suffix[j] = total - prefix[j-1]
    # We need prefix[i] = D - suffix[j] = D - total + prefix[j-1]
    # i ranges 1..N-1, j ranges 2..N, i < j
    
    # Iterate j from 2 to N:
    # We want prefix[i] = D - (total - prefix[j-1]) for some i < j
    # As j increases, we can add prefix[i] values to a dict as i goes up to j-1
    
    # prefix[0] = 0, prefix[1] = c[0], ..., prefix[k] = sum(c[0..k-1])
    
    # Build prefix sums
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + c[i]
    
    # For part 2:
    # pairs (i, j) 1-indexed, 1 <= i < j <= N
    # sum = prefix[i] + (total - prefix[j-1]) = D
    # prefix[i] = D - total + prefix[j-1]
    
    # We iterate j from 2 to N (1-indexed)
    # For each j, we need prefix[i] = D - total + prefix[j-1], with 1 <= i < j
    # As j goes from 2 to N, i can be from 1 to j-1
    # We maintain a frequency map of prefix[1..j-1] as j increases
    
    from collections import defaultdict
    freq = defaultdict(int)
    
    # j=2: i can be 1, so we add prefix[1] before processing j=2
    # When j=2, prefix[j-1] = prefix[1], need prefix[i] for i in 1..1
    # So before j=2, add prefix[1]
    # Before j=3, add prefix[2]
    # ...
    # Before j=k, add prefix[k-1]
    
    for j in range(2, n + 1):
        # Add prefix[j-1] to freq (i = j-1)
        freq[prefix[j-1]] += 1
        # Now find how many i in 1..j-1 have prefix[i] = D - total + prefix[j-1]
        target = d - total + prefix[j-1]
        count += freq[target]
    
    print(count)

solve()