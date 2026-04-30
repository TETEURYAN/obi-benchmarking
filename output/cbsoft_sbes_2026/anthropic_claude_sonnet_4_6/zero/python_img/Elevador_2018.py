import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    boxes = list(map(int, input_data[1:n+1]))
    
    # Key insight: A box can be transported if we can find a sequence of trips.
    # Each trip: one cabin goes up with a box (weight P), other cabin goes down with a box or empty (weight Q).
    # Constraint: |P - Q| <= 8
    # 
    # A box of weight w can go up if:
    # - The other cabin is empty: |w - 0| <= 8, so w <= 8
    # - The other cabin has a box of weight q going down: |w - q| <= 8
    #
    # To bring a box down, we need to send it up first (it's already up) or it starts up.
    # Wait - boxes start at floor 1 (bottom). We need to get them all to floor 2 (top).
    #
    # The elevator can be used to shuttle boxes. A box can go up paired with another box going down.
    # A box going down must have been previously sent up.
    #
    # Strategy: We can use "helper" boxes to assist heavier boxes.
    # A box of weight w can go up alone if w <= 8.
    # A box of weight w can go up paired with a box of weight q (going down) if |w - q| <= 8.
    #
    # The question is: can all boxes be transported?
    # 
    # Key observation: Any box with weight > 8 needs a companion box going down.
    # The companion must have weight in [w-8, w+8].
    # The companion box must be able to go up first (possibly with help).
    #
    # This is essentially: can we order the boxes such that each box can be lifted?
    # A box can be lifted if there exists another box (already upstairs or being sent down) 
    # within 8 units of weight, OR if the box itself weighs <= 8.
    #
    # Greedy/BFS approach: 
    # State = set of boxes currently upstairs. But N up to 10^4, so we need smarter approach.
    #
    # Actually the key insight: a box w can go up if w <= 8 OR there exists some box q 
    # (that can be sent back down) with |w - q| <= 8.
    # 
    # We can repeatedly find boxes we can move up. Start with boxes <= 8 (can go up alone).
    # Once a box is upstairs, it can come back down to help another box go up.
    # A box q upstairs can help box w go up if |w - q| <= 8.
    # After helping, q is back downstairs and needs to go up again.
    # 
    # So: reachable set of weights we can get upstairs grows as we find helpers.
    # We can get box w upstairs if: w <= 8, OR exists q already gotten upstairs with |w-q| <= 8.
    # Because q can go down to help w go up, then q needs to go up again (but q is already proven movable).
    
    # BFS on which boxes can be moved upstairs
    # A box can go up if its weight <= 8 OR if there's any box already confirmed movable with |w - q| <= 8
    
    boxes_set = list(boxes)
    
    # Use iterative approach: keep trying to add more boxes to "can go up" set
    can_go_up = set()
    
    # Initially, boxes with weight <= 8 can go up
    changed = True
    while changed:
        changed = False
        remaining = []
        for w in boxes_set:
            if w <= 8:
                can_go_up.add(w)
                changed = True
            else:
                # Check if any box in can_go_up is within 8 of w
                # We need to check if there's q in can_go_up with |w - q| <= 8
                found = False
                for q in can_go_up:
                    if abs(w - q) <= 8:
                        found = True
                        break
                if found:
                    can_go_up.add(w)
                    changed = True
                else:
                    remaining.append(w)
        boxes_set = remaining
        if not changed and remaining:
            break
    
    if not boxes_set:
        print("S")
    else:
        print("N")

solve()