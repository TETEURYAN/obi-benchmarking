import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = list(map(int, data[1:n+1]))
    
    # Key insight: each box must be transported from floor 1 to floor 2.
    # The elevator has two cabins connected by a pulley.
    # In each trip, one cabin goes up (with or without a box) and the other goes down.
    # Constraint: |P - Q| <= 8, where P and Q are weights of the two cabins.
    # Empty cabin has weight 0.
    
    # A box can be moved up directly if its weight <= 8 (paired with empty cabin).
    # A box of weight w can be moved up paired with another box of weight v going down,
    # if |w - v| <= 8.
    
    # The critical observation: a box with weight > 8 cannot travel alone (paired with empty cabin).
    # It must be paired with another box going down, meaning that box must already be upstairs
    # (to come back down) or we need a helper box.
    
    # For a box of weight w > 8 to go up, there must exist some box v already upstairs
    # such that |w - v| <= 8, i.e., w - 8 <= v <= w + 8.
    
    # Strategy: We can always move boxes with weight <= 8 freely.
    # For heavier boxes, we need a "bridge" of boxes where consecutive weights differ by <= 8.
    
    # Actually, let's think more carefully:
    # - Any box with weight <= 8 can go up alone (diff with empty = weight <= 8).
    # - A box with weight w can go up if there's a box upstairs with weight v where |w-v| <= 8.
    #   That box v can then come back down (diff = v with empty, so v <= 8, OR paired again).
    
    # The key insight: we can use boxes as "counterweights". 
    # A box can be transported up if we can find a sequence of boxes forming a chain
    # where each consecutive pair differs by at most 8, starting from 0 (empty).
    
    # So: sort the boxes. Check if there's a connected path from 0 to each box weight
    # where consecutive steps differ by <= 8.
    # This means: starting from 0, can we reach all box weights by steps of <= 8?
    
    # With sorted weights: check if weights[0] <= 8, and each consecutive pair 
    # weights[i+1] - weights[i] <= 8.
    # But we also need to consider that we might use the same box multiple times as counterweight.
    
    # Once a box is upstairs, it can serve as counterweight for boxes within 8 units of it.
    # So effectively: starting from "0" (empty), can we reach all weights?
    # The reachable set grows: initially {0}, then any weight w where w <= 8 is reachable.
    # Once w is upstairs, any weight v with |v - w| <= 8 becomes reachable.
    
    # This is equivalent to: sort weights, check weights[0] <= 8, 
    # and for each i, weights[i] - weights[i-1] <= 8 (since we can always bring a box back down).
    
    # Wait - but a box brought upstairs can come back down as counterweight.
    # So once any box is upstairs, we can use it repeatedly.
    
    # The reachable weights form a connected component from 0 with step size 8.
    # Sort weights. If min weight > 8: impossible.
    # Otherwise, check that sorted weights form a chain where each gap <= 8.
    
    weights.sort()
    
    if weights[0] > 8:
        print('N')
        return
    
    for i in range(1, n):
        if weights[i] - weights[i-1] > 8:
            print('N')
            return
    
    print('S')

solve()