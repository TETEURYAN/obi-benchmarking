import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # Group trees by height
    height_to_indices = defaultdict(list)
    for i, h in enumerate(a):
        height_to_indices[h].append(i)
    
    # For each height, we have a list of tree positions.
    # We need to pair them up (non-overlapping intervals at same height don't intersect).
    # The constraint is: two nets at same height don't intersect means they are nested or non-overlapping.
    # Wait, re-reading: "two nets at same height should not intersect" means one is completely to the left of the other.
    # So intervals [l1,r1] and [l2,r2] at same height: they must not intersect (one completely left of other).
    # This means we can pair trees greedily within each height group.
    
    # Actually, the constraint is about ALL nets at the same height not intersecting each other.
    # So for each height, the intervals formed by the pairs must be non-overlapping (non-intersecting).
    # To maximize the number of pairs across all heights, we need to find maximum matching.
    
    # For a single height with positions p1 < p2 < ... < pk:
    # We want to pair them such that intervals don't overlap.
    # Non-overlapping intervals from a sorted list: greedy pairing of consecutive elements gives maximum pairs.
    # Actually for non-overlapping intervals from sorted positions, pairing consecutive ones is optimal.
    # With k positions, we can make floor(k/2) non-overlapping pairs by pairing (p1,p2), (p3,p4), ...
    
    # But wait - nets of DIFFERENT heights can overlap freely (no constraint between different heights).
    # The constraint is only between nets of the SAME height.
    
    # Also constraint: each tree can have at most one net.
    # So if two heights share... no, trees have fixed heights, each tree is unique.
    # Each tree can be used at most once across all nets.
    
    # So the problem is: 
    # - For each height h, we have positions. We can form pairs (intervals) from these positions.
    # - Intervals of same height must be non-overlapping.
    # - Each position (tree) used at most once.
    # - Maximize total number of pairs.
    
    # Since trees have unique positions and each tree belongs to exactly one height group,
    # there's no conflict between different height groups regarding tree usage.
    # So we can independently maximize pairs for each height group!
    
    # For each height group with k trees (sorted positions), 
    # maximum non-overlapping pairs = floor(k/2)
    # achieved by pairing consecutive: (1st,2nd), (3rd,4th), ...
    
    total = 0
    for h, indices in height_to_indices.items():
        k = len(indices)
        total += k // 2
    
    print(total)

solve()