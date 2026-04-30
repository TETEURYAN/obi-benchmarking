
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

A = [int(x) for x in data[2:2+N]]
B = [int(x) for x in data[2+N:2+2*N]]

posA = [i for i in range(N) if A[i] == 1]
posB = [i for i in range(N) if B[i] == 1]

def min_swaps_to_match(pos1, pos2):
    n = len(pos1)
    total = 0
    for i in range(n):
        total += abs(pos1[i] - pos2[i])
    return total

def compute_for_target(target):
    costA = min_swaps_to_match(posA, target)
    costB = min_swaps_to_match(posB, target)
    return costA + costB

ans = float('inf')

# All possible target position sets
for i in range(K):
    for j in range(i+1, K):
        target = [posA[i], posA[j]]
        ans = min(ans, compute_for_target(target))
        target = [posB[i], posB[j]]
        ans = min(ans, compute_for_target(target))

if K == 1:
    ans = abs(posA[0] - posB[0])
else:
    # Consider matching existing pairs
    for i in range(K):
        for j in range(K):
            t1 = posA[i]
            t2 = posB[j]
            if t1 > t2:
                t1, t2 = t2, t1
            target = [t1, t2]
            ans = min(ans, compute_for_target(target))

print(ans)
``` 

Wait, this is incorrect. Let me think again.

The correct approach is to realize that the final positions for the friends on both sides must be the same set of column indices. So we need to choose K distinct columns where the pairs will sit.

The cost is the total distance the friends on top need to move to those positions (sorted) plus the total distance the friends on bottom need to move to those same positions (sorted). Since they can only swap with adjacent, the number of swaps to move to sorted positions is exactly the sum of absolute differences.

But with N=150000 and K up to 149999, we cannot enumerate all combinations of K positions.

We need an efficient way.

The optimal target positions are the medians or something? No.

Actually, this is a classic problem: we have two sets of points on a line, and we want to match them to the same K positions, minimizing sum of transportation costs.

But more precisely, we need to choose K positions p1 < p2 < ... < pk, and the cost is sum |posA[i] - p_{i+1}| + sum |posB[i] - p_{i+1}| for i in 0 to k-1.

To minimize this over all possible strictly increasing p.

This is a standard dynamic programming problem.

Let me define the positions.

Let me collect the list of all friend positions, but no.

Since both groups must move to the same set of positions, and the cost is independent, it's sum over i of |A[i]-P[i]| + |B[i]-P[i]| where P is sorted chosen positions.

To minimize sum_i (|A[i]-P[i]| + |B[i]-P[i]|) over all 0 <= P[0] < P[1] < ... < P[K-1] < N.

This is a classic DP.

Let C[j] = |A_sorted_to_j - j| no.

The P are the final column indices (0-based).

We need to choose K distinct columns, assign the i-th smallest chosen column to the i-th friend on A and on B (since they will sort themselves optimally).

Yes.

So let f[0..K-1] be the chosen columns, strictly increasing.

Cost = sum_{i=0}^{K-1} (abs(posA[i] - f[i]) + abs(posB[i] - f[i]))

We need min cost over all 0 <= f0 < f1 < ... < f{K-1} < N.

This can be computed with dynamic programming.

Let dp[k][j] = min cost to place first k friends (0 to k-1) using columns up to j as the last position.

But with N=1.5e5, K up to 1.5e5, we need O(NK) is too slow (2e10).

We need a better way.

Notice that the cost for each possible column j being used as the m-th position is abs(posA[m] - j) + abs(posB[m] - j).

So for each "pair index" m (from 0 to K-1), if we assign column j to it, cost is abs(posA[m]-j) + abs(posB[m]-j).

And we need to assign increasing columns to increasing m.

This is minimum cost to assign K distinct positions to K "demands" with cost c[m][j] = abs(posA[m]-j) + abs(posB[m]-j), with j strictly increasing.

This is a classic assignment with convex costs, can be solved with divide and conquer optimization or knuth optimization in O(K log N + N) or O(KN) but we need faster.

Since the cost abs(x-j) + abs(y-j) = abs(x-y) + 2*max(0, j-max(x,y)) + 2*max(0, min(x,y)-j) or something.

Actually abs(a-j) + abs(b-j) is a piecewise linear function with minimum at the median of {a,b}, which is any point between min(a,b) and max(a,b), and slope -2 left, +2 right.

So the total cost is sum over m of that.

To minimize sum over chosen distinct j's assigned in order.

This seems tricky but there is a greedy way.

Let's search for the standard way to solve this.

This problem is from OBI, likely 2018 or so, and with N=1.5e5, it must be O(N log N) or O(N).

The key insight is that the optimal matching is to match the friends in order, but we need to find the best "alignment".

No, the final positions will be some consecutive? No.

Since both sides will move their friends to the same positions, and movements are like sorting the positions.

The number of swaps on one side to move to positions p1 < p2 < ... < pk is exactly sum |pos[i] - p[i]| because each swap with adjacent is like bubble sort steps, and it's known that the minimal number of adjacent swaps to move tokens to target positions (without crossing unnecessarily) is the sum of distances if we match sorted to sorted.

Yes, that's correct.

So we need min over all strictly increasing sequences p0 < p1 < ... < p_{k-1} of sum_i |posA[i]-p_i| + |posB[i]-p_i|.

To compute this efficiently.

This is a well-known problem that can be solved using dynamic programming with convex hull optimization trick because the cost functions are convex.

Let’s define dp[i][j] : minimum cost to place the first i groups (i friends) using the first j columns (last column is j-1).

Let’s 0-index.

Let dp[k][j] = min cost to assign the first k positions (for the first k friends, k from 1 to K) with the k-th friend pair assigned to column j (j from 0 to N-1).

Then dp[1][j] = abs(posA[0]-j) + abs(posB[0]-j) for each j.

Then for k=2 to K:
dp[k][j] = abs(posA[k-1]-j) + abs(posB[k-1]-j) + min over i < j of dp[k-1][i]

This is the recurrence.

But if we do it naively it's O(K N^2) way too slow.

But notice that we are taking min of all previous, so we can maintain the minimum so far of dp[k-1].

No, for each k, dp[k][j] = cost[k][j] + min_{i=0 to j-1} dp[k-1][i]

Yes! Because the previous position can be any i < j, and since there is no other constraint, it's just the minimum of all dp[k-1][0..j-1].

So we can maintain a prefix minimum for each layer.

This is O(K*N) which for 150000*150000 is 2.25e10, impossible.

But K and N are both 1.5e5, so we need O(N) or O(N log N).

We need a closed form or different approach.

The final p's are chosen, and each p is assigned to one "slot" i in order.

But perhaps we can think of all the desired positions from A and B.

The total cost is sum_i |posA[i] - p[i]| + |posB[i] - p[i]| = sum_i f_i(p[i]) where f_i(x) = |posA[i]-x| + |posB[i]-x|

And p strictly increasing.

This is like choosing distinct integers p and assigning in order to minimize sum f_i(p_i).

Since f_i are all convex, the optimal p can be found greedily or with two pointers.

There is a standard greedy algorithm for this: using median or something.

Let's consider that for each possible "pairing column" j, it contributes to one of the K "slots".

But perhaps a better way: notice that in the end, the p[i] will be such that they are the positions where we "place" the pairs.

But let's consider the list of all posA and posB.

Let's consider that we can model it as matching the two multisets in a certain way.

The minimal number of adjacent swaps is the number of steps the friends need to move.

Since on each side the friends can move independently (the non-friends are just obstacles but since we can swap, it's like the friends can move freely but the cost is the total steps).

The sum |current - target| is indeed the total number of adjacent swaps needed on that side.

So back to the DP.

The recurrence I wrote is correct: dp[k][j] = c[k][j] + prefix_min of dp[k-1] up to j-1.

We can compute each layer in O(N) time by maintaining running min.

So total time is O(K * N), too slow.

But K<=150000, N<=150000, can't.

We need a way to compute this without O(KN).

So we need to find a closed form for the min cost.

Let’s denote XA[0..K-1] = posA, XB[0..K-1] = posB, both sorted (they already are since we collected them in order).

XA is increasing, XB is increasing.

We need to find strictly increasing integers 0 <= P0 < P1 < ... < P{K-1} <= N-1 minimizing sum_{i=0}^{K-1} (|XA[i]-Pi| + |XB[i]-Pi| )

Let g(i, x) = |XA[i]-x| + |XB[i]-x|

g(i,x) = {
  XA[i] + XB[i] - 2*x   if x <= min(XA[i],XB[i])
  |XA[i]-XB[i]|         if min <= x <= max
  2*x - XA[i] - XB[i]   if x >= max(XA[i],XB[i])
}

It's constant between the two positions, and increases linearly with slope ±2 outside.

To minimize sum g(i, Pi) with P strictly increasing.

This is still not easy but there is a way.

I recall that for such problems with absolute deviation, the optimal is to set Pi to the median of some set.

But with the strict increase constraint.

If there were no strict increase constraint, each Pi would be set to the median of XA[i], XB[i], which is any value between them, but we have to make them distinct and ordered.

So the problem is like we have K intervals [min(XA[i],XB[i]), max(XA[i],XB[i])] where the cost is constant, and outside it increases.

To minimize, we want to pick P's inside their "preferred" intervals as much as possible, respecting order and uniqueness.

This sounds like we can use a greedy algorithm where we try to assign the leftmost possible positions.

This is similar to matching with minimal movement.

Let's consider all the "desired" positions from both lists.

Consider that the total cost is sum |XA[i] - Pi| + sum |XB[i] - Pi|.

This is independent per side.

It's the sum of costs to move list XA to P and list XB to P, with P sorted.

To minimize cost_move(XA, P) + cost_move(XB, P) over all combinations P of size K.

Yes.

There is a known way: the optimal P is the K positions that are the "best" according to some criteria? 

Let's think differently.

Suppose we decide that the final positions are some set S of K columns.

Then the optimal way to assign is to sort S and assign to sorted XA and XB.

Yes, that's what we have.

To find the best S.

But how to choose which K columns.

The DP I had is the way, but too slow.

But perhaps we can notice that because the cost functions are convex, we can use the divide and conquer optimization for DP, but in my recurrence it's not the standard form.

In my recurrence dp[k][j] = c[k][j] + min_{i<j} dp[k-1][i]

This is very special.

The min_{i<j} dp[k-1][i] is just the prefix minimum of the previous dp row.

So we can compute it in O(N) per layer, but K layers is too much.

To speed up, perhaps we don't need all K layers. Maybe we can find when the prefix min changes.

But that seems complicated.

Let's compute what the optimal P is.

Since each g(i,.) is convex, the total cost is convex in the P's, so the optimal P's will be as close as possible to the "preferred" positions.

A standard way for this kind of problem is to use two pointers or greedy.

Let's consider pairing the i-th friend from top with i-th from bottom in some alignment.

No.

The final positions P must satisfy that for the ordered P, the cost is sum ( |XA[i]-P[i]| + |XB[i]-P[i]| ).

To minimize this, we can think of it as each possible column j can be chosen or not.

If chosen as the r-th position, it has cost |XA[r]-j| + |XB[r]-j|.

The decision of which rank it gets.

This is hard.

Let's look at the sample.

First sample:
N=6, K=2
A: 0 1 0 0 1 0  => posA = [1,4]
B: 1 0 1 0 0 0  => posB = [0,2]

The example says optimal is positions 2 and 4? In 1-based? The description says positions 2 and 4.

Assuming 1-based in description: upper friends at 2 and 5 (1-based), so 1,4 0-based.
Lower at 1 and 3, so 0,2 0-based.

Then they end up at 2 and 4 (1-based so 1,3 0-based?).

In the description:
After moves, both sides have friends at positions 2 and 4.

Assuming 1-based.

So P = [1,3] (0-based).

Cost for A=[1,4] to [1,3]: |1-1| + |4-3| = 0+1 =1
For B=[0,2] to [1,3]: |0-1| + |2-3| =1+1 =2
Total 3, matches the sample.

Is there better? If P=[0,1]: cost A: |1-0|+|4-1|=1+3=4, B:|0-0|+|2-1|=0+1=1, total 5 >3
P=[1,2]: A:|1-1|+|4-2|=0+2=2, B:|0-1|+|2-2|=1+0=1, total 3 same.
P=[2,3]: A: |1-2|+|4-3|=1+1=2 , B:|0-2|+|2-3|=2+1=3, total 5
P=[3,4]: A:|1-3|+|4-4|=2+0=2, B:|0-3|+|2-4|=3+2=5, total 7

So 3 is optimal.

Another sample has output 0, which is when posA and posB are already the same.

Now, to find an efficient algorithm.

Notice that because we take prefix min, the dp[k][j] = c[k][j] + min( dp[k-1][0] , dp[k-1][1], ..., dp[k-1][j-1] )

Let M[k-1][j] = min of dp[k-1][0 to j]

Then dp[k][j] = c[k][j] + M[k-1][j-1]   (with care for j=0)

This can be computed sequentially but still O(KN).

But perhaps we can see that the optimal P[i] will be max( XA[i], XB[i] ) or min or something.

Let's consider for each "slot" i, the preferred range is [L[i], R[i]] where L[i] = min(XA[i], XB[i]), R[i] = max(XA[i], XB[i]).

Inside [L,R] the cost for that pair is |XA[i]-XB[i]| which is constant.

Outside it costs extra 2 per unit distance.

So the base cost is sum |XA[i]-XB[i]| over i, and then we have to pay extra if we cannot fit the P's inside their ranges without overlapping.

The problem reduces to: we have K intervals [L[i], R[i]], we need to pick one distinct integer from each interval, with the chosen points strictly increasing (P0 < P1 < ...), or if we can't, we have to go outside the intervals paying 2 per unit outside.

If we can find strictly increasing P with L[i] <= P[i] <= R[i] for all i, then the min extra cost is 0, total cost is sum |XA[i]-XB[i]|.

But in the sample, for i=0: XA[0]=1, XB[0]=0, so L=0, R=1, constant cost |1-0|=1
i=1: XA=4, XB=2, L=2,R=4, constant cost 2
Base cost = 3.

Can we pick P0 in [0,1], P1 in [2,4], P0 < P1 ? Yes, e.g. P0=1, P1=2 or P0=0,P1=2 etc. Yes, so extra cost 0, total cost 3, which matches.

In the 4th sample:
posA = [0,3], posB=[0,3]
L = [0,0], R=[3,3]? For first: min(0,0)=0 max=0
Second min(3,3)=3 max=3
So intervals [0,0] and [3,3], and 0<3, yes, can pick P=[0,3], extra=0, and |0-0|+|3-3|*2=0, yes.

Third sample:
N=9 K=4
A:1 1 1 1 0 0 0 0 0 => posA = [0,1,2,3]
B:1 0 0 1 0 1 0 0 1 => posB = [0,3,5,8]

So XA=[0,1,2,3], XB=[0,3,5,8]
Intervals:
i=0: min(0,0)=0, max=0
i=1: min(1,3)=1,3
i=2: min(2,5)=2,5
i=3: min(3,8)=3,8

Base cost = 0 + 2 + 3 + 5 = 10

Can we assign increasing P with P0 in [0,0], P1 in[1,3], P2 in[2,5], P3 in[3,8] ?

P0 must be 0.
Then P1 >0, in[1,3] ok.
P2 > P1, in[2,5]
P3 >P2 in[3,8]

Yes easily, e.g. 0,1,2,3. So extra cost 0, total cost should be 10, and the sample output is 10. Yes!

Another sample 2:
N=12 K=4
A: 0 0 1 0 1 1 0 0 0 0 1 0 => posA = [2,4,5,10]
B: 0 1 0 0 0 1 0 0 0 1 0 1 => posB = [1,5,9,11]

XA = [2,4,5,10]
XB = [1,5,9,11]

Intervals:
i=0: min(2,1)=1, max=2
i=1: min(4,5)=4,5
i=2: min(5,9)=5,9
i=3: min(10,11)=10,11

Base cost = |2-1| + |4-5| + |5-9| + |10-11| = 1+1+4+1 = 7

Can we pick P0 in[1,2], P1 in[4,5], P2 in[5,9], P3 in[10,11] with strictly increasing?

Possible: e.g. 1,4,5,10
Is 1<4<5<10 yes.
Or 2,4,6,10 etc.

Yes, so extra=0, total cost 7, and sample output is 7. Perfect!

So in all samples, the min cost is just sum_{i=0}^{K-1} |posA[i] - posB[i]| 

Is that always the case?

Is it always possible to find such non-crossing assignment inside the intervals?

No. Let's think of a case where intervals force overlap.

Suppose K=2, N=5
posA = [0,1]
posB = [2,3]

Then intervals:
i=0: min(0,2)=0,2
i=1: min(1,3)=1,3

Base cost = 2+2=4

Can pick P0 in[0,2], P1 in[1,3], P0<P1 easily yes.

Another example: suppose posA = [0,3], posB=[1,2]

XA=[0,3], XB=[1,2]
intervals:
i=0: min(0,1)=0,1
i=1: min(3,2)=2,3

Base =1 +1 =2

Can we pick P0 in[0,1], P1 in[2,3], P0 < P1 : yes, 0<2, 1<2, 1<3 etc.

Now suppose a case where it fails.

Suppose K=2, XA=[0,1], XB=[0,1]

Then intervals both [0,0] and [1,1]? min(0,0)=0,0 ; min(1,1)=1,1. Can pick 0<1, good. Cost=0+0=0

Suppose K=3, XA=[0,1,2], XB=[0,1,2], cost 0.

Good.

Suppose overlapping badly.

Suppose XA = [1,2], XB=[0,3], N=5, K=2

intervals:
i=0: min(1,0)=0,1
i=1: min(2,3)=2,3

Good.

Let's try to find when it's not possible to pick without extra.

Suppose two intervals that force conflict: for example K=2
XA=[0,2], XB=[3,4]
No:
i=0 min(0,3)=0,3
i=1 min(2,4)=2,4
Still can pick 0 and 2? 0 in [0,3], 2 in[2,4], 0<2 yes.

Another try: XA=[3,4], XB=[0,1]
Then XA[0]=3, XA[1]=4, XB[0]=0, XB[1]=1
intervals:
i=0: min(3,0)=0,3
i=1: min(4,1)=1,4
Still can pick P=[0,1], is 0 in[0,3] yes, 1 in[1,4] yes.

Or [2,4] etc.

The cost would be for P=[0,1]: |3-0|+|4-1| + |0-0|+|1-1| = 3+3 +0+0 =6
But base cost is |3-0| + |4-1| =3+3=6, yes.

If I pick P=[3,4]: cost for A:0+0, for B: |0-3|+|1-4|=3+3=6, total 6 same.

Now, is there a case where we must pay extra?

Suppose K=2, N=3, positions XA=[0,2], XB=[0,2]
intervals i=0: [0,0], i=1:[2,2]
Can pick 0 and 2, good.

Suppose K=3, N=4, XA=[0,1,3], XB=[0,2,3]
intervals:
i=0: min(0,0)=0,0
i=1: min(1,2)=1,2
i=2: min(3,3)=3,3

Can we pick P0=0, P1=1 or 2, P2=3. Yes as long as P1<3 which is true.

Good.

Let's suppose a case where intervals are [0,0], [0,0], but since positions are distinct, XA and XB can't have two at same if K>1? Positions are distinct because they are different chairs.

posA are distinct, posB are distinct.

But the L[i] = min(XA[i],XB[i]), R[i]=max(XA[i],XB[i])

Since XA is increasing, XB is increasing.

This is important: both sequences are strictly increasing.

So XA[0] < XA[1] < ... < XA[K-1]
XB[0] < XB[1] < ... 

Therefore L[i] = min(XA[i], XB[i]), R[i] = max(XA[i], XB[i])

Now, is it always possible to select P[i] in [L[i], R[i]] with P[0] < P[1] < ... < P[K-1] ?

Not necessarily.

Consider this: suppose XA = [0,3], XB = [1,2], N=4, K=2

L[0] = min(0,1)=0, R[0]=1
L[1] = min(3,2)=2, R[1]=3

Then P0 in [0,1], P1 in [2,3], P0 < P1 always since 1<2. Good.

Now suppose XA=[0,1], XB=[2,3]
L0=min(0,2)=0 R0=2
L1=min(1,3)=1 R1=3
Good.

Now let's make conflict: suppose K=3
XA = [0, 1, 5]
XB = [2, 3, 4]

Then L = [min(0,2)=0,2], [min(1,3)=1,3], [min(5,4)=4,5]
So intervals: [0,2], [1,3], [4,5]

Can we pick 3 increasing numbers?
Possible P0=0 (in0-2), P1=1 (in1-3), P2=4 (in4-5). Yes 0<1<4.

Good.

Another try: XA=[0,4,5], XB=[1,2,3]
L=[0,1], [2,4], [3,5]
Good.

Suppose XA=[2,3,4], XB=[0,1,5]
L[0]=min(2,0)=0,2
L[1]=min(3,1)=1,3
L[2]=min(4,5)=4,5

Possible P0=0, P1=1, P2=4 : 0 in[0,2],1 in[1,3],4 in[4,5] and 0<1<4 yes.

Seems always possible?

Is it always true that we can find such P?

If so, then the answer is always sum |posA[i]-posB[i]| for i in 0..K-1 !!

Let's see if this makes sense with the problem.

In the problem description, they did 3 swaps, and |1-0| + |4-2| =1+2=3 yes! It matches.

In all samples it matches.

Is this the case?

But is it always possible to choose P[i] \in [min(XA[i],XB[i]), max(XA[i],XB[i])] with P strictly increasing?

This is equivalent to whether we can select one number from each interval with strict increase.

This is a classic problem and since the intervals are "sorted" in some sense (because XA and XB are sorted), it turns out we can always do it by choosing P[i] = max( L[i], P[i-1]+1 ) and check if <= R[i], or something.

There is a greedy way: the latest possible or earliest.

But let's see a counterexample where it's impossible.

Suppose K=2, XA=[0,3], XB=[4,5], N=6
L[0]=min(0,4)=0,4
L[1]=min(3,5)=3,5
Can easily.

Suppose XA=[1,2], XB=[0,4]
L0=min(1,0)=0,1
L1=min(2,4)=2,4
P0 <=1, P1>=2, so P0=0 or 1, P1=2,3,4 with P0<P1 ok.

Now suppose this: K=3, XA=[1,2,3], XB=[0,4,5]
L = [min(1,0)=0,1], [min(2,4)=2,4], [min(3,5)=3,5]
Good.

Suppose the intervals are nested or crossed badly.

Suppose XA = [0, 5], XB = [1, 2], K=2 N=6
XA[0]=0, XA[1]=5 , XB[0]=1, XB[1]=2
Then L[0] = min(0,1)=0, max=1
L[1] = min(5,2)=2, max=5

P0 in [0,1], P1 in [2,5], P0 < P1 : yes, max P0=1 < 2=min P1.

Good.

Suppose K=3 XA=[0,1,6], XB=[2,3,4]
L[0]=min(0,2)=0,2
L[1]=min(1,3)=1,3
L[2]=min(6,4)=4,6

Now, suppose we try to pick:
If I pick P0 as large as possible? Or small.

If I use greedy left to right, take smallest possible:
P0 = 0 (smallest in [0,2])
P1 = max(P0+1, L[1]) = max(1,1)=1, which is <=3 ok
P2 = max(P1+1,4)= max(2,4)=4 <=6 ok.

Good.

Suppose a failing case: imagine intervals [0,2], [0,2], [0,2] but can that happen?

For that, for i=0: max(XA0,XB0)<=2, min>=0
But since XA[0] < XA[1] < XA[2], if all XA[i] in 0..2, but there are only 3 positions 0,1,2 so XA=[0,1,2], then for XB also to make all R[i]<=2, XB[i] <=2, but XB also 3 distinct in 0-2, impossible because only 3 spots.

Since there are K distinct on each side, but the point is the intervals may overlap a lot.

Suppose N=5, K=3
XA = [0,1,2]
XB = [0,1,4]

Then L,R:
i=0: min(0,0)=0,0
i=1: min(1,1)=1,1
i=2: min(2,4)=2,4

Intervals: [0,0], [1,1], [2,4]

Then P=[0,1,2], which is in the intervals, and strictly increasing. Good.

Suppose XA=[0,1,4], XB=[2,3,4]
L,R:
i=0 min(0,2)=0,2
i=1 min(1,3)=1,3
i=2 min(4,4)=4,4

P0 in0-2, P1 in1-3, P2=4.
As long as P1 <4 which is true. Can pick 0,1,4 or 2,3,4. Good.

It might be that due to the sorted nature, it's always possible to assign without leaving the intervals.

Is that true?

Let me try to prove it.

We can use induction or greedy.

Consider the following algorithm: set P[i] = max( XA[i], XB[i], P[i-1]+1 ) no.

A known result or we can use Hall's marriage theorem or something.

We can assign P[i] = median or.

Consider that one possible choice is to set P[i] = max(XA[i], XB[i]) for each i.

Is this strictly increasing?

max(XA[i], XB[i])  ??

Not necessarily, e.g. if XA=[0,3], XB=[4,5], then max0=4, max1=5, 4<5 good.

If XA=[0,4], XB=[1,2], then max for i=0: max(0,1)=1, i=1 max(4,2)=4, 1<4 good.

If XA=[0,1,2], XB=[3,4,5]: max =[3,4,5] good.

If XA=[3,4,5], XB=[0,1,2]: then max(i=0)=max(3,0)=3, i=1=max(4,1)=4, i=2=5 good.

Another: XA=[1,3,4], XB=[0,2,5]: max= [1,3,5], is 1<3<5 good.

Seems increasing.

Is max(XA[i], XB[i]) always non-decreasing?

Suppose XA[i] = 5, XB[i]=0, but since XB is increasing, if XB[i]=0 then previous XB[i-1]<0 impossible.

Since both XA and XB are strictly increasing sequences, consider f(i) = max(XA[i], XB[i])

Suppose f(i) > f(i+1) for contradiction.

Then max(XA[i],XB[i]) > max(XA[i+1], XB[i+1])

But XA[i] < XA[i+1], XB[i] < XB[i+1]

It's known that max of two increasing functions is not necessarily increasing, but wait:

Suppose XA[i]=2, XA[i+1]=3
XB[i]=5, XB[i+1]=6 then max 5,6 increasing.
Suppose XA[i]=2, XA[i+1]=10
XB[i]=4, XB[i+1]=5 then max(2,4)=4 , max(10,5)=10 , 4<10 good.
Suppose XA[i]=5, XA[i+1]=6
XB[i]=3, XB[i+1]=4 then max(5,3)=5, max(6,4)=6 good.

It seems hard to have decrease.

Assume f(i) >= f(i+1)
That is max(a_i, b_i) >= max(a_{i+1}, b_{i+1}) where a=XA, b=XB, a_i < a_{i+1}, b_i < b_{i+1}

Let M = max(a_i, b_i)
Then M >= a_{i+1} and M >= b_{i+1}

But a_{i+1} > a_i , b_{i+1}>b_i

If a_i == M, then since M >= a_{i+1} > a_i =M, contradiction.

Similarly if b_i ==M, then M >= b_{i+1} > b_i = M, contradiction.

Yes! So it's impossible. Therefore f(i) = max(XA[i], XB[i]) is strictly increasing!

Beautiful!

We can always choose P[i] = max(XA[i], XB[i]), and it satisfies P[i] < P[i+1], and clearly P[i] >= XA[i] and >= XB[i], so it's within [min, max]? No, max is exactly the upper bound, so yes P[i] = R[i] which is in [L[i],R[i]].

Therefore it is always possible to choose such P inside the intervals, so the extra cost is always 0.

Therefore the minimal total swaps is always sum over i |posA[i] - posB[i]| !!!

In the first sample: |1-0| + |4-2| =1+2=3 yes.

In fourth sample: |0-0| + |3-3| =0 yes.

In third: |0-0| + |1-3| + |2-5| + |3-8| = 0+2+3+5=10 yes.

In second: |2-1|+|4-5|+|5-9|+|10-11| =1+1+4+1=7 yes.

Perfect!

So is this the answer? It seems almost too simple, but the math checks out.

Is the cost sum |posA[i]-posB[i]| ?

In the calculation earlier, when we choose P[i] = max(XA[i],XB[i]), then the cost for that pair is |XA[i]-P[i]| + |XB[i]-P[i]| = |XA[i]-max| + |XB[i]-max| = since max is the larger one, it's |smaller - larger| = |XA[i]-XB[i]| yes.

And since we can always do it, there is no extra movement needed beyond that.

If we chose P[i] inside the interval, the cost for each individual is still |XA-XB|, so total same.

Yes.

Is there a case where we can get lower than that? No, because for each i, no matter what P you choose for that slot, the cost for that slot is at least |XA[i]-XB[i]|, by triangle inequality or from the piecewise definition. So the sum is a lower bound, and since we achieved it, it is the minimum.

Perfect!

So the minimal number of trocas (swaps) is sum_{i=0}^{K-1} |posA[i] - posB[i]|

And that's the answer.

Now, with N up to 1.5e5, it's efficient.

We just need to collect the positions where A[i]==1 and B[i]==1, and compute the sum of abs differences.

Note that positions are 0-based or 1-based doesn't matter as long as consistent.

Yes.

Let's confirm with the constraint K < N, and N>=2, K>=1.

Yes.

If the positions overlap in a way that max are not distinct? But we proved it's strictly increasing.

Suppose two consecutive have same max? But from the contradiction, it can't be equal either? In the proof, if equal, then if a_i = M, then a_{i+1} > a_i =M but M >= a_{i+1} implies a_{i+1}<=M, contradiction. Same for b. So yes strictly increasing.

Great.

So the code is very simple.

Now, according to the instructions, generate ONLY the code, no other text.

It must read from stdin and output the number. 

Since N is large, better to read efficiently, but in python it's fine. 

Here is the code: 
```python
import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
K = int(data[index])
index += 1

A = []
for _ in range(N):
    A.append(int(data[index]))
    index += 1

B = []
for _ in range(N):
    B.append(int(data[index]))
    index += 1

posA = []
for i in range(N):
    if A[i] == 1:
        posA.append(i)

posB = []
for i in range(N):
    if B[i] == 1:
        posB.append(i)

ans = 0
for i in range(K):
    ans += abs(posA[i] - posB[i])

print(ans)
``` 

This should work.

In the problem, the swaps are only on the same side. The total swaps is the sum on both sides, which is exactly sum |posA[i]-P[i]| over i plus sum |posB[i]-P[i]| over i, which equals sum |posA[i]-posB[i]| as we have.

Yes.

And in the example they moved upper by 1, lower by 2, total 3.

Yes.

I think this is the solution. 

Is there a case where this is not optimal? Suppose we choose different matching, not matching the i-th with i-th.

No, because the P must be assigned in order: the leftmost P to the leftmost friend on that side, because friends can't cross each other (since to cross they'd need to swap with each other but the problem allows only swapping with neighbor, but if two friends swap it would cost but in terms of final positions, since they are identical, but wait.

The friends are indistinguishable, so we don't have to match the order?

No, the posA is the current positions of the K friends on top, sorted.

When we choose target positions P sorted, we assign the leftmost target to the current leftmost friend? No.

Since they can move by swapping with non-friends, but friends cannot cross each other on the same side, because to cross, two friends would have to pass through each other, which would require them to be adjacent and swap, but if they swap, then their order changes.

But the problem is, are the friends distinguishable? For the purpose of "each friend facing another friend", since all friends are equivalent, it doesn't matter which friend faces which.

But on one side, the order of specific friends doesn't matter, but since they are identical, the target is just to have friends in certain K positions on top and same K positions on bottom.

So the cost to move the current friend positions to the target positions, since friends are identical, we should match the sorted current positions to the sorted target positions, and the minimal adjacent swaps is indeed sum |current_sorted[i] - target_sorted[i]|.

Yes, that's standard in these kinds of problems (like rearranging with adjacent swaps, the number is the L1 distance after sorting).

So yes, our approach is correct.

We cannot re-order the friends arbitrarily without extra cost; the optimal matching is indeed sorted to sorted.

So everything checks out.

Thus the code above is the soluti