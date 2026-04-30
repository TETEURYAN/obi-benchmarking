Looking at this problem, I need to simulate a dance where indigenous people jump between logs arranged in a circle.

Key rules:
1. Each beat, each person jumps to the next log in their direction
2. If two people jumping in opposite directions land on the same log → both reverse direction
3. If two people on consecutive logs are about to jump toward each other → neither jumps, both reverse direction
4. Dance ends when the set of occupied logs matches the initial set

Let me think about the simulation carefully:

- Logs numbered 1 to N in clockwise order
- Direction 1 = clockwise (position increases), -1 = anti-clockwise (position decreases)
- Each step: compute new positions considering collisions

For each beat:
1. Compute intended new position for each person: `new_pos = (pos + dir - 1) % N + 1`
2. Check case 2: two people on consecutive logs jumping toward each other (they would swap positions). These people don't move and reverse direction.
3. For remaining people, compute their new positions.
4. Check case 1: two people land on same log from opposite directions → both reverse direction.

Let me implement this step by step:

```python
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    E = int(input_data[idx]); idx+=1
    
    positions = []
    directions = []
    for _ in range(E):
        v = int(input_data[idx]); idx+=1
        d = int(input_data[idx]); idx+=1
        positions.append(v)
        directions.append(d)
    
    initial_set = frozenset(positions)
    
    step = 0
    while True:
        # Check termination: set of positions matches initial
        if step > 0 and frozenset(positions) == initial_set:
            print(step)
            return
        
        # Compute intended moves
        new_pos = [(positions[i] - 1 + directions[i]) % N + 1 for i in range(E)]
        
        # Check case 2: two people on consecutive logs jumping toward each other
        # Person i at pos p with dir 1, person j at pos p+1 with dir -1
        # They would swap: new_pos[i] = p+1, new_pos[j] = p
        blocked = [False] * E
        
        pos_to_idx = {positions[i]: i for i in range(E)}
        
        for i in range(E):
            if blocked[i]:
                continue
            # Check if person i and some person j would swap
            j_pos = new_pos[i]
            if j_pos in pos_to_idx:
                j = pos_to_idx[j_pos]
                if not blocked[j] and new_pos[j] == positions[i]:
                    # They would swap - case 2
                    blocked[i] = True
                    blocked[j] = True
                    directions[i] = -directions[i]
                    directions[j] = -directions[j]
        
        # Move unblocked people
        for i in range(E):
            if not blocked[i]:
                positions[i] = new_pos[i]
        
        # Check case 1: multiple people on same log from opposite directions
        pos_groups = defaultdict(list)
        for i in range(E):
            pos_groups[positions[i]].append(i)
        
        for pos, group in pos_groups.items():
            if len(group) >= 2:
                # Reverse all their directions
                for i in group:
                    directions[i] = -directions[i]
        
        step += 1
        
        if step > 10 * N * E + 1000:
            print(step)
            return

solve()
```

Let me test with the examples and refine. The termination condition needs care - we need to check after each step. Also need a reasonable upper bound.

```python
import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    E = int(data[idx]); idx+=1
    positions = []
    directions = []
    for _ in range(E):
        v = int(data[idx]); idx+=1
        d = int(data[idx]); idx+=1
        positions.append(v)
        directions.append(d)
    initial_set = frozenset(positions)
    step = 0
    while True:
        step += 1
        new_pos = [(positions[i]-1+directions[i])%N+1 for i in range(E)]
        pos_to_idx = {positions[i]:i for i in range(E)}
        blocked = [False]*E
        for i in range(E):
            if blocked[i]: continue
            j_pos = new_pos[i]
            if j_pos in pos_to_idx:
                j = pos_to_idx[j_pos]
                if not blocked[j] and new_pos[j]==positions[i] and i!=j:
                    blocked[i]=True; blocked[j]=True
                    directions[i]=-directions[i]; directions[j]=-directions[j]
        for i in range(E):
            if not blocked[i]: positions[i]=new_pos[i]
        groups=defaultdict(list)
        for i in range(E): groups[positions[i]].append(i)
        for g in groups.values():
            if len(g)>=2:
                for i in g: directions[i]=-directions[i]
        if frozenset(positions)==initial_set:
            print(step); return

solve()
```