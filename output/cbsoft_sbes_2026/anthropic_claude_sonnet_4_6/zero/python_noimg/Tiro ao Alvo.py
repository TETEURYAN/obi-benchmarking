import sys
from bisect import bisect_right

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    C = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1
    
    radii = []
    for _ in range(C):
        r = int(input_data[idx]); idx += 1
        radii.append(r)
    
    # radii are sorted in increasing order
    # For each shot, compute distance squared and find how many circles contain it
    # A shot is contained in circle i if dist <= R_i, i.e., dist^2 <= R_i^2
    
    radii_sq = [r * r for r in radii]
    
    total = 0
    for _ in range(T):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        d2 = x * x + y * y
        # Find number of circles with radii_sq[i] >= d2
        # Since radii_sq is sorted ascending, find first index where radii_sq[i] >= d2
        # That's bisect_left(radii_sq, d2)
        # Number of circles containing = C - bisect_left(radii_sq, d2)
        # Wait: we need radii_sq[i] >= d2, so count = C - bisect_left(radii_sq, d2)
        # bisect_left gives first position where radii_sq[pos] >= d2
        from bisect import bisect_left
        pos = bisect_left(radii_sq, d2)
        total += C - pos
    
    print(total)

main()