import sys
from sortedcontainers import SortedList

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1

sl = SortedList()
P_prev = 0

for k in range(1, N + 1):
    XK = int(input_data[idx])
    YK = int(input_data[idx + 1])
    idx += 2
    
    XR = XK + P_prev
    YR = YK + P_prev
    dist_sq = XR * XR + YR * YR
    
    PK = sl.bisect_right(dist_sq)
    print(PK)
    
    sl.add(dist_sq)
    P_prev = PK