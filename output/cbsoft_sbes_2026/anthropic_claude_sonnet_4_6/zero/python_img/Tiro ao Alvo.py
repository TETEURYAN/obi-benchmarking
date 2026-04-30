import sys
from bisect import bisect_right

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    C, T = int(input_data[idx]), int(input_data[idx+1])
    idx += 2
    
    radii = []
    for i in range(C):
        radii.append(int(input_data[idx]))
        idx += 1
    
    # radii are sorted in increasing order
    # For each shot, compute distance squared and find how many circles contain it
    # A circle with radius R contains the shot if x^2 + y^2 <= R^2
    
    radii_sq = [r * r for r in radii]
    
    total = 0
    for _ in range(T):
        x, y = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        d2 = x * x + y * y
        # Find number of circles where radii_sq[i] >= d2
        # Since radii_sq is sorted ascending, find rightmost index where radii_sq[i] >= d2
        # = C - bisect_left(radii_sq, d2) ... no
        # bisect_right gives first index > d2, so all indices from that point have radii_sq > d2
        # indices with radii_sq >= d2: from bisect_left(radii_sq, d2) to C-1
        # count = C - bisect_left(radii_sq, d2)
        pos = bisect_right(radii_sq, d2 - 1)  # first index where radii_sq[i] >= d2
        total += C - pos
    
    print(total)

main()