import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    passwords = []
    for i in range(1, n + 1):
        passwords.append(data[i])
    
    # For each pair (A, B) where A != B (by index), check if password_A is substring of password_B
    # N up to 20000, passwords up to length 10
    # Naive O(N^2) with string contains: 20000^2 = 4*10^8 might be tight
    # But since passwords are at most length 10, we can group by unique passwords
    # and use frequency counts
    
    # Count frequency of each password
    freq = defaultdict(int)
    for p in passwords:
        freq[p] += 1
    
    unique_passwords = list(freq.keys())
    
    # For each pair of distinct unique passwords (A, B), check if A is substring of B
    # Then add freq[A] * freq[B] to answer
    # Also handle A == B case: if A is substring of A (always true since A == A),
    # then pairs = freq[A] * (freq[A] - 1)
    
    answer = 0
    
    for i, pa in enumerate(unique_passwords):
        for j, pb in enumerate(unique_passwords):
            if i == j:
                # same unique password: pa is always substring of pb (they're equal)
                cnt = freq[pa]
                answer += cnt * (cnt - 1)
            else:
                # check if pa is substring of pb
                if pa in pb:
                    answer += freq[pa] * freq[pb]
    
    print(answer)

solve()