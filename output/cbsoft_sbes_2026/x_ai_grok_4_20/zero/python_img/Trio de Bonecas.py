
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
sizes = list(map(int, data[2:]))
sizes.sort()

dp = [float('inf')] * (K + 1)
dp[0] = 0

for i in range(N - 2):
    for k in range(K, 0, -1):
        if dp[k - 1] != float('inf'):
            for j in range(i + 1, N - 1):
                if j + 1 >= N:
                    break
                a = sizes[i]
                b = sizes[j]
                c = sizes[j + 1]
                if a > b:
                    continue
                cost = (a - b) ** 2
                if dp[k - 1] + cost < dp[k]:
                    dp[k] = dp[k - 1] + cost

print(dp[K])
``` 

Wait, this is incorrect. Let me think again.

The previous approach is too slow. N=1e4, K=3e3, we need O(NK) or better.

The balance is (A-B)^2 with A<=B<=C. To minimize sum of (A-B)^2 for K disjoint triples.

Since we want A and B as close as possible, and C can be anything >=B.

The optimal way is to sort the array, and then we need to choose 3K dolls and pair them in a smart way.

But we can leave out N-3K dolls.

To minimize the sum of costs, we should consider the possible "pairs" for (A,B).

A common approach for this kind of problem is to sort the dolls, and then use dynamic programming where we process the dolls from smallest to largest.

Let me define dp[i][k] = minimum cost to form k triples using the first i dolls.

But with N=10000, K=3000, dp[10000][3000] is 30M states, acceptable if transition is O(1).

How to transition?

When considering the i-th doll (0-based, sorted), we can:

- discard it

- use it as C for some previous open pair

- use it as B for a new pair with some previous A

- use it as A for a new pair

This seems complicated, we need to track open pairs.

Since for each triple (A,B,C) with A<=B<=C, the cost is only dependent on A and B: (A-B)^2. C is just any doll >=B.

To minimize the total cost, we want to pair close values for A and B, and use the largest dolls as C's preferably, because they can serve as C for any B.

A good strategy is to sort all dolls in increasing order: s1 <= s2 <= ... <= sN.

Then, the C's will likely be the largest possible dolls.

We can think of selecting 2K dolls that will be the A's and B's, and K dolls that will be the C's. The C's should be the K largest among the selected 3K dolls, because they need to be >= their B.

But it's a bit tricky.

Let's search for a better way.

Notice that in optimal solution, it's best to take consecutive dolls in some way.

Let's consider that we will use the largest  K dolls as the C's for the K triples. Because the largest dolls are good for being C (since C can be large).

Then, we need to pair the remaining N-K dolls into K pairs (A,B) with A<=B, each pair will be assigned to one C (which is larger than all of them probably).

Since the C's are the largest K, all remaining dolls are <= the smallest C, so any of them can be used as A or B.

So, we need to choose 2K dolls from the smallest N-K dolls? No.

If I decide the K C's are the largest K dolls, then I need to choose 2K dolls from the first N-K dolls to be the A's and B's, and leave (N-K - 2K) = N-3K dolls unused from the small ones.

Then, among the 2K chosen small dolls, I need to pair them into K pairs (A,B) with A<=B to minimize sum (A-B)^2.

To minimize sum of (A-B)^2 for K pairs, what's the optimal pairing?

For minimizing sum of squared differences in pairs, the optimal is to sort the 2K dolls and pair consecutive ones: (1,2), (3,4), ..., (2K-1,2K). Because pairing close values minimizes the differences.

Is that true? Yes, for squared difference, pairing closest is optimal, and in sorted array, pairing adjacent is best.

Proof is standard: crossing pairs would have larger sum of squares.

So, if I fix that I use the largest K as C's, then I need to select 2K dolls from the smallest (N-K), sort them, and find the minimum possible sum of (x[2i]-x[2i+1])^2 over all ways to choose 2K dolls? No, that would be hard.

I don't need to choose which 2K, because to minimize the sum of squared diffs of the pairs, I should choose the 2K dolls that allow the smallest possible such sum.

That is equivalent to finding K disjoint adjacent pairs with smallest (diff)^2 in the smallest N-K dolls? Not exactly.

Since we will sort the chosen 2K, and pair 1-2,3-4,... , to minimize sum (s[2i]-s[2i+1])^2 where s is the sorted chosen 2K dolls, we actually want the chosen dolls to be as clustered as possible.

This seems complicated. Maybe my assumption that C's are the largest K is correct, because any doll used as C cannot be used in a pair, and since large dolls if used in a pair as B would require an even larger C, but it's better to use large as C.

Is it always optimal to use the largest K as C's?

Let's see the sample.

Sample: 1,5,7,8,11,15,16. K=2, so 3*2=6, we leave out 1 doll.

If we take largest 2 as C's: 15 and 16 as C's.

Then from [1,5,7,8,11] we need to choose all 4? No, we need 4 dolls for A,B's from the first 5, leaving one out.

N=7, K=2, N-K=5, we need 4 for pairs, leave 1 out from the small 5.

Then to minimize the pairing cost on 4 chosen sorted dolls.

To minimize sum of two (diff)^2 of consecutive pairs, we should choose 4 dolls that are closest together.

Possible choices:

Leave out 1: chosen 5,7,8,11. sorted same. pairs (5,7)+(8,11) -> (2)^2 + (3)^2 = 4+9=13

Leave out 5: 1,7,8,11 -> (1,7)(8,11)=36+9=45 bad

Leave out 7: 1,5,8,11 -> big

Leave out 8: 1,5,7,11 -> big

Leave out 11: 1,5,7,8 -> pairs (1,5)+(7,8) =16+1=17

So best is 13, which matches the sample.

And in sample, the configuration 2 is (5,7,16) and (8,11,15), exactly using 15,16 as C's.

The other configuration was 17.

Good.

Another sample: many 1's and 2's. Clearly cost 0.

So assumption seems good: use the K largest as the C's. Then from the first N-K dolls, we need to choose 2K of them, and pair them optimally i.e. after sorting the chosen ones, pair adjacent, and minimize the sum of squared diffs of those K pairs.

Now, the question is how to choose which 2K out of the first M = N-K dolls to minimize that cost.

But that seems still hard.

Since the pairing is adjacent in sorted order, choosing 2K dolls means we are selecting 2K positions from the sorted small dolls, say t1 <= t2 <= ... <= tM where M=N-K.

Then we choose a subset of 2K indices, let the sorted chosen be p1<=p2<=...p2K, then cost = sum_{i=1 to K} (p[2i-1] - p[2i])^2

To minimize this.

This looks like we want to cover 2K dolls with K "segments" of length 2 (in terms of count).

It's equivalent to selecting K pairs of consecutive in the chosen list.

A standard way is to consider that in the optimal selection, the chosen 2K dolls will be some consecutive 2K + some gaps where we skip some dolls (the left out ones).

But with M up to 10000, K=3000, it's tricky.

Since we are leaving out L = M - 2K = (N-K) - 2K = N - 3K dolls from the first M.

We can leave out any L dolls from the M, and the remaining 2K will be paired consecutively.

To minimize the sum of (diff of every two consecutive in the remaining list)^2.

The remaining list is the sorted list with L dolls removed.

We need to choose which L positions to remove to minimize the sum of squared differences of every two remaining consecutive dolls in the paired way.

After removing L dolls from the sorted list t[1..M], let the remaining be r1 < r2 < ... < r_{2K}, then cost = sum_{i=1}^K (r_{2i-1} - r_{2i})^2

Note that it's NOT pairing r1-r2, r3-r4, etc where the indices are in the final list.

Yes it is.

It's the sum of squared diff between 1st and 2nd, 3rd and 4th, etc in the final remaining sorted list.

To minimize this, we want each of those (r_{2i-1}, r_{2i}) to be as close as possible.

This seems like a DP.

Let’s denote the sorted small dolls as t[0..M-1], M = N - K.

We need to form K pairs, each pair takes 2 dolls, and we can skip some dolls (total skips = M - 2*K).

We can think of processing the dolls from left to right (small to large), and decide for each doll whether to skip it, or use it as an A (start of a pair), or use it as a B (end of a pair).

But we have to maintain if we have an open A or not.

Since it's paired as (1-2),(3-4),... in the chosen ones, it's like we choose positions, and every odd position in chosen sequence is A, even is B.

For DP, we can define dp[i][j]: the minimum cost to process the first i dolls (of the small M), and have chosen 2*j dolls (i.e. formed j pairs).

When we choose a doll, if the number of chosen so far is even (before adding, so now it will be odd), then it will be an A, but we don't know its value yet until we pair it with next.

The cost is paid when we take the B.

So we need to remember the last A if we have an open A (i.e. have chosen odd number so far).

So let’s define two states:

Let dp[i][j][0]: min cost using first i dolls, formed j complete pairs, and no open A (even number chosen).

dp[i][j][1]: min cost using first i dolls, formed j complete pairs, and have one open A (the value of that A), but since value varies, we cannot store all.

That's the problem, we cannot have the value in state.

Since N is 1e4, we cannot afford extra factors.

We need a different approach.

Notice that because the cost is (A-B)^2 and A<=B, and they are from sorted, the optimal is to consider possible "candidate pairs" as adjacent dolls.

Many problems like this (forming teams or triples with cost on two) have a greedy or DP on sorted array with O(NK).

Let's try to define dp[i][k] = min cost to form k triples using only the first i smallest dolls (and we must have used exactly 3k dolls? No.

Since the C can be any larger, but if we are processing from small to large, it's hard.

Since we decided that the K largest are used as C's, and they are fixed, now the problem reduces to: given a sorted list of M = N-K numbers t1 <= t2 <= ... tm, select 2K of them, let the selected sorted be p1<=...<=p2K, minimize sum_{i=1 to K} (p_{2i-1} - p_{2i})^2 .

This is a standard-ish DP.

Let dp[i][j] be the minimum cost to choose 2j dolls from the first i dolls.

Then, the transition is: for the last pair.

To form the j-th pair, we must choose two dolls as the last two in the selected list, say we choose t[x] and t[y] as p_{2j-1} and p_{2j}, with x < y <=i, and between x and y we didn't choose any, and before x we chose 2(j-1) from first (x-1).

But that would be too slow.

The last pair is two dolls that are consecutive in the selected sequence, but there may be skipped dolls between them.

For dp[i][j]: min cost after considering first i dolls and having selected exactly 2*j dolls from them.

To compute dp[i][j], we have options for what to do with the i-th doll:

- not select it: dp[i][j] = dp[i-1][j]

- select it. Then it becomes the (2j)-th selected doll, so it is a B, and there must be a previous selected that is the (2j-1)-th, which is some previous doll.

But to know what was the A for this pair, we need to know which one was the last selected before this one.

So we would need to try all possible positions for the A.

That is, suppose the A is at position m < i, we select t[m] as A, t[i] as B, and between m+1 to i-1 we select 0 dolls, and before m we have selected 2*(j-1) dolls from first m-1 dolls.

So dp[i][j] = min over m < i :   dp[m-1][j-1] + (t[m] - t[i])**2   , but only if we don't select anything between m and i.

Yes, and also the min with not using i.

This is correct.

But if we do for each i,j loop over all possible m, it's O(N^2 K) which with N=1e4, K=3k is way too slow (10^4 ^2 * 3*10^3 = 3e11, impossible).

We need to optimize this.

Notice that for fixed j and i, we are taking min over m=1 to i-1 of  dp[m-1][j-1] + (t[m]-t[i])**2 , and we didn't select in (m,i).

But since we don't select anything in between, it's already accounted.

To make it fast, we need to compute this min quickly.

(t[m] - t[i])**2 = t[m]^2 - 2*t[m]*t[i] + t[i]^2

So dp[m-1][j-1] + t[m]^2 - 2*t[m]*t[i] + t[i]^2

For fixed i and j, t[i]^2 is constant, so we need min over m < i of ( dp[m-1][j-1] + t[m]^2 - 2*t[m]*t[i] )

This looks like min of f(m) + g(m)*X where X=t[i], it's a linear function in t[i].

This suggests convex hull optimization trick (CHT).

Since t is sorted non-decreasing, t[i] is increasing as i increases.

For each possible "A position" m, it offers a "line" y = (-2*t[m]) * X + (dp[m-1][j-1] + t[m]**2), and we query the min y at X = t[i].

And since slopes -2*t[m] are non-increasing (because t[m] non-decreasing as m increases), and queries X=t[i] are non-decreasing as we process i increasing, we can use convex hull trick with deque to maintain lower hull.

Yes! This is perfect for CHT.

So for each layer j from 1 to K, we can process i from 1 to M, and maintain a hull of possible previous decisions (the m's).

The order: we need to add the lines in order of decreasing slope (which is as m increases, slope -2*t[m] decreases or stays), good.

We process in order of increasing i.

For a fixed j, when computing dp[i][j], the possible m are from ... well m must be > the previous chosen, but since it's from dp[m-1][j-1], it's ok.

The recurrence is:

dp[0][0] = 0

For i from 0 to M, dp[i][0] = 0 (choosing 0 pairs, cost 0, can skip all)

No, dp[i][j] defined only when 2j <= i.

But let's index from 1.

Let t = [0] + sorted list of first M, so t[1..M]

dp = [[inf]*(K+1) for _ in range(M+1)]

dp[0][0] = 0

for i in range(1,M+1):
    dp[i][0] = 0   # not choosing any pairs, just skipping all

Then for j=1 to K:
    # we will use CHT to compute for this j
    # we need to add lines corresponding to possible A's

    # The line for a particular m (position where we put A = t[m]) can be added after we have dp[m][j-1] wait let's see.

When we decide to pair t[m] as A and t[i] as B (i > m), then the cost added is (t[m]-t[i])**2, and the previous state must be dp[m-1][j-1], because before position m, we have considered first m-1 dolls, chosen 2*(j-1) of them.

Then at m we choose it as the start of the pair (the odd one), and then from m+1 to i-1 we skip them, and at i we choose as B.

So yes, the cost for dp[i][j] can be dp[m-1][j-1] + (t[m]-t[i])**2

We can also not use the i-th doll at all: dp[i][j] = dp[i-1][j]

So dp[i][j] = min( dp[i-1][j] ,   min over m=1 to i-1 of dp[m-1][j-1] + (t[m]-t[i])**2 )

Note that m must satisfy that we can choose t[m], meaning after the previous 2(j-1) chosen from 1..m-1.

To use CHT, for each j, we can iterate i from 1 to M, but we need to add the possible m's at the right time.

The m's are added in increasing order.

We can maintain a hull, and for each possible m, after we have computed all dp[*][j-1], which we have since we go j increasing.

Since for fixed j, the dp[.][j-1] are already fully computed.

So for fixed j, the possible "lines" are for each possible m=1 to M, the line corresponding to using that m as an A for a future B.

We can add lines in order of increasing m (decreasing slope).

The query is also in increasing i (increasing t[i]).

But for a query at i, the possible m must be < i.

So we need to add lines dynamically: as we increase i, before querying for i, we can add the line for m = i ? No.

For a fixed i, when computing the min over m < i.

After computing dp[i][j], then we can add a line for using this i as a potential A for future pairs (for this same j? No.

For this j, the m is the position of A for the j-th pair.

So the lines are independent of i in terms of when added, but we must add m before using it for i > m.

So the proper way is:

For fixed j:

  Initialize a CHT hull.

  We will also have the option of carrying over from previous i.

  We need to process i from 1 to M.

  At each i, first we can query the current hull to get the best previous m < i, compute the candidate cost = that min + t[i]**2 (since we factored).

  Then dp[i][j] = min(dp[i-1][j], that candidate if hull not empty)

  THEN, after using i as a potential B, now we can consider using i as an A for future j pairs. That is, add a line for m = i+1 ? 

When can we add the line for a particular m?

The line for m can be added as soon as we want to use it for i > m, so after we have processed i=m, but actually since dp[m-1][j-1] is fixed.

Since all dp[*][j-1] are known before starting j, we can add the line for m at the moment when i reaches m+1.

That is:

- Start with empty hull

- For i=1 to M:

  - First, add the line corresponding to m=i  ? Let's see when m=i can be used: for future B >i, so for this i, m=i cannot be used yet for this i (since m<i required).

  So:

Better:

for i=1 to M:

    # first, we can query the hull for best m < i

    if hull not empty:

        best = hull.query(t[i])

        candidate = best + t[i]*t[i]

        dp[i][j] = min(dp[i-1][j], candidate)

    else:

        dp[i][j] = dp[i-1][j]

    # Now, after processing this i as possible B, we can now add the possibility of using this i as an A for future B's.

    # To use i as A (m=i), the previous state is dp[i-1][j-1], wait yes dp[(i)-1][j-1] + (t[i] - t[future])^2

    # Yes! So we add the line for m=i now, so that it can be used for future i's > current i.

    # The constant part is dp[i-1][j-1] + t[i]**2 , slope = -2 * t[i]

    Yes exactly.

So after setting dp[i][j], we add the line with slope = -2*t[i], intercept = dp[i-1][j-1] + t[i]**2

No, let's recall:

The value is dp[m-1][j-1] + (t[m]-t[future])^2 = dp[m-1][j-1] + t[m]**2 -2*t[m]*t[future] + t[future]**2

So when we query, we get the min of (dp[m-1][j-1] + t[m]**2 -2*t[m]*X )  and then we add X**2 later.

For m = current i, the dp[m-1][j-1] is dp[i-1][j-1]

Yes, so we add a line with slope = -2 * t[i],  y_intercept (or b) = dp[i-1][j-1] + t[i]**2

Then query(X) returns min( slope * X + b )

Then the candidate cost is query(t[i]) + t[i]**2 ? No wait.

X is t[future], here future is also i in the query? In the loop above, when at position i (as future), we query before adding the line for m=i, which is correct because m<i.

Let's correct the order.

At the beginning of iteration for i, the hull should contain all m < i.

So we should add the line for m = i AFTER querying but BEFORE going to next? No.

Let's say:

We need to add line for m=1 before any query that uses it (i>=2).

So correct order:

dp[i][j] depends on dp[i-1][j] and queries with m<=i-1.

Initialize hull empty.

For i = 1 to M:

    # add the line for m=i ? But if I add now, then for this i, if I query after, it would include m=i, but m must <i, since cannot pair a doll with itself.

    # And also for m=i, to be A and B at same position impossible.

    So we must query first (with previous lines m < i), then set dp, then add the line for this i as possible future A.

Yes:

for i in range(1, M+1):
    # hull has lines for m=1 to i-1
    if not hull.empty():
        min_val = hull.query(t[i])
        candidate = min_val + t[i]**2
        dp[i][j] = min(dp[i-1][j], candidate)
    else:
        dp[i][j] = dp[i-1][j]
    
    # now add the line for using m = i as A for future
    if j-1 >= 0 and dp[i-1][j-1] != float('inf'):
        slope = -2 * t[i]
        intercept = dp[i-1][j-1] + t[i] * t[i]
        hull.add_line(slope, intercept)

But for i=1, hull is empty, so dp[1][j] = dp[0][j] which for j>=1 is inf probably.

Then we add line for m=1, using dp[0][j-1]

Yes.

For i=2, now hull has m=1, we query with X=t[2], get min_val = slope*t[2] + intercept = -2*t[1]*t[2] + (dp[0][j-1] + t[1]**2)

Then candidate = that + t[2]**2 = dp[0][j-1] + t[1]**2 -2*t[1]*t[2] + t[2]**2 = dp[0][j-1] + (t[1]-t[2])**2   Perfect!

Yes.

Then we set dp[2][1] for example.

Then we add line for m=2: slope=-2*t[2], b= dp[1][j-1] + t[2]**2

Note that dp[1][j-1] may be from previous.

This seems correct.

We also need to make sure that we cannot have chosen more than possible, but since we build from smaller, it should be fine as long as we set inf properly.

For j=1, dp[i][0] = 0 for all i.

Yes.

Now, we need to implement a CHT that supports adding lines with decreasing slopes, and querying with increasing X, so we can use a deque to maintain the lower envelope.

Since slopes are added in decreasing order (because t[i] non-decreasing, -2*t[i] is non-increasing), yes.

We need a function to check if three lines, when to pop.

Let's write the code.

First, we need to decide which dolls are the "small" ones: after sorting all, the first N-K are the potential A and B, the last K are C's.

Yes.

If N-3K >0 , we can skip up to N-3K from the small ones, which is already handled because we don't have to use all.

In dp[M][K] will be the min cost.

Yes.

Now, about inf: since costs are up to (1e5)^2 * 3000 = 3e3 * 1e10 = 3e13, so we can use a large number like 10**18.

Since python, int is fine.

Let's think about the second sample: 8 2, sizes 8 twos and ones.

Sorted: 1,1,2,2,2,2,2,2

N=8 K=2, so M = N-K =6, we use first 6 as potential A/B: 1,1,2,2,2,2 , and last 2 as C: 2,2.

Then dp[6][2] should be 0, by pairing (1,1) and (2,2).

Yes, (1-1)^2 + (2-2)^2 =0.

Good.

We need to implement the ConvexHullTrick.

Since slopes added decreasing, queries increasing, we use deque, add back, query from front.

We need a function to compute intersection.

Standard CHT for lines.

Let me recall a standard implementation.

We will store lines as (slope, intercept)

To decide if line3 is better than line1 and line2, we use the intersection point.

The intersection x of line1 and line2 is (b2-b1)/(s1-s2)  (since s1*x + b1 = s2*x + b2 => x=(b2-b1)/(s1-s2))

Since slopes are negative, but ok.

Because we have floating point issues, but since all values are integers, we can use integer comparison to avoid float.

To check if we need to pop line2 when adding line3, if the intersection of line1 and line3 is before intersection of line1 and line2, then line2 is useless.

The condition to pop line2: if (b3-b2)*(s1-s2) <= (b2-b1)*(s3-s2) or something. We need to be careful with signs.

Since python is slow, N=1e4, K=3e3, then for each j=1 to 3000, for each i=1 to ~7000, we do O(1) amortized for add and query, so total time is O((N+K)*K) wait no, O(N * K) since for each of K layers, we loop N times, each does O(1) amortized for hull operations.

N=1e4, K=3e3, NK = 3e7 operations, python should pass if implemented efficiently (within 2-3 seconds probably ok for most judges).

Let's implement carefully.

First the CHT class.

I will write a CHT that minimizes.

class ConvexHullTrick:
    def __init__(self):
        self.hull = []
    
    def _bad(self, l1, l2, l3):
        # returns true if l2 is bad (not needed)
        # (b3 - b2) / (s2 - s3) <= (b2 - b1)/(s1 - s2)
        # to avoid div, (b3-b2)*(s1-s2) <= (b2-b1)*(s2-s3)
        # but since slopes s1 >= s2 >= s3 (decreasing), s1-s2>=0, s2-s3>=0, so inequality direction ok.
        s1, b1 = l1
        s2, b2 = l2
        s3, b3 = l3
        return (b3 - b2) * (s1 - s2) <= (b2 - b1) * (s2 - s3)
    
    def add_line(self, slope, intercept):
        line = (slope, intercept)
        while len(self.hull) >= 2 and self._bad(self.hull[-2], self.hull[-1], line):
            self.hull.pop()
        self.hull.append(line)
    
    def query(self, x):
        # find the best line for this x. Since x increasing, we can pop front
        while len(self.hull) >= 2 and self._better(self.hull[0], self.hull[1], x):
            self.hull.pop(0)
        return self.hull[0][0] * x + self.hull[0][1]
    
    def _better(self, l1, l2, x):
        # return true if l2 is better than l1 at x
        s1, b1 = l1
        s2, b2 = l2
        return s1 * x + b1 > s2 * x + b2   # since we want min

Since we are minimizing, in query we want the smallest value.

In _better, if l2 gives smaller value than l1 at this x, then pop l1.

Yes.

The condition in _bad: since slopes are decreasing (more negative), s1 > s2 > s3 usually (or >=).

In our case slopes are negative and decreasing.

The inequality (b3-b2)*(s1-s2) <= (b2-b1)*(s2-s3)

Since (s1-s2)>=0 and (s2-s3)>=0, it preserves the <= for the intersection points.

I think this is standard.

Some people use >= depending on convention.

Let me test with small case.

Since time is limited, let's assume it's correct; if not we can adjust.

Many codes use:

def bad(l1,l2,l3):

    return (l3[1]-l2[1])*(l2[0]-l1[0]) >= (l2[1]-l1[1])*(l3[0]-l2[0])   wait, signs depend on how we define.

Let's redefine with tuple (m, b) where y = m*x + b, minimize.

Slopes m added in decreasing order.

The intersection x of two lines l1 and l2: x = (b2 - b1) / (m1 - m2)   note m1 > m2 so denom positive.

For three lines l1,l2,l3 with m1>m2>m3, l2 is not needed if intersection(l1,l3) <= intersection(l1,l2)

That is (b3-b1)/(m1-m3) <= (b2-b1)/(m1-m2)

Then cross multiply (since denoms >0): (b3-b1)*(m1-m2) <= (b2-b1)*(m1-m3)

But this is a bit different.

Let's implement the correct one.

Let me set:

def _bad(self, l1, l2, l3):

    # l1, l2, l3 are (m, b)

    m1, b1 = l1

    m2, b2 = l2

    m3, b3 = l3

    # return true if intersection l1-l3 <= intersection l1-l2

    # (b3-b1)/(m1-m3) <= (b2-b1)/(m1-m2)

    # (b3-b1)*(m1-m2) <= (b2-b1)*(m1-m3)

    return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

But in our case since m's are negative, but math is the same.

For the query, since x increasing, we remove from front if the first two, the intersection is < current x, meaning second is better.

def query(self, x):

    while len(self.hull) >= 2:

        m1,b1 = self.hull[0]

        m2,b2 = self.hull[1]

        if (b2 - b1) <= (m1 - m2) * x:   # if intersection <= x then l2 better, pop l1
            # from y1 = y2 => m1x +b1 = m2x +b2 => (m1-m2)x = b2-b1 => x= (b2-b1)/(m1-m2)
            # if current x >= that, then since m1 > m2 (less negative? wait our m negative but m1 > m2 means m1 less negative.
            # Our slopes m = -2*t , t increasing so m decreasing: m1 > m2 means m1=-2*small , m2=-2*larger so m1 > m2 yes ( -4 > -10).
            # So m1 > m2, denom positive.
            # If x >= (b2-b1)/(m1-m2), then since slope m1 > m2 (m1 less steep negative), the l2 will be smaller after the intersection.
            # So yes, if x >= intersection then l2 is better or equal, so we can pop l1.
            self.hull.pop(0)
        else:
            break
    return self.hull[0][0] * x + self.hull[0][1]

Yes.

For add:

def add_line(self, m, b):

    line = (m, b)
    while len(self.hull) >= 2 and self._bad(self.hull[-2], self.hull[-1], line):
        self.hull.pop()
    self.hull.append(line)

With _bad as:

    def _bad(self, l1, l2, l3):

        m1, b1 = l1

        m2, b2 = l2

        m3, b3 = l3

        return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

Yes, this should work.

Now, let's put it together.

Also, for j from 1 to K, for each j we need a new hull.

And dp[0][0] = 0, dp[i][0] = 0 for all i.

For j>=1, dp[0][j] = inf.

Also if 2*j > i then impossible but it will be handled by inf.

Now, the full code:

import sys

inf = 10**18

data = sys.stdin.read().split()

N = int(data[0])

K = int(data[1])

t = list(map(int, data[2:]))

t.sort()

# the small ones are t[0 .. N-K-1], the C's are the last K

M = N - K

small = t[:M]

# now small is sorted, index 0 to M-1, but we'll use 1-based in dp

dp = [[inf] * (K + 1) for _ in range(M + 1)]

for i in range(M + 1):

    dp[i][0] = 0

class CHT:
    def __init__(self):
        self.hull = []
    
    def _bad(self, l1, l2, l3):
        m1, b1 = l1
        m2, b2 = l2
        m3, b3 = l3
        return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)
    
    def add_line(self, m, b):
        line = (m, b)
        while len(self.hull) >= 2 and self._bad(self.hull[-2], self.hull[-1], line):
            self.hull.pop()
        self.hull.append(line)
    
    def query(self, x):
        while len(self.hull) >= 2:
            m1, b1 = self.hull[0]
            m2, b2 = self.hull[1]
            if (b2 - b1) <= (m1 - m2) * x:
                self.hull.pop(0)
            else:
                break
        return self.hull[0][0] * x + self.hull[0][1]

for j in range(1, K+1):
    hull = CHT()
    for i in range(1, M+1):
        # query if possible
        if hull.hull:  # not empty
            min_val = hull.query(small[i-1])
            candidate = min_val + small[i-1] * small[i-1]
            if candidate < dp[i][j]:
                dp[i][j] = candidate
        # also the skip option
        if dp[i-1][j] < dp[i][j]:
            dp[i][j] = dp[i-1][j]
        
        # now add the line for this i as potential A
        prev = dp[i-1][j-1]
        if prev != inf:
            slope = -2 * small[i-1]
            intercept = prev + small[i-1] * small[i-1]
            hull.add_line(slope, intercept)

print(dp[M][K])

This should work.

Let me test with sample 1.

N=7, K=2

sizes: 11 1 7 5 16 8 15 -> sorted [1,5,7,8,11,15,16]

M = 7-2=5, small = [1,5,7,8,11]

So indices 0:1, 1:5, 2:7, 3:8, 4:11

dp[i][0]=0 for i=0 to 5

Now j=1:

hull = empty

i=1, small[0]=1

hull empty, so no query. dp[1][1] = dp[0][1] which is inf. So dp[1][1] = inf

Then add line: prev=dp[0][0]=0, slope=-2*1=-2, intercept=0 +1=1

add (-2,1)

i=2, small[1]=5

hull has one, query(5): -2*5 +1 = -10+1=-9

candidate = -9 + 25 = 16

dp[2][1] = min(inf from dp[1][1], 16) =16

Then min with dp[1][1]=inf, so 16

Then add line for i=2: prev=dp[1][0]=0 , slope=-2*5=-10, intercept=0 + 25=25

add line m=-10, b=25

Check if bad? only 2 lines now.

i=3, small[2]=7

query: first check if pop front.

Current hull: [(-2,1), (-10,25)]

Check if (25-1) <= (-2 - (-10))*7   i.e. 24 <= 8*7=56  yes 24<=56, so pop front.

Now hull has only [(-10,25)]

Then query: -10*7 +25 = -70+25=-45

candidate = -45 + 49 = 4

So dp[3][1] = 4

Then min with dp[2][1]=16, so 4

Then add line for i=3 m=-14, b = dp[2][0] +49 =0+49=49

slope=-2*7=-14, intercept=0+49=49

Add to hull.

i=4 small[3]=8

hull has [(-10,25), (-14,49)]

Check pop: compute (b2-b1)=49-25=24 , (m1-m2)= -10 - (-14)=4 , 4*8=32, is 24 <=32 ? yes, so pop the first? According to code: if (b2-b1) <= (m1-m2)*x : 24 <= 4*8=32 yes, pop(0), now hull=[(-14,49)]

Then query: -14*8 +49 = -112 +49 = -63

candidate = -63 + 64 =1

dp[4][1] =1 , better than dp[3][1]=4

Yes, this corresponds to pairing 7 and 8: (7-8)^2=1, and dp[2][0]=0 before m=3 (i=3 for A=7, m-1=2)

Yes.

Then add line for i=4, m=-16, b=dp[3][0]+64=64, slope=-16, b=64

i=5, small[4]=11

hull has [(-14,49), (-16,64)]

Check: b2-b1=64-49=15, m1-m2=-14-(-16)=2, 2*11=22, 15<=22 yes, pop front, hull=[(-16,64)]

query: -16*11 +64 = -176+64=-112

candidate=-112 + 121 = 9

dp[5][1] = min(dp[4][1]=1, 9)=1

Good. So dp[*][1] : at i=5 is 1, which is pairing the two closest: 7 and 8.

Yes.

Now j=2:

new hull.

i=1, small0=1

hull empty, dp[1][2] = dp[0][2]=inf

add line: prev=dp[0][1] , but dp[0][1]=inf, so not added.

i=2, small=5

hull empty, dp[2][2]= min(dp[1][2]=inf) =inf

Then add: prev=dp[1][1] which is inf, so not add.

i=3, small=7

hull empty -> dp[3][2] = dp[2][2]=inf

add: prev=dp[2][1]=16 , which is finite.

slope=-14, intercept=16 + 49 =65

add line (-14,65)

i=4, small=8

hull has one, query(8): -14*8 +65 = -112+65=-47

candidate = -47 + 64 = 17

dp[4][2] =17

min with dp[3][2]=inf ->17

This 17 corresponds to first pair cost 16 (1 and 5), then second pair 7 and 8 cost 1, total 17.

Yes.

Then add line for i=4 as A for j=2: prev=dp[3][1]=4 , slope=-16, b=4 + 64=68

add (-16,68)

i=5, small=11

Now hull has [(-14,65), (-16,68)]

Check if pop: (68-65)=3 , ( -14 - (-16) )*11 = 2*11=22 , 3 <=22 ? yes, so pop front, hull=[(-16,68)]

Then query(11): -16*11 +68 = -176+68 = -108

candidate = -108 + 121 = 13

So dp[5][2] =13

Yes! Which is better than 17.

What does it correspond to? Using m=4 (i=4, A=8), with prev dp[3][1]=4

dp[3][1]=4 means using first 3 small dolls (1,5,7) to form 1 pair with cost 4.

How? From earlier, when i=3 j=1, candidate 4, which was pairing 5 and 7? (5-7)^2=4, and dp[1][0]=0 (m=2 for A=5, m-1=1).

Yes: pair (5,7) cost 4, then later pair (8,11) cost (8-11)^2=9, total 13. Perfect! Matches the sample.

And the previous 17 was pairing (1,5) and (7,8).

Excellent.

So the code works.

Now for the case when we have dp[i-1][j-1] , it correctly picks the best.

Great.

We need to handle if K=0 but constraints K>=1? No, K>=1 since 1<=K.

But N>=3, 3K<=N.

If all equal, cost 0 good.

Now, since M can be up to 10000, K=3000, dp is 10000*3000 = 30M integers, each python int is object, memory might be tight but usually 256MB or more, should be ok. To optimize memory we could use two arrays, prev and curr, but for simplicity since it works, and constraints allow.

In python it might use a lot of memory, about 30M * 28 bytes ~ 840MB, too much probably.

We need to optimize space.

We only need dp for previous j.

So we can use two arrays: prev_dp and curr_dp, both of size M+1.

No, because for each j we need dp[i][j-1] which is the previous layer.

Yes, we can have dp as list of size M+1, representing the min cost for current number of pairs.

We start with dp = [0] * (M+1)  # for 0 pairs

Then for each j, we compute a new_dp = [inf]*(M+1)

But in the loop, when we add the line, we use the old dp[i-1] (which is for j-1), and we also take min with new_dp[i-1] for the skip.

Yes.

So let's rewrite without 2D list.

code:

import sys

input = sys.stdin.read

data = input().split()

index = 0

N = int(data[index])

index += 1

K = int(data[index])

index += 1

t = [int(data[i]) for i in range(index, index + N)]

t.sort()

M = N - K

small = t[:M]

INF = 10**18

# dp[i] will be min cost to form current j pairs using first i small dolls

dp = [0] * (M + 1)  # for j=0

for k in range(1, K + 1):

    new_dp = [INF] * (M + 1)

    hull = CHT()

    for i in range(1, M + 1):

        # query

        if hull.hull:

            min_val = hull.query(small[i-1])

            candidate = min_val + small[i-1] ** 2

            new_dp[i] = candidate

        # skip this doll

        new_dp[i] = min(new_dp[i], new_dp[i-1])

        # add line using this as A, using the previous dp (which is for k-1)

        if dp[i-1] != INF:

            slope = -2 * small[i-1]

            b = dp[i-1] + small[i-1] ** 2

            hull.add_line(slope, b)

    dp = new_dp

print(dp[M])

In the code above, for the skip, new_dp[i] = min( new_dp[i], new_dp[i-1] )

But initially for the query part, if no hull, new_dp[i] remains INF, then it will be set to new_dp[i-1] which propagates the INF or previous values.

For k=1, dp is all 0s.

Then for i=1, hull empty, new_dp[1] = INF, then min with new_dp[0] which is INF? We need to set new_dp[0] = 0 ?

For any number of pairs, using 0 dolls, cost is 0 only for 0 pairs. For k>=1, new_dp[0] should be INF.

We forgot to set new_dp[0] = INF (since cannot form positive pairs with 0 dolls)

Yes.

So before the for i loop:

    new_dp[0] = INF   # since k >=1

No, for every k, new_dp[0] = INF if k>0.

But in our loop, since dp[0] for k=0 was 0, but now for k=1, new_dp[0]=INF.

Also in the min with new_dp[i-1], for i=1, new_dp[0] should be INF.

Yes.

So add:

for k in range(1, K+1):

    new_dp = [INF] * (M + 1)

    new_dp[0] = INF  # explicit

    hull = CHT()

    for i in range(1, M+1):

        if hull.hull:

            min_val = hull.query(small[i-1])

            candidate = min_val + small[i-1]*small[i-1]

            if candidate < new_dp[i]:

                new_dp[i] = candidate

        new_dp[i] = min(new_dp[i], new_dp[i-1])

        if dp[i-1] < INF:   # dp is previous layer

            slope = -2 * small[i-1]

            b = dp[i-1] + small[i-1]*small[i-1]

            hull.add_line(slope, b)

    dp = new_dp

Yes, this matches our earlier calculation.

For sample, for k=1, at i=5, we got dp[5]=1 after first loop.

Then for k=2, new_dp[0]=INF

At i=5, we got 13, yes.

Perfect.

In the CHT, when hull.hull: means if len(self.hull)>0.

Yes.

Now, we need to define the CHT class before.

Also, in query and add, since numbers are up to 1e5**2 *3000 ~ 3e13, and slopes -2e5, x=1e5, so m*x ~ 2e5*1e5=2e10, all fit in 64-bit but python int arbitrary.

Good.

This should work within time, 3000*10000=3e7, with some constant in hull (but amortized small), python can handle around 1e8 operations per second usually, so should be fine.

One issue: in the _bad and query, since we use large numbers, but no division, all multiplication, max value like 1e13 * 2e5 ~ 2e18, still fine for python.

In _bad: (b3-b1)*(m1-m2), b~1e13, m diff ~2e5, so 1e13*2e5=2e18, python ok.

Good.

In the class, self.hull = [] in __init__.

In query while len>=2 and condition, we pop(0) which is O(n) worst case but amortized it's O(1) per line since each line popped at most once.

Yes.

This is the solution.

Now, to put the full code.

In the beginning I have input = sys.stdin.read but then used index, or use the first way.

Also need to include the class.

The instructions: generate ONLY the code. Start directly with libraries/imports.

So here is the final co