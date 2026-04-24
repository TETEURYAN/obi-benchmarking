import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        L = int(next(iterator))
        H = int(next(iterator))
    except StopIteration:
        return

    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = int(next(iterator))
    
    marked_pos = []
    for i in range(1, N + 1):
        m = int(next(iterator))
        if m == 1:
            marked_pos.append(i)
    
    K = len(marked_pos)
    
    # Prefix sums
    PS = [0] * (N + 1)
    for i in range(1, N + 1):
        PS[i] = PS[i-1] + S[i]
        
    # P array with boundaries
    # P[0] = 0, P[K+1] = N+1
    P = [0] + marked_pos + [N + 1]
    
    # Precompute min and max prefix sums in segments defined by marked positions
    # Segment i corresponds to indices u in [P[i], P[i+1]-1]
    # There are K+1 segments (indices 0 to K)
    min_ps = [0] * (K + 1)
    max_ps = [0] * (K + 1)
    
    for i in range(K + 1):
        start_idx = P[i]
        end_idx = P[i+1] - 1
        
        # The range is never empty as P[i] < P[i+1]
        current_min = PS[start_idx]
        current_max = PS[start_idx]
        
        for u in range(start_idx + 1, end_idx + 1):
            val = PS[u]
            if val < current_min:
                current_min = val
            if val > current_max:
                current_max = val
        
        min_ps[i] = current_min
        max_ps[i] = current_max
        
    # Initialize answer
    # If L=0, empty subsequence is valid, sum 0.
    # Also need to check k=0 case (subsequence with 0 marked elements).
    ans = -float('inf')
    if L == 0:
        ans = 0
        # Check max subarray sum in segments (Kadane's algorithm)
        for i in range(K + 1):
            start_s = P[i] + 1
            end_s = P[i+1] - 1
            
            if start_s > end_s:
                continue
                
            current_sum = 0
            for idx in range(start_s, end_s + 1):
                val = S[idx]
                current_sum = max(0, current_sum + val)
                if current_sum > ans:
                    ans = current_sum
                    
    # Iterate k (number of marked elements) from max(L, 1) to min(H, K)
    start_k = L
    if start_k == 0:
        start_k = 1
    
    end_k = H
    if end_k > K:
        end_k = K
        
    for k in range(start_k, end_k + 1):
        # Iterate starting marked index x
        # marked elements are P[x] ... P[x+k-1]
        # Start segment index: x-1
        # End segment index: x+k-1
        limit_x = K - k + 1
        for x in range(1, limit_x + 1):
            seg_start = x - 1
            seg_end = x + k - 1
            
            val = max_ps[seg_end] - min_ps[seg_start]
            if val > ans:
                ans = val
                
    print(ans)

if __name__ == '__main__':
    solve()