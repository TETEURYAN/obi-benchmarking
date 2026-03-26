import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().split()
    idx = 0
    C = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    radii_sq = []
    for i in range(C):
        r = int(data[idx]); idx += 1
        radii_sq.append(r * r)
    
    total = 0
    for _ in range(T):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        dist_sq = x * x + y * y
        # number of circles with r^2 >= dist_sq
        # radii_sq is sorted ascending
        # find first index where radii_sq[i] >= dist_sq
        pos = bisect_left(radii_sq, dist_sq)
        total += C - pos
    
    print(total)

main()