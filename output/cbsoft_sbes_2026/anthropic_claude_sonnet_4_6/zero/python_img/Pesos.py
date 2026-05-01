I need to analyze this problem carefully.

The elevator has two cabins connected by a pulley. When one goes up, the other goes down. The constraint is that the weight difference between cabins must be ≤ 8.

Key observations:
- A cabin can be empty (weight 0) or have one box
- During a trip: one cabin goes up, one goes down
- Constraint: |weight_up - weight_down| ≤ 8
- We need to move all boxes from floor 1 to floor 2

The critical constraint is: when moving a box up, the difference between the box being moved up and whatever is in the other cabin (going down) must be ≤ 8.

So for each box with weight P going up, we need something with weight Q going down where P - Q ≤ 8 and Q - P ≤ 8, i.e., |P - Q| ≤ 8. Q can be 0 (empty cabin) or another box.

The key insight: to move a heavy box up, we might need to use another box as counterweight going down. But that box needs to be brought back up later.

Let me think about what's possible:
- Any box with weight ≤ 8 can go up with an empty cabin going down (difference ≤ 8)
- A heavier box needs a counterweight: another box going down with weight within 8 of it

The question is: can we transport all boxes?

For a box of weight W to go up, we need a counterweight Q where |W - Q| ≤ 8. Q = 0 works if W ≤ 8. Otherwise we need a box with weight in [W-8, W+8].

The hardest boxes to move are the heaviest ones. The largest box needs a counterweight within 8 of it. That counterweight box must also be movable.

Let me think about this differently: the largest box (weight M) needs a counterweight with weight in [M-8, M]. If no such box exists (other than itself), it's impossible... unless M ≤ 8.

Actually, we can use the same box multiple times as counterweight. So if we have box A (heavy) and box B (medium, within 8 of A), we can:
1. Move B up with empty going down (if B ≤ 8, or B has its own counterweight)
2. Move A up with B going down
3. Move B up again...

The critical question: is the largest box transportable?

For the largest box W_max:
- If W_max ≤ 8: trivially yes (use empty cabin)
- Otherwise: need some box with weight in [W_max - 8, W_max]. That box must itself be transportable.

This suggests a greedy/recursive approach: check if each box can be moved given available counterweights.

Actually, let me think about it: if we sort boxes, the largest box needs a counterweight. If there exists any other box within 8 of it, we can use that box (send it up first, use it as counterweight going down while large box goes up, then send it up again). The counterweight box itself needs to be movable.

So the condition is: for every box, either its weight ≤ 8, OR there exists another box (could be same weight) within 8 units that is itself movable.

This is recursive. Let's think greedily: process from smallest to largest. A box is "movable" if weight ≤ 8 OR there's a movable box within 8 of it.

```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    weights = list(map(int, input_data[1:n+1]))
    
    weights.sort()
    
    # A box is movable if weight <= 8 or there exists a movable box within 8 of it
    movable = [False] * n
    
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if movable[i]:
                continue
            if weights[i] <= 8:
                movable[i] = True
                changed = True
            else:
                # Check if there's a movable box within 8
                for j in range(n):
                    if i != j and movable[j] and abs(weights[i] - weights[j]) <= 8:
                        movable[i] = True
                        changed = True
                        break
    
    if all(movable):
        print('S')
    else:
        print('N')

solve()
```

This might be O(n²) per iteration which could be slow. Let me optimize using sorted order:

Since weights are sorted, once we know the maximum movable weight, any box within 8 of a movable box is also movable. We can track the maximum movable weight.

n=10^4, O(n²) = 10^8 which might be too slow. But the while loop runs at most n times... Let me just submit the cleaner version with binary search optimization.

```python
import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = sorted(map(int, data[1:n+1]))
    
    max_movable = 0  # max weight that is movable (0 means empty cabin)
    
    changed = True
    movable_set = set()
    while changed:
        changed = False
        for w in weights:
            if w not in movable_set:
                if w <= 8 or (max_movable > 0 and w - max_movable <= 8):
                    movable_set.add(w)
                    max_movable = max(max_movable, w)
                    changed = True
    
    print('S' if len(movable_set) >= n or all(w in movable_set for w in weights) else 'N')

solve()
```