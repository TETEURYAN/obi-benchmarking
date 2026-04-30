
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
L = list(map(int, data[1:]))

total = sum(L)
if total % 2 != 0:
    print("N")
    sys.exit()

half = total // 2

prefix = [0] * (2 * N + 1)
for i in range(2 * N):
    prefix[i + 1] = prefix[i] + L[i % N]

found = False
for i in range(N):
    target1 = prefix[i] + half
    target2 = prefix[i] + total // 2
    if target2 > prefix[i] + total:
        continue
    left = i + 1
    right = i + N
    while left <= right:
        mid = (left + right) // 2
        if prefix[mid] == target1:
            pos1 = mid % N
            for j in range(1, N):
                if (pos1 + j) % N == i:
                    break
                target3 = prefix[pos1] + (prefix[(pos1 + j) % N] - prefix[pos1]) % total
                if target3 == target2 % total:
                    found = True
                    break
            if found:
                break
            left = mid + 1
        elif prefix[mid] < target1:
            left = mid + 1
        else:
            right = mid - 1
    if found:
        break

if found:
    print("S")
else:
    print("N")
``` 

Wait, this is incorrect. Let me think again.

The correct approach for this problem is to realize that for four points on a circle to form a rectangle, they must form a rectangle inscribed in the circle, which means the diagonals must be diameters of the circle.

Since it's a circle, any rectangle inscribed in a circle must be a rectangle with diagonals as diameters, and in fact, all rectangles can be inscribed in a circle with the diagonals as diameters.

But more importantly, the two diagonals must both be diameters, meaning they must both span exactly half the circumference.

So, the four points divide the circle into four arcs, and for it to be a rectangle, the opposite arcs must be equal, or more simply: the points must be at positions where the chord lengths (in arc terms) correspond to the diagonals being equal to the diameter.

Since the trees are on the circumference, to form a rectangle, the diagonals must both be diameters of the circle. That means the arc between two opposite vertices must be exactly half the circumference.

So, if we consider the cumulative arc lengths, we need to find if there are four distinct points A, B, C, D in order such that the arc AC and arc BD are both exactly half the total circumference.

In other words, we need two distinct pairs of points that are exactly diametrically opposite (arc length = total/2).

And these two pairs must not share points, and the four points must be distinct.

Since N can be 1e5, we need an efficient way.

First, if total is odd, impossible, since half must be integer (arc lengths are integers).

All Li are integers, so total is integer. For half to be achievable, total must be even.

So first check if sum(L) % 2 == 0.

Let S = sum(L)//2

We can compute the prefix sums.

Let pos = [0]

for i in range(N):
    pos.append(pos[-1] + L[i])

The positions are at 0, L0, L0+L1, ..., modulo total.

But since it's a circle, to find if there is a point at position x + S mod total for a given x.

To have a rectangle, we need two distinct diameters that are not the same.

That is, we need at least two distinct pairs of points that are exactly S arc length apart.

But they must form a rectangle, which they will as long as the four points are distinct.

If I have two different pairs (A,C) and (B,D) where C is A+S mod total, D is B+S mod total, and all four are distinct, then they form a rectangle (actually a rectangle inscribed in circle is always a rectangle).

Any four points where the diagonals are both diameters will form a rectangle.

Yes.

So, the condition is: there exist at least two different starting points i and j such that there exists a point at (pos[i] + S) % total, and (pos[j] + S) % total, and the four indices are distinct.

To implement efficiently, we can put all cumulative positions modulo total into a set.

Since positions are unique? The problem doesn't say the arc lengths are positive, but constraints say 1 ≤ Li, so all arcs >0, so all points are distinct.

Yes.

So:

```python
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
L = list(map(int, data[1:]))
total = sum(L)

if total % 2 != 0:
    print("N")
    sys.exit(0)

S = total // 2

# Compute all prefix sums
prefix = [0] * n
for i in range(1, n):
    prefix[i] = prefix[i-1] + L[i-1]

pos_set = set(prefix)

count = 0
for i in range(n):
    target = (prefix[i] + S) % total
    if target in pos_set:
        count += 1

# Each diameter is counted twice (once from each end)
if count >= 4:
    print("S")
else:
    print("N")
```

This is better.

Because each valid diameter contributes 2 to the count (A to C and C to A).

If we have two distinct diameters, we have 4 endpoints, so count >= 4.

We need to make sure that the diameters are not the same.

If all points have a counterpart, but if there's only one diameter, count would be 2.

Let's check with samples.

First sample:
8
3 3 4 2 6 2 2 2

Sum = 3+3+4+2+6+2+2+2 = 24, S=12

Prefix: 0,3,6,10,12,18,20,22,24

Positions mod 24: 0,3,6,10,12,18,20,22

Now check for each:
0 +12 =12 -> yes
3+12=15 -> 15 not in set
6+12=18 -> yes
10+12=22 -> yes
12+12=24%24=0 -> yes
18+12=30%24=6 -> yes
20+12=32%24=8 -> no
22+12=34%24=10 -> yes

So the points that have opposites: 0,6,10,12,18,22. That's 6 points, count=6 >=4, so S. Correct.

Second sample:
4
14 16 15 15

Sum=60, S=30

Prefix: 0,14,30,45

Positions: 0,14,30,45

0+30=30 -> yes
14+30=44 -> no
30+30=60%60=0 -> yes
45+30=75%60=15 -> no

So only 2, count=2 <4, output N. Correct.

Third sample:
6
3 7 7 3 10 10

Sum=40, S=20

Prefix: 0,3,10,17,20,30

Positions: 0,3,10,17,20,30

0+20=20 -> yes
3+20=23 -> no
10+20=30 -> yes
17+20=37 -> no
20+20=40%40=0 -> yes
30+20=50%40=10 -> yes

So 0,10,20,30 have opposites. count=4 >=4, S. Correct.

Perfect.

Is there a case where count>=4 but it's not a rectangle? For example if all points are at 0 and S, but since arcs >=1, points are distinct.

Suppose we have multiple points but the diameters are the same pair. But since each pair is counted twice, and if only one unique diameter, count=2.

If three diameters, count=6, etc.

What if a point is its own opposite? That would require S=0 mod total, impossible.

Also, note that if we have a square, it works.

This seems correct.

Is it possible to have count=4 but the four points are not forming two distinct diameters? No.

In the example above it works.

One thing: in a circle, if I take two diameters, they always form a rectangle (actually a rectangle, and if angles are 90 degrees wait no, in circle, any two diameters form a rectangle? 

The angles: the inscribed angle.

Actually, since all vertices lie on circle and diagonals are both diameters, then each angle is inscribed in a semicircle, so each angle is 90 degrees. Yes! So it is always a rectangle.

Perfect.

So this is the condition: we need at least two distinct diameters connecting pairs of points.

Which translates to at least 4 "directed" matches, i.e. count >=4.

Yes.

Now, since N=1e5, and we use a set of size 1e5, and loop N times, it's fine. Set lookup is O(1) average.

But in python, with integers up to 1e5 * 1e6 = 1e11, but since we do % total, but in prefix we didn't mod, but in set I put the prefix without mod, but when computing target I did % total.

That's a bug.

In the code above, prefix = [0, L0, L0+L1, ...] so up to sum of n-1 elements < total.

Then pos_set = set(prefix)  # all < total

Then target = (prefix[i] + S) % total

If prefix[i] + S < total, then it's prefix[i]+S, which may be in set.

If prefix[i] + S >= total, then (prefix[i]+S)%total = prefix[i]+S - total, which is < S, and may be in set.

Since all positions in set are between 0 and total-1, it's fine.

Yes.

In first example, for i at 18, 18+12=30%24=6, and 6 is in set. Yes.

Good.

We need to make sure we don't count a point paired with itself, but since S = total//2, and total>=4 (N>=4, Li>=1, total>=4), S >=2, so !=0.

Good.

This should work.

Final code:

We should use fast input.

But this is fine.

Let me write it clean