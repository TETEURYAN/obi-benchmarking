import sys
import math

N, K = map(int, sys.stdin.read().split())

low = 1
high = 1000000000
while low < high:
    mid = (low + high) // 2
    if K >= mid:
        if mid >= 30:
            sum_val = 10**18
        else:
            sum_val = 1 << mid
    else:
        sum_val = 0
        for i in range(K + 1):
            sum_val += math.comb(mid, i)
    if sum_val >= N:
        high = mid
    else:
        low = mid + 1

print(low)