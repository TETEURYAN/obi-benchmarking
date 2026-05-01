import sys
from collections import deque

# Fast I/O
input_data = sys.stdin.read().split()
if not input_data:
    exit()

iterator = iter(input_data)
try:
    N = int(next(iterator))
    D = int(next(iterator))
    W = int(next(iterator))
    P = []
    for _ in range(N):
        P.append(int(next(iterator)))
except StopIteration:
    exit()

# Precompute prefix sums for range sum queries
# S[i] is sum of first i elements (P[0]...P[i-1])
S = [0] * (N + 1)
for i in range(N):
    S[i+1] = S[i] + P[i]

# Function to get sum of P[a...b] inclusive
def get_sum(l, r):
    return S[r+1] - S[l]

# Monotonic queue to maintain maximum sum of a subarray of length D
# Stores pairs (index, value)
# index is the start of the free window
dq = deque()

L = 0
max_len = 0

for R in range(N):
    # The current window is [L, R]
    # If the window size is at least D, we can consider a free window ending at R
    # The free window would be [R-D+1, R]
    
    if R - D + 1 >= 0:
        u = R - D + 1
        # Sum of the free window starting at u
        val = get_sum(u, u + D - 1)
        
        # Maintain decreasing order in deque
        while dq and dq[-1][1] <= val:
            dq.pop()
        dq.append((u, val))
    
    # Remove elements from the front that are out of the current L-bound
    # The free window must start at u >= L
    while dq and dq[0][0] < L:
        dq.popleft()
        
    # Check if current window is valid
    # We need a valid free window inside [L, R]
    if dq:
        # Current cost is Total Sum - Max Free Sum
        current_total = get_sum(L, R)
        max_free = dq[0][1]
        cost = current_total - max_free
        
        # If cost exceeds W, shrink window from left
        while cost > W:
            L += 1
            # Remove elements out of new L-bound
            while dq and dq[0][0] < L:
                dq.popleft()
            
            if not dq:
                break
            
            # Recalculate cost
            current_total = get_sum(L, R)
            max_free = dq[0][1]
            cost = current_total - max_free
            
        # If valid, update max length
        if dq:
            current_len = R - L + 1
            if current_len > max_len:
                max_len = current_len

print(max_len)