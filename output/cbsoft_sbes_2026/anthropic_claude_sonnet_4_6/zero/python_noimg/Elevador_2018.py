
```python
import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    weights = list(map(int, input_data[1:n+1]))
    
    # Key insight: each box needs to be transported from floor 1 to floor 2.
    # The elevator has two cabins connected by a pulley.
    # When one goes up, the other goes down.
    # Constraint: |P - Q| <= 8 where P and Q are weights of the two cabins.
    # One cabin can be empty (weight 0).
    
    # A box can be moved up if we can pair it with something going down such that
    # the difference is <= 8. The cabin going down can be empty (weight 0) or 
    # carry a box going down (but boxes need to go UP, not down).
    
    # Wait - boxes need to go from floor 1 to floor 2.
    # The cabin going down is empty (or carries a box back down temporarily).
    # Actually re-reading: we can use boxes as counterweights temporarily.
    
    # For each trip:
    # - One cabin goes UP with a box (weight P)
    # - Other cabin goes DOWN (empty, weight 0, or with a box being brought back down)
    # 
    # But bringing a box back down seems wasteful... let's think again.
    # 
    # Actually the example shows boxes being brought back down (step 2: caixa de peso 4 desce).
    # So we can use boxes as counterweights.
    
    # The question is: can we transport all boxes to floor 2?
    # 
    # Key observation: A box with weight w can be transported alone (with empty cabin going down)
    # if |w - 0| = w <= 8.
    # 
    # A box with weight w can be transported with another box of weight q going down if |w - q| <= 8.
    # But then q needs to be brought back up again.
    
    # Let's think about which boxes can be moved:
    # - Any box with weight <= 8 can be moved alone.
    # - Any box can be moved if there's another box with weight within 8 of it to act as counterweight.
    #   But that counterweight box needs to eventually get up too.
    
    # This is essentially: can we order the boxes such that each one can be lifted?
    # A box of weight w can be lifted if:
    #   1. w <= 8 (lift alone), OR
    #   2. There exists another box already on floor 2 (or being used as counterweight) 
    #      with weight q such that |w - q| <= 8
    
    # Actually, let me think differently. 
    # We can use any box currently on floor 2 as a counterweight (bring it back down temporarily).
    # 
    # So the process is:
    # - We have a set of boxes on floor 1 and floor 2.
    # - Initially all on floor 1.
    # - Each step: pick a box from floor 1 to go up, optionally pick a box from floor 2 to go down.
    # - Constraint: |weight_up - weight_down| <= 8 (weight_down = 0 if no box going down)
    
    # This is a reachability problem. State = set of boxes on floor 2.
    # But N can be up to 10^4, so we can't enumerate all subsets.
    
    # Let me think about what's really needed.
    # 
    # Claim: A box of weight w can eventually be moved to floor 2 if and only if
    # either w <= 8, or there exists some box with weight in [w-8, w+8] that can be moved.
    # 
    # Actually, once ANY box is on floor 2, we can use it as counterweight.
    # So if box A (weight a) is on floor 2, we can move box B (weight b) if |b - a| <= 8.
    # Then both A and B are on floor 2, and we can use either as counterweight for others.
    
    # Algorithm:
    # - Start with "moveable" set = boxes with weight <= 8
    # - Repeatedly: find boxes that can be moved using any box in the moveable set as counterweight
    # - A box w is moveable if there exists a box q in moveable set with |w - q| <= 8
    # - Repeat until no new boxes can be added
    # - If all boxes are moveable, output S, else N
    
    # This is like a graph connectivity / BFS problem.
    # Sort boxes by weight, use a sliding window or similar approach.
    
    weights.sort()
    
    # BFS/iterative approach
    moveable = set()
    
    # Initially, boxes with weight <= 8 can be moved
    for i, w in enumerate(weights):
        if w <= 8:
            moveable.add(i)
    
    # Keep expanding
    changed = True
    while changed:
        changed = False
        for i, w in enumerate(weights):
            if i in moveable:
                continue
            # Check if any moveable box can serve as counterweight
            # We need some q in moveable weights such that |w - q| <= 8
            # i.e., w - 8 <= q <= w + 8
            for j in moveable:
                if abs(w - weights[j]) <= 8:
                    moveable.add(i)
                    changed = True
                    break
    
    if len(moveable) == n:
        print("S")
    else:
        print("N")

solve()
```

Wait, this O(N^2) approach might be too slow for N=10^4. Let me optimize:

```python
import sys
from sortedcontainers import SortedList

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    weights = list(map(int, input_data[1:n+1]))
    
    weights.sort()
    
    moved = [False] * n
    moveable_weights = SortedList()
    
    queue = []
    for i, w in enumerate(weights):
        if w <= 8:
            moved[i] = True
            moveable_weights.add(w)
            queue.append(i)
    
    head = 0
    while head < len(queue):
        idx = queue[head]
        head += 1
        w = weights[idx]
        # Find all unmoved boxes within [w-8, w+8]
        lo = w - 8
        hi = w + 8
        for i, ww in enumerate(weights):
            if not moved[i] and lo <= ww <= hi:
                moved[i] = True
                moveable_weights.add(ww)
                queue.append(i)
    
    print("S" if all(moved) else "N")

solve()
```

This is still O(N^2). Let me use a proper BFS with sorted array:

```python
import sys
from bisect import bisect_left, bisect_right

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = list(map(int, data[1:n+1]))
    weights.sort()
    
    moved = [False] * n
    queue = []
    
    for i in range(n):
        if weights[i] <= 8:
            moved[i] = True
            queue.append(i)
    
    head = 0
    while head < len(queue):
        idx = queue[head]
        head += 1
        w = weights[idx]
        lo = w - 8
        hi = w + 8
        left = bisect_left(weights, lo)
        right = bisect_right(weights, hi)
        for i in range(left, right):
            if not moved[i]:
                moved[i] = True
                queue.append(i)
    
    print("S" if sum(moved) == n else "N")

solve()
```