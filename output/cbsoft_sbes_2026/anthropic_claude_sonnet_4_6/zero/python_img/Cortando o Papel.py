import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # For a horizontal cut at height h (0 < h):
    # A rectangle i is "cut" if h < a[i] (the cut passes through it)
    # A rectangle i is "not cut" if h >= a[i] (the cut is above or at the top)
    
    # The number of pieces:
    # When we make a horizontal cut at height h:
    # - Rectangles where a[i] <= h are not cut (they remain whole below the cut)
    # - Rectangles where a[i] > h are cut into two pieces
    
    # The pieces are formed by contiguous groups.
    # Let's think about it differently:
    # The cut divides the paper. The number of pieces depends on how many 
    # contiguous segments are created.
    
    # For a cut at height h:
    # Each rectangle with a[i] > h contributes to the cut region
    # Each rectangle with a[i] <= h is a "gap" in the cut
    
    # Number of pieces = 1 (bottom always connected as one piece along base)
    # Wait, let me reconsider.
    
    # Actually: pieces are separated segments.
    # Bottom piece: always 1 connected piece (all rectangles connected at base)
    # Top pieces: number of contiguous groups of rectangles with a[i] > h
    # Plus the bottom piece which is always 1.
    
    # Wait, but if all rectangles are cut, bottom is 1 piece, top segments = number of contiguous groups of cut rectangles
    # If some rectangles are not cut, the bottom piece might still be 1 (connected at base)
    # Top pieces = number of contiguous groups where a[i] > h
    
    # Total pieces = 1 (bottom) + number of contiguous groups with a[i] > h
    # But if no rectangle is cut (h >= max(a)), pieces = 1
    # If all are cut, pieces = 1 + 1 = 2 (bottom strip + top strip)... 
    # Hmm, but the example shows up to 11 pieces.
    
    # Let me reconsider: when cut at height h,
    # - bottom parts: contiguous groups of ALL rectangles (they're all connected at base) = 1 piece
    # - Actually no: rectangles not cut remain whole, rectangles cut have bottom part
    # - All bottom parts are connected = 1 piece
    # - Top parts: each contiguous group of rectangles with a[i] > h = separate piece
    # Total = 1 + (number of contiguous groups with a[i] > h)
    
    # To maximize: we want to maximize contiguous groups with a[i] > h
    # This means we want h to be such that many rectangles alternate above/below h
    
    # The optimal h is just below some a[i] value.
    # For each unique height value v, consider h = v - epsilon (so rectangles with a[i] >= v are cut)
    # and h = v (so rectangles with a[i] > v are cut)
    
    # We need to check all critical heights: just below each unique a[i]
    
    # For a given set of "cut" rectangles (a[i] > h), count contiguous groups
    
    # Collect all unique heights
    unique_heights = sorted(set(a))
    
    best = 1
    
    # For each candidate h, we consider h = v (rectangles with a[i] > v are cut)
    # and h = v-1 effectively means rectangles with a[i] >= v are cut
    # Since heights are integers, h can be any value. Critical values are at each a[i].
    
    # Check h = v for each unique v (cut if a[i] > v)
    # Check h = v-1 for each unique v (cut if a[i] >= v, i.e., a[i] > v-1)
    # These two cases cover all needed thresholds
    
    candidates = set()
    for v in unique_heights:
        candidates.add(v)
        candidates.add(v - 1)
    
    for h in candidates:
        if h <= 0:
            continue
        # Count contiguous groups with a[i] > h
        groups = 0
        in_group = False
        for i in range(n):
            if a[i] > h:
                if not in_group:
                    groups += 1
                    in_group = True
            else:
                in_group = False
        
        pieces = 1 + groups
        if pieces > best:
            best = pieces
    
    print(best)

solve()