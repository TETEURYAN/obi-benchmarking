The image shows a rock-paper-scissors-like game with 5 options. Based on the examples:
- Test 1: rounds (1,3), (4,2), (0,2) → dario wins
- Test 2: round (3,1) → xerxes wins

I need to figure out the winning relationships. In the classic 5-option game (Rock Paper Scissors Lizard Spock or similar), each option beats exactly 2 others.

Let me analyze from examples:
- Round (1,3): dario chose 1, xerxes chose 3 → dario wins (arrow from 1 to 3)
- Round (4,2): dario chose 4, xerxes chose 2 → dario wins (arrow from 4 to 2)
- Round (0,2): dario chose 0, xerxes chose 2 → dario wins (arrow from 0 to 2)
- Round (3,1): xerxes wins → arrow from 1 to 3 means... wait, dario wins (1,3) so 1 beats 3? But (3,1) xerxes wins means 1 beats 3 from dario's perspective... contradiction.

Wait: (1,3) dario wins → 1 beats 3. (3,1) xerxes wins → xerxes has 1, dario has 3 → 1 beats 3. Consistent!

So wins[d] contains what d beats. Let me figure out the full graph from the standard 5-option circular game where each beats the next 2: i beats (i+1)%5 and (i+2)%5.

Check: 1 beats 2,3. (1,3) dario wins ✓. (4,2): 4 beats 0,1... that gives 4 beats (4+1)%5=0 and (4+2)%5=1. But (4,2) dario wins means 4 beats 2. Doesn't fit simple +1,+2.

Try: i beats (i+1)%5 and (i+3)%5:
- 1 beats 2,4. (1,3) needs 1 to beat 3. No.

Try: i beats (i+2)%5 and (i+3)%5:
- 1 beats 3,4. (1,3) ✓
- 4 beats 1,2. (4,2) ✓  
- 0 beats 2,3. (0,2) ✓
- 1 beats 3,4. (3,1): xerxes has 1, beats 3,4. dario has 3. So 1 beats 3 → xerxes wins ✓

This works!

wins = {i: {(i+2)%5, (i+3)%5} for i in range(5)}

n = int(input())
dario = 0
xerxes = 0
wins = {i: {(i+2)%5, (i+3)%5} for i in range(5)}
for _ in range(n):
    d, x = map(int, input().split())
    if x in wins[d]:
        dario += 1
    else:
        xerxes += 1
print("dario" if dario > xerxes else "xerxes")