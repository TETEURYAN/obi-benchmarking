import sys
import math

def truncate_div(s, m):
    # Truncate toward zero
    if s >= 0:
        return s // m
    else:
        return -((-s) // m)

data = sys.stdin.read().split()
idx = 0
test_num = 0

while idx < len(data):
    N = int(data[idx]); M = int(data[idx+1])
    idx += 2
    if N == 0 and M == 0:
        break
    
    temps = []
    for i in range(N):
        temps.append(int(data[idx]))
        idx += 1
    
    test_num += 1
    
    # Sliding window sum of size M
    window_sum = sum(temps[:M])
    min_sum = window_sum
    max_sum = window_sum
    
    for i in range(1, N - M + 1):
        window_sum += temps[i + M - 1] - temps[i - 1]
        if window_sum < min_sum:
            min_sum = window_sum
        if window_sum > max_sum:
            max_sum = window_sum
    
    min_avg = truncate_div(min_sum, M)
    max_avg = truncate_div(max_sum, M)
    
    print(f"Teste {test_num}")
    print(f"{min_avg} {max_avg}")
    print()