Looking at this problem, I need to determine if all boxes can be transported from floor 1 to floor 2 using an elevator with two cabins connected by a pulley.

Key constraints:
- Only one box per cabin at a time
- During a trip, |P - Q| ≤ 8, where P is heavier cabin and Q is lighter cabin
- A cabin can be empty (weight 0)

Let me think about what "a trip" means:
- One cabin goes up with a box (or empty), the other goes down (with a box or empty)
- The difference between the two cabins during that trip must be ≤ 8

For a box to go up, it needs to be in the ascending cabin. The descending cabin can have a box (going down temporarily) or be empty.

The critical observation: to move a box of weight W up, we need another cabin with weight Q such that W - Q ≤ 8 (assuming W ≥ Q), so Q ≥ W - 8.

The hardest box to move is the heaviest one. To move the heaviest box (weight W_max), we need a counterweight of at least W_max - 8.

But we can also use boxes already on floor 2 as counterweights (sending them down temporarily).

The key insight: The heaviest box needs a counterweight ≥ W_max - 8. This counterweight must come from some other box. If no other box has weight ≥ W_max - 8, it's impossible.

But wait - we can also move boxes up first to use them as counterweights later. Let me think recursively.

Actually, the problem reduces to: can we always find a valid "helper" box for each box we want to move? The heaviest box is the hardest. To move it, we need some box with weight ≥ W_max - 8. 

If such a box exists, we can move the heaviest box. Then we need to check the remaining boxes similarly.

But the helper box might need to go down temporarily - that's fine since we can move it back up.

The condition is: for the largest box, there must exist another box with weight ≥ largest - 8. If N=1, the single box just needs weight ≤ 8 (since the other cabin is empty with weight 0).

Wait, for N=1: box weight W, other cabin empty (0), difference = W - 0 = W ≤ 8.

For N>1: the largest box needs a counterweight ≥ largest - 8. The best counterweight is the second largest box.

But after moving the largest, we need to check if the remaining can be moved. However, once the largest is up, it can serve as counterweight for others.

Let me reconsider: The only problematic box is the largest. If we can move the largest (using the second largest as counterweight), then all smaller boxes can be moved using the largest as counterweight (since largest ≥ any box, and we just need largest - box ≤ 8... no that's not right either).

Actually each box needs a counterweight. The worst case for each box is when it's the heaviest being moved. 

The greedy approach: sort boxes. The largest box needs second largest as counterweight: boxes[N-1] - boxes[N-2] ≤ 8. For N=1: boxes[0] ≤ 8.

But test case 3: [10, 14, 20, 23]. Largest=23, second=20, diff=3 ≤ 8. But answer is N!

So my analysis is wrong. Let me reconsider...

Maybe ALL consecutive pairs need to satisfy the constraint? [10,14,20,23]: 14-10=4✓, 20-14=6✓, 23-20=3✓ → should be S but answer is N.

Hmm. Let me think differently. Maybe the box being moved down as counterweight also needs to eventually come back up, creating a chain requirement.

After more careful analysis: to move box W up, we use box C as counterweight (C goes down). Then C needs to come back up, requiring another counterweight ≥ C-8. This creates a dependency chain.

The condition seems to be: every box must be "reachable" - meaning we need to check if the second largest can be moved up using the third largest, etc.

So the condition is: for every i from 1 to N-1: boxes[i] - boxes[i-1] ≤ 8, AND boxes[0] ≤ 8.

Test 3: [10,14,20,23] - boxes[0]=10 > 8 → N! That matches!
Test 1: [4,10,15] - 4≤8✓, 10-4=6✓, 15-10=5✓ → S ✓
Test 2: [2,6,15,20,25,35,35,40] - 15-6=9 > 8 → N ✓
Test 4: [8] - 8≤8 → S ✓

```python
n = int(input())
boxes = list(map(int, input().split()))

possible = True
if boxes[0] > 8:
    possible = False
else:
    for i in range(1, n):
        if boxes[i] - boxes[i-1] > 8:
            possible = False
            break

print('S' if possible else 'N')
```