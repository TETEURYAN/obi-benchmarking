Looking at this problem, I need to understand the dice structure.

From the figure description, a die is given as A B C D E F where:
- A = front face value
- B = back face value  
- C = left face value
- D = right face value
- E = bottom face value
- F = top face value

The constraint is: face E (bottom) of die above = face F (top) of die below.

When we rotate a die horizontally (around vertical axis), the top and bottom stay the same, but the four side faces (A, B, C, D) rotate among themselves. So we can arrange the 4 side faces in any cyclic order.

The side sum for one die = one of its 4 side faces (we pick the best one for the chosen side direction). But wait - all dice must have their sides aligned, and we pick ONE side of the tower. So for each die, we pick the value on that particular side face. After horizontal rotation, the 4 side faces can be arranged in any cyclic order, so we can pick any of the 4 side faces to face a given direction.

So for each die, the maximum contribution to any side is `max(A, B, C, D)` (the maximum of the 4 lateral faces).

But the constraint between stacked dice: bottom of upper die = top of lower die. The top/bottom faces are E and F. When we rotate horizontally, E and F don't change. So the constraint is: F of die i (top) = E of die i+1 (bottom).

Wait, but we can also flip the die? No - we can only rotate horizontally. So top and bottom are fixed as E and F.

But actually, we might be able to orient the die differently initially (before stacking). The problem says the dice are placed in order, but doesn't say we can't orient them differently initially. Actually re-reading: "Hortência pode girar cada dado horizontalmente de forma independente" - she can rotate each die horizontally independently. This implies the initial orientation might be fixed, but she rotates horizontally.

However, we can also choose the initial orientation of each die (which face is up/down). The horizontal rotation only changes which lateral face points in which direction.

So for each die, we need to choose which pair of opposite faces becomes top/bottom, and then the remaining 4 faces are lateral. The constraint is top of die i = bottom of die i+1.

For each die with faces A,B,C,D,E,F: the opposite pairs need to be determined. The problem says opposite faces don't necessarily sum to 7, so we need to figure out which faces are opposite.

From the figure: A-B are opposite (front-back), C-D are opposite (left-right), E-F are opposite (bottom-top). So the three opposite pairs are (A,B), (C,D), (E,F).

So for each die, we can choose orientation: which opposite pair is vertical (top/bottom). Three choices: (E up, F down), (F up, E down), (A up, B down), (B up, A down), (C up, D down), (D up, C down).

The lateral faces' max is the max of the remaining 4 faces.

This becomes a DP problem: dp[i][top_face] = max sum of sides for first i dice where die i has `top_face` on top.

For each die, enumerate all 6 possible top faces. For each top face t, the bottom face is its opposite, and the 4 lateral faces give max lateral value.

dp[i][t] = max over all valid previous states of dp[i-1][bottom_of_die_i] + max_lateral(die_i, t)

where bottom_of_die_i must equal top of die i-1.

Let me implement this:

```python
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    dice = []
    for _ in range(n):
        faces = [int(data[idx+i]) for i in range(6)]
        idx += 6
        dice.append(faces)
    
    # opposite pairs: (0,1), (2,3), (4,5) -> A-B, C-D, E-F
    opposite = {0:1,1:0,2:3,3:2,4:5,5:4}
    
    INF = float('-inf')
    # dp[top_face_index] = max sum
    dp = [INF] * 7  # indexed by face value 1-6
    
    # First die: no constraint on bottom
    d = dice[0]
    for top_idx in range(6):
        bot_idx = opposite[top_idx]
        lateral = [d[i] for i in range(6) if i != top_idx and i != bot_idx]
        best_lat = max(lateral)
        top_val = d[top_idx]
        if dp[top_val] < best_lat:
            dp[top_val] = best_lat
    
    for i in range(1, n):
        d = dice[i]
        new_dp = [INF] * 7
        for top_idx in range(6):
            bot_idx = opposite[top_idx]
            bot_val = d[bot_idx]
            lateral = [d[j] for j in range(6) if j != top_idx and j != bot_idx]
            best_lat = max(lateral)
            top_val = d[top_idx]
            if dp[bot_val] != INF:
                val = dp[bot_val] + best_lat
                if new_dp[top_val] < val:
                    new_dp[top_val] = val
        dp = new_dp
    
    print(max(v for v in dp if v != INF))

solve()
```