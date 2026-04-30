
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
digits = list(map(int, data[1:]))

# Find the last digit
last = digits[-1]

# To get a number divisible by 5, last digit must be 0 or 5 after exactly one swap

# We want the lexicographically largest possible number after exactly one swap
# So we will try to change the last digit to the largest possible 0 or 5
# by swapping with the rightmost possible position that allows the largest number

best = None
best_num = None

# Case 1: Make last digit 0 by swapping with a 0 somewhere
for i in range(N-1, -1, -1):
    if digits[i] == 0:
        # Swap i and N-1
        new_digits = digits[:]
        new_digits[i], new_digits[N-1] = new_digits[N-1], new_digits[i]
        # If this is the first time or better than best
        if best is None or new_digits > best:
            best = new_digits[:]
        break  # since we go from right to left, first 0 we find is the rightmost, which is best for lex largest

# We need to consider all possible swaps that make last digit 0 or 5, and pick the maximum number
# But to get the largest number, we should prefer changes that affect higher positions as little as possible
# i.e., we want to swap the last digit with the largest possible valid digit (5 or 0) from the leftmost? No.

# Actually, since we have to do exactly one swap, and want the largest possible number,
# the best strategy is to iterate over all possible positions to swap with the last position,
# but only if the digit there makes the new last digit 0 or 5.
# Then among all such possible resulting numbers, choose the maximum one.
# Since N<=1000, we can afford O(N) swaps and comparisons.

candidates = []

# Try swapping last position with every other position
for i in range(N-1):
    if digits[i] == 0 or digits[i] == 5:
        new_d = digits[:]
        new_d[i], new_d[N-1] = new_d[N-1], new_d[i]
        candidates.append(new_d)

# Also, we can swap two positions where one is not the last, but the swap makes the last digit 0 or 5.
# That means we must swap the last digit with some position that has 0 or 5.
# If I swap two positions both not last, the last digit doesn't change, so it remains not 0 or 5.
# Since original number is not divisible by 5, last digit is not 0 or 5.
# Therefore, the ONLY way to make it divisible by 5 with one swap is to swap the LAST digit with some other digit that IS 0 or 5.

# So above is complete: we only need to consider swapping the last position with any position that currently has 0 or 5.

if candidates:
    # Choose the maximum one
    best = max(candidates)
    print(' '.join(map(str, best)))
else:
    # Check if there is a 0 or 5 at all
    # If not, impossible
    print(-1)
```

Wait, the above has a bug: when we swap last with a 0 or 5 at position i, if i==0 and it was leading zero, but since we print digits, it's ok.

But in the code above, I have `for i in range(N-1): if digits[i]==0 or ==5`, then create new_d.

Then take max of candidates.

Since lists are compared lexicographically in Python, max() will give the lexicographically largest list, which is what we want (largest number).

But in the first test case:

Input: 7 3 0 1 0 5 6 9 7 5 4 2

Last digit=2

Positions with 0 or 5: index 2:0, 4:0, 5:5, 9:5

If swap with index 9 (5), last becomes 5, number becomes 7 3 0 1 0 5 6 9 7 2 4 5 ? Not matching sample.

Sample output is 7 3 2 1 0 5 6 9 7 5 4 0

So last is 0, meaning we swapped the last 2 with a 0.

There are 0s at positions 2 and 4.

If we swap with the rightmost 0? Position 4 (0-based 4 is fifth digit 0), swapping with last: position 4 and 11.

So number becomes 7 3 0 1 2 5 6 9 7 5 4 0 ? But sample has 7 3 2 1 0 5 6 9 7 5 4 0

That's swapping the 0 at position 2 with the 2 at the end? No.

Original: indices: 0:7,1:3,2:0,3:1,4:0,5:5,6:6,7:9,8:7,9:5,10:4,11:2

Sample output: 7 3 2 1 0 5 6 9 7 5 4 0

So compared to original, the 2 moved to position 2, and the 0 that was at position 2 moved to the end.

Yes, so we swapped position 2 (0) with position 11 (2), resulting in position 2 having 2, and end having 0.

In my code, when I do for i in range(N-1), if digits[i] in (0,5), I swap i with N-1.

So when i=2, digits[2]=0, swap with last: new = original but pos2=2, pos11=0 → exactly 7 3 2 1 0 5 6 9 7 5 4 0 Yes!

And when i=4, digits[4]=0, swap: pos4 gets 2, pos11 gets 0 → 7 3 0 1 2 5 6 9 7 5 4 0 which is smaller than the previous one because at position 2, 0<2.

So max() will correctly choose the one where we swapped the leftmost? No, in this case swapping earlier 0 (at pos 2) puts the 2 earlier, which makes it larger.

Yes, because 732... > 730... yes.

Is max() going to pick the largest? Yes, because Python list comparison is left to right.

Now, what if swapping with a 5 gives even larger?

In sample, there is a 5 at pos 5 and 9.

If swap pos5 (5) with last(2): then pos5=2, last=5 → 7 3 0 1 0 2 6 9 7 5 4 5 which starts with 73010... while the other is 732... so 732 > 730, so correctly max picks the 732... one.

Perfect.

Now, is there a case where we swap to put a 5 at the end but it allows a larger digit earlier? In this logic, since we try all possible i where digits[i] is 0 or 5, and swap it to the end, and the digit that was at end goes to i, and then take the max among all such possibilities, it covers all.

Yes.

What if the position we swap has 5, and putting the old last (say 1) in that position, but if there are multiple, max will choose the best.

Also, important: if there is a 5 or 0 at the last position already? But problem says the number is NOT divisible by 5, so last digit is not 0 or 5.

Good.

Now, look at test 3:

8

0 0 7 8 4 5 3 1

So digits = [0,0,7,8,4,5,3,1], last=1 not 0/5.

Positions with 0 or 5: 0:0, 1:0, 5:5

If swap pos0 with last: last gets 0, pos0 gets 1 → [1,0,7,8,4,5,3,0]

If swap pos1: [0,1,7,8,4,5,3,0]

If swap pos5: [0,0,7,8,4,1,3,5]

Now, which is largest? [1,0,7,8,4,5,3,0] vs [0,1,...] vs [0,0,...]

Clearly 1... is the largest. And sample output is 1 0 7 8 4 5 3 0 Yes!

Perfect. So taking max() works.

Test 5:

7

9 7 4 5 3 5 2

digits=[9,7,4,5,3,5,2], last=2

Positions with 5: index 3 and 5.

Swap with 3: pos3=2, last=5 → 9 7 4 2 3 5 5

Swap with 5: pos5=2, last=5 → 9 7 4 5 3 2 5

Which is larger? 97455.. vs 9745325, at position 3: first has 2, second has 5, 5>2 so 9745... > 9742..., so max picks 9 7 4 5 3 2 5 which matches sample.

Excellent.

Test 2: 7 4 1 2 9 last=9, no 0 or 5 in the number, so -1. Yes.

Test 4: has 5s and 0s.

Seems correct.

One edge case: if swapping with position 0 that has 0, but results in leading zero, but since we are printing digits, not the number, it's allowed. Like in test 3.

Another edge: N=2.

Say 1 2, last=2, if there's a 0 or 5? No, -1.

Say 1 5, but last=5, but problem says not divisible by 5, so last won't be.

Say 5 1, last=1, has 5 at pos0. Swap: 1 5. Ok.

What if multiple same, we take the one that gives largest number, which max does.

Is there a case where to get largest, we should not swap with last? No, as reasoned earlier, because only swapping with last changes the last digit.

Unless the 0 or 5 is already at last, but it's not.

What if we swap two non-last positions, one of them is... no, last stays the same.

Yes.

So only these candidates.

Now, in code, if the digit at i is 0 or 5, we swap.

But what if last digit is say 0, but problem guarantees not.

Good.

Also, if there are multiple same resulting numbers, max is fine.

Now, efficiency: N=1000, candidates up to 1000, each list of 1000, max() will do comparisons, each comparison O(N), so total time O(N^2) worst case, but N=1000, 10^6 operations, fine.

To implement cleanly.

In my first code I had a wrong early break, then corrected in comments.

So final code should be:

Read N, digits.

Then collect all possible after swapping last with a position i that has 0 or 5.

Then if any, print the max one, else -1.

But one more: the problem says "um número decimal não divisível por 5", and "não divisível por 5" in input.

We can assume that.

But what if after swap we get same as original? Only if last was already 0 or 5, which is not.

Good.

Also, leading zeros are allowed in output as in sample 3.

Yes.

So here is the co