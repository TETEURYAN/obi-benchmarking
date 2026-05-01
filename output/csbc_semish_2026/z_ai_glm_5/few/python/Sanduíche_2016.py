import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        D = int(next(iterator))
    except StopIteration:
        return

    # Read C values
    C = []
    for _ in range(N):
        try:
            C.append(int(next(iterator)))
        except StopIteration:
            break
            
    # Compute prefix sums
    P = [0] * (N + 1)
    for i in range(N):
        P[i+1] = P[i] + C[i]
    
    total_sum = P[N]
    
    # Case 1: Continuous sequence
    # We want P[j] - P[i-1] = D, which means P[i-1] = P[j] - D
    # Iterate j from 1 to N. We need to know if P[j] - D was seen before as a prefix sum.
    # The prefix sums available are P[0]...P[j-1].
    count1 = 0
    freq = {0: 1} # P[0] = 0 is available initially
    
    for j in range(1, N + 1):
        target = P[j] - D
        if target in freq:
            count1 += freq[target]
        
        # Add current prefix sum to map for future j's
        # Note: We add P[j] after checking because for continuous sequence i <= j, 
        # the start index i-1 must be strictly less than j (as a prefix sum index).
        # Actually, P[i-1] corresponds to sum before C[i]. 
        # For P[j] - P[i-1], we need i-1 < j.
        # So we must use prefix sums strictly before current j.
        freq[P[j]] = freq.get(P[j], 0) + 1
        
    # Case 2: Prefix + Suffix
    # We want P[i] + (Total - P[j-1]) = D
    # Rearranging: P[i] - P[j-1] = D - Total
    # Let k = j-1. We want P[i] - P[k] = K, where K = D - Total.
    # Constraints: 1 <= i < j <= N  =>  1 <= i <= k < N
    # We iterate k from 1 to N-1.
    # We need P[i] = P[k] + K with i <= k.
    # The available prefix sums are P[1]...P[k].
    
    count2 = 0
    K = D - total_sum
    freq2 = {}
    
    for k in range(1, N):
        # Add P[k] to map first so it's included in the search (allowing i=k)
        val = P[k]
        freq2[val] = freq2.get(val, 0) + 1
        
        target = val + K
        if target in freq2:
            count2 += freq2[target]
            
    print(count1 + count2)

if __name__ == '__main__':
    solve()