
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
sizes = list(map(int, data[2:]))
sizes.sort()

# dp[i][j] = min cost using first i dolls to form j trios
INF = 10**18
dp = [[INF] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(K + 1):
        if dp[i][j] == INF:
            continue
        # skip this doll
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        
        # try to form a trio ending at i (as the largest)
        if i >= 2 and j >= 1:
            # possible pairs for the two smaller: (i-2,i-1), (i-1,i) but since sorted i is largest
            # we consider the two smallest possible with this largest
            # actually we need to choose any two before i as A <= B <= sizes[i]
            # but to minimize (A-B)^2 we want A and B as close as possible
            # since we are doing DP on prefix, the optimal is to consider local choices
            
# This approach is too slow. Need a better way.

# Since dolls are sorted, the optimal way is to pair them in a greedy manner but with DP optimization.

# Let's redefine DP.
# After sorting, we will assign dolls from smallest to largest.
# For each trio we choose 3 dolls where the two smallest determine the cost (diff squared).

# The key observation is that in optimal solution, the trios will consist of dolls that are "close" in the sorted list.

# Consider that every trio uses 3 consecutive dolls in some matching.

# But not necessarily.

# Let's think differently.
# Sort the array S[0..N-1] ascending.
# A trio is defined by three indices i < j < k, cost = (S[i]-S[j])**2, and S[k] is just >= S[j].

# To minimize sum of such costs for K disjoint trios.

# This looks like a classic DP on sorted array.

# Define dp[i][j] = min cost to form j trios using the first i dolls (smallest i dolls).

# Transition: for the last trio, we need to choose how many dolls to "skip" or how the last trio is formed.

# When adding the i-th doll, it can be:
# - not used
# - used as the large one in a trio
# - used as one of the two small ones

# But it's tricky.

# Notice that for a trio A <= B <= C, cost = (A-B)**2. C can be any larger or equal.
# To minimize total cost, we want to pair close A and B, and use the remaining as C's.

# The C's don't contribute to cost, only act as "covers".

# So essentially, we need to choose 2K dolls that will be the A and B's (the ones that contribute to cost), paired into K pairs, each pair has cost (smaller-larger in pair)^2, and we need at least K additional dolls to serve as C's (which can be any of the remaining dolls, including larger ones).

# But the pairing must respect that for each pair (A,B), there must be a C >= B. Since array is sorted, if we assign the largest possible as C's it should be fine as long as we have enough dolls.

# Since C can be any doll >= B, and we can assign the largest dolls as C's, the constraint is almost always satisfied as long as we have at least 3K dolls.

# The bottleneck is just selecting 2K dolls for the "paired" positions and K for the "large" positions.

# To minimize the sum of squared differences of the K pairs, we should pair dolls that are close in size.

# The optimal strategy is to sort all dolls, and then consider pairing adjacent dolls.

# We can think of the sorted list. We need to choose K pairs of dolls that will be (A,B), and the cost is sum (B-A)^2 for each pair, and we need to have at least K dolls not in these pairs to serve as C's.

# To minimize the sum, we should choose the K smallest possible (B-A)^2 from possible non-overlapping pairs.

# This sounds like a greedy on possible pair costs.

# Let's consider all possible "consecutive" pairs.

# A standard way for this kind of problem is to use dynamic programming on the sorted array with efficient transitions.

# Let’s sort the sizes: S[0] <= S[1] <= ... <= S[N-1]

# dp[i][j] : minimum total cost to form j trios using the first i dolls.

# To compute dp[i][j], we have options for what to do with doll i-1 (the largest among first i).

# Option 1: don't use doll i-1 at all -> dp[i][j] = dp[i-1][j]

# Option 2: use doll i-1 as a C (the largest in some trio). Then we must have formed the two smaller ones before. So we need to have "pending" two dolls that are not yet paired? This is getting complicated.

# For the last trio, suppose the largest doll in the last trio is S[i-1], then the other two are some S[p], S[q] with p < q < i-1, cost = (S[p]-S[q])**2, and the dolls between q+1 and i-2 must be used in previous trios or not used.

# This is O(N^2 K) which is too slow.

# N=1e4, K=3e3, too big.

# We need O(NK) or O(N log N + NK) solution.

# Let's observe that because C can be any doll larger than or equal to B, the optimal way is to always use the largest available dolls as the C's, and focus on pairing the smallest possible differences for the (A,B) pairs.

# In other words, we should sort the array, and then the K largest dolls will be used as the C's (one for each trio), and the remaining N-K dolls will be used to form the A and B's. No, we need exactly 2 per trio for A and B, so 2K for A+B and K for C, total 3K dolls used, we can leave N-3K unused.

# The unused can be any.

# To minimize sum of K terms of (A-B)^2 with A<=B, we should choose 2K dolls that allow the smallest possible pairing differences.

# The best is to take the 2K dolls that are closest together? Not exactly.

# Actually, since we can choose any 2K dolls for the paired ones, but to minimize pairing cost, we should look at the sorted list and consider the cost of pairing adjacent ones.

# Consider that in optimal solution, the pairs will be made from dolls that are near each other in the sorted order, and the C's will be assigned the largest in each group or something.

# Let's consider the following DP:

# We process the dolls from smallest to largest.

# At each position, we can decide to:
# - leave it unused
# - use it as an A or B in a pair
# - use it as a C

# But we need to track how many open B's we have (dolls that are waiting for a pair).

# This might work but let's see.

# A better observation: since (A-B)^2 is smaller when A and B are closer, and since sorted, the optimal pairs will be non-crossing.

# The optimal way is to consider for each possible pair of consecutive dolls in sorted list as potential (A,B).

# Let's calculate the cost of making a pair from positions i and i+1: cost = (S[i]-S[i+1])**2, then we need one C from somewhere larger.

# If we take many such adjacent pairs, we need to ensure we have enough C's left.

# If we sort the array, then we can use a greedy approach where we consider the possible "pair costs" from adjacent dolls, and we select the K smallest possible pair costs such that no two pairs share a doll, and we have enough dolls left for C's.

# But selecting K non-adjacent pairs with smallest cost is still not trivial.

# The pairs can be (i,j) with j > i+1, but that would have larger or equal diff than pairing closer ones usually.

# Since the array is sorted, (S[i]-S[j])**2 is smaller when j is closer to i.

# So it's always better or equal to pair adjacent rather than skipping.

# Is it optimal to only consider pairing adjacent dolls?

# In the sample:
# Sorted: 1,5,7,8,11,15,16
# If I pair adjacent:
# Possible adjacent diffs: 4,2,1,3,4,1
# Squared: 16,4,1,9,16,1

# To choose 2 pairs without overlapping dolls, and have at least 2 C's.

# For example, pair 7-8 (cost 1), and 15-16 (cost 1), total 2. Then we have dolls 1,5,11 left. We can use any two of them as? No, we need to assign C's to the pairs.

# For pair (7,8), we need a C >=8, we can use 11,15,16 but 15 and 16 are used in other pair.

# If I use (7,8) with C=11, and (15,16) with C= something but we only have 1,5 left which are smaller. Problem.

# We don't have a C for the second pair because the only dolls >=16 are none.

# So we cannot pair (15,16) because there is no C >=16 left.

# This shows that we cannot freely pair any adjacent.

# The C must be >= the B of its trio.

# So the assignment of C is constrained.

# This makes it more like we need to assign the larger dolls as C's preferably.

# Let's think of it this way: in the sorted list, the K trios will "consume" 3 dolls each, but the cost is determined by the two smallest in each trio.

# If we decide which dolls are the "middle" B's and the "small" A's.

# A standard way for this is to realize that the optimal is to group the dolls into K groups of at least 3 dolls each (consecutive in sorted order), but not necessarily, because we can leave some dolls out.

# We can leave up to N-3K dolls unused.

# The unused dolls can be used to "separate" the groups or be discarded.

# But if we assume that the trios are formed from consecutive segments, it may not be optimal but let's see the sample.

# In sample, the optimal is (5,7,16) cost (5-7)^2=4 and (8,11,15) cost (8-11)^2=9, sum 13.

# The groups are not consecutive without overlap.

# Dolls used: 5,7,8,11,15,16. Left out 1.

# The pairs are (5,7) and (8,11).

# They are almost consecutive.

# Another way: is there a better than 13? The sample says 13 is the min.

# Let's see if we can get lower.
# Pair (7,8) cost 1, then we need two C's >=8. We have 11,15,16. So we can take C=15 and C=16. Then for the other trio we need another pair. We have 1,5,11 left. We can pair 1 and 5 cost 16, and use 11 as C (but 11>=5 yes). Total cost 1+16=17, which is the first configuration.

# Pair (8,11) cost 9, (5,7) cost 4, then C's can be 15 and 16 for both since both B's are 7 and 11, 15 and 16 are larger. Total 13.

# Pair (11,15) cost 16, (7,8) cost 1, then for the pairs, B's are 15 and 8. For B=15 we need C>=15, we have 16. For B=8 we can use 1? No 1<8. Dolls left are 1,5,16. So C for 15 is 16, for 8 we have to use 5 or 1 but both <8. Not possible.

# So indeed 13 is best.

# To solve this systematically, let's go back to DP on the sorted array.

# Let S be the sorted list.

# We will define dp[i][j] = the minimum total cost to form j trios using only the first i smallest dolls.

# That is, we have considered dolls 0 to i-1.

# To transition, we need to decide how many dolls from the end are used for the last few trios.

# But to make it efficient, notice that when we form a trio, the C can be the largest doll in that trio, so we can assume that in each trio the largest is the C.

# So each trio is exactly 3 dolls: A, B, C with A<=B<=C, cost (A-B)**2.

# We don't have to use more than 3 per trio; using more than 3 would mean leaving some dolls in between unused or in other trios.

# But we can leave dolls unused, so it's equivalent to choosing 3K dolls out of N, grouping them into K groups of 3 consecutive in the chosen subset, with cost for each group (first-second)^2.

# The chosen 3K dolls in sorted order T[0] < T[1] < ... < T[3K-1], then we group them as (T[0],T[1],T[2]), (T[3],T[4],T[5]), etc, and the cost would be sum (T[3m]-T[3m+1])**2 for m in 0 to K-1.

# Is that optimal? In the sample, the chosen dolls are 5,7,8,11,15,16. So T = [5,7,8,11,15,16]
# If we group as (5,7,8) cost (5-7)^2=4, and (11,15,16) cost (11-15)^2 =16, total 20 which is worse than 13.

# But earlier we had a better grouping: (5,7,16) and (8,11,15). Note that the C's are not the third in sorted order within group.

# In terms of the chosen dolls, the pairing is not pairing adjacent in the chosen subset.

# In first trio: 5,7,16 -> A=5 B=7
# Second: 8,11,15 -> A=8 B=11

# So the A's and B's are 5,7 and 8,11. The C's are 16 and 15.

# In the sorted chosen, it's mixed.

# The pairing is the 1st and 2nd, 3rd and 4th in the chosen list, and the 5th and 6th are used as C's.

# Yes! That gives cost (5-7)^2 + (8-11)^2 = 4+9=13, which matches the optimal.

# If I had grouped as first two for first pair, next two for second pair, last two as C's.

# This seems promising.

# Generalizing: to form K trios, we select 3K dolls, sort them as T[0] <= T[1] <= ... <= T[3K-1].
# Then we pair T[0] with T[1], T[2] with T[3], ..., T[2K-2] with T[2K-1] as the (A,B) pairs, and use T[2K], T[2K+1], ..., T[3K-1] as the C's.
# Since the sequence is sorted, for each pair T[2m], T[2m+1], the corresponding C can be any of the larger T's, and since there are K such C's all larger than or equal to T[2K-1] >= all the B's, it is guaranteed that we can assign C's to all pairs.

# This works.

# Now, is the optimal always achievable this way? That is, is the optimal matching always pair the smallest 2K dolls in order as adjacent pairs?

# In the sample it worked.

# In the second sample: 8 dolls, all 1 or 2. Clearly we can make pairs of equal sizes, cost 0.

# Yes.

# Is this always optimal?

# Suppose we have sizes: 1,2,3,4,5,6, and K=2, N=6.

# If we take all, T=[1,2,3,4,5,6], pair 1-2 cost 1, 3-4 cost 1, C=5,6. Total cost 2.

# Pair 2-3 cost 1, 4-5 cost 1, total also 2.

# Is there better? No.

# Another example where crossing might be better? Since it's squared diff, and sorted, pairing closest possible should be good.

# Suppose we have 1,10,11,12,20. K=1, N=5. Then 3K=3.

# Possible choices:
# Choose 1,10,11: but according to above, T=[1,10,11], pair first two 1 and 10, cost 81, C=11.
# Choose 10,11,12: pair 10-11 cost 1, C=12. Much better.

# The DP will choose the best 3 dolls that minimize the (smallest - middle)^2.

# In our method, we need to choose which 3K dolls to pick to minimize the sum of (T[2i]-T[2i+1])**2 for i=0 to K-1.

# Yes.

# So now the problem reduces to: choose a subsequence of 3K dolls from the sorted list (or equivalently select positions), but since it's sorted we just choose increasing indices.

# We need to select 3K positions from 0 to N-1, let the selected indices be p1 < p2 < ... < p_{3K}, then the cost is sum_{m=0}^{K-1} (S[p_{2m+1}] - S[p_{2m}]) ** 2

# Note indices starting from 0.

# We want the minimum such cost over all choices of 3K indices.

# This is a standard DP!

# We can define dp[i][j]: the minimum cost to choose 2*j + r dolls from the first i dolls, where r is the number of "open" C slots or something? Wait.

# Since we pair them in order: every two selected dolls contribute a cost if they are in the "pair" positions, and every third is a free C.

# As we pick dolls from left to right (smallest to largest), we assign them in order to the next available slot in the "virtual" T list.

# The slots are: pair1_A, pair1_B, pair2_A, pair2_B, ..., pairK_A, pairK_B, C1, C2, ..., CK.

# But since all C's are at the end, when we pick a doll it is assigned to the next position in this sequence.

# So we can think of the positions in the chosen T as 0 to 3K-1, where for even positions < 2K, it is an A, the next odd is B, and cost is added when we pick the B.

# To compute the min cost, we can do DP where we track how many dolls have been picked so far.

# Let dp[i][j] be the minimum cost to consider the first i dolls and have already chosen j dolls for the T list.

# When we choose the j-th doll (0-based) to be S[i-1], if j < 2*K and j % 2 == 1, then we add (S[previous_A] - S[i-1])**2 to the cost.

# So we need to remember what was the previous A for that pair.

# That means we need to know what the last A was.

# This would require extra state.

# Since N=10000, K=3000, 3K <=N so max 9000.

# If we do dp[i][j] with i<=10000, j<= min(i,3*K) , it's 10000*9000 = 90M states, if transition O(1) it's acceptable (around 1-2 seconds maybe in python but tight).

# But we need to know the position of the A when we pick a B.

# So if j is odd and j < 2K, when we decide to pick current doll as position j, we need to know what was S at position j-1.

# We cannot do it without storing the last open A position.

# We can observe that the pairs are independent in terms of when we add the cost: the cost for a pair is added when we pick the second doll of the pair.

# So we can have a state that tracks if we have an "open" A waiting for a B.

# Let's define the state as the number of complete trios (or rather number of pairs made) and whether we have an open A.

# But we also have to count how many C's we have assigned.

# Since the C's are just fillers at the end, but we can pick C's only after all pairs are done? No, in the model, the C's are the last K in the chosen list, meaning we must pick all 2K pair dolls before picking any C? No, that's not true.

# In the T list, the C's are the last K chosen dolls in sorted order. That means all the pair dolls (the smallest 2K chosen) are chosen before the C dolls in value, but since we pick in order it's automatic.

# But in the DP, as we go from left to right, when we decide to pick a doll, it becomes the next in the T sequence.

# The T sequence positions are filled from smallest to largest.

# So the first chosen doll is T[0] = A1, second chosen T[1]=B1, third T[2]=A2, fourth T[3]=B2, ..., up to T[2K-2], T[2K-1], then the next chosen are C's.

# The cost is added when we choose T[1], T[3], T[5],..., i.e., when we choose an odd position in 0-based before 2K.

# To do DP, we can have:

# dp[i][j][0/1]: min cost after considering first i dolls, having chosen j "pair-slots" (i.e. j dolls for the 2K pair positions), and the parity (whether we have chosen an A and are waiting for B).

# More precisely:

# Let’s say we need to fill 2K "pair positions" and K "C positions".

# But the C positions can only be filled after the 2K pair positions are filled, because they are the largest.

# No, in the sequence, yes, we must fill the pair positions first in the chosen sequence. That is, the first 2K chosen dolls (the smallest 2K chosen) will be used for the pairs, and the last K chosen will be the C's.

# So we cannot pick a C until we have picked all 2K pair dolls.

# In DP terms, we first pick exactly 2K dolls that will be used in pairs, grouped as (1st,2nd), (3rd,4th),..., and then pick K more larger dolls as C's.

# Yes.

# So we can split the DP in two phases but since it's sequential it's the same.

# Define dp[i][j] = minimum cost to choose j dolls from the first i dolls to be used as the "pair dolls", where the cost is the sum of squared diffs for the completed pairs.

# But to know the cost we need to know which ones are paired.

# Since they are chosen in order, the 1st chosen is A1, 2nd is B1, cost added at 2nd, 3rd is A2, 4th B2, etc.

# So when we choose the m-th doll for the pair group (m from 1 to 2K), if m is even, we add (current - last_A)^2.

# To do this in DP we need to remember the size of the last A if we are at odd position.

# So let's use state for number of pair-dolls chosen modulo 2.

# Let’s define two arrays:

# Let f[i][k] = min cost to use first i dolls and have selected exactly 2*k pair-dolls (i.e. k complete pairs), with no open A.

# g[i][k] = min cost to use first i dolls and have selected 2*k + 1 pair-dolls (k complete pairs and one open A), and we need to remember the value of that open A.

# But remembering value is impossible unless we keep the index of the open A.

# If we keep the index of the last open A, then state would be too big.

# This is the problem.

# Notice that when we have an open A, it is the last chosen doll.

# When we decide to pick a new doll as B, the A is the previously chosen one.

# So if we only pick when we decide, we can have the DP transition when we pick.

# Let's define the state as position i, number of pairs completed k, and number of dolls chosen for pairs so far mod 2, and if mod 2 ==1, the A is the last picked doll's size.

# But to avoid storing size, we can do the DP by iterating and when we pick we know the current size.

# We can do it by considering at each doll we have options: skip it, or use it as next in the sequence.

# We need to track only the number of chosen so far for the pair phase, and if we are expecting a B or an A.

# Let's code the state as:

# We have to choose exactly 2K pair dolls and then K C dolls.

# But during the pair phase, the cost depends on which are chosen as A's and B's.

# Let’s say current "needed" : we need to track how many pair dolls have been chosen so far.

# If the number chosen so far is even, then next picked will be an A, no cost added, just record its size.

# If the number chosen so far is odd, then next picked will be a B, and we add (A - current)^2, where A was the last picked.

# So to handle this, the state must remember the last A if the current count is odd (waiting for B).

# So we can have two DP tables:

# even[i][k]: min cost after processing first i dolls, having completed exactly k pairs (so 2k dolls chosen), ready to start a new pair or start C phase.

# odd[i][k][last]: but last is size, too many.

# Since N=1e4, we cannot afford extra factors.

# We need a different approach.

# Notice that for a fixed set of chosen dolls for the 2K pair positions, the pairing is fixed: we sort them, pair 1 with 2, 3 with 4, etc.

# The cost is sum (T[2m+1] - T[2m])**2 for m=0..K-1.

# To minimize this, we are choosing 2K positions from the N, say the chosen indices for pair dolls are q1 < q2 < ... < q_{2K}, then cost = sum (S[q_{2m+1}] - S[q_{2m}])**2

# Then, to have K C's, we need at least K dolls after the last pair doll, i.e. we need N - (q_{2K}) >= K ? No.

# The C's must be chosen from the dolls larger than the last B, i.e. from indices > q_{2K}.

# We need at least K dolls with index > q_{2K} (not chosen as pair, but since we didn't choose them yet, all remaining after q_{2K} are available for C's).

# So number of dolls after the last pair doll must be at least K, i.e. N - 1 - q_{2K} >= K - 1, i.e. q_{2K} <= N - K - 1.

# The last pair doll can be at most at position N-K-1.

# Then we can choose any K from the last K + (N-1 - q_{2K} - K +1 wait, as long as there are at least K dolls after it.

# Yes, if the last B is S[p], then there must be at least K dolls with size >= S[p], but since sorted, that means at least K dolls after p or including if equals but since we can use equals, but to simplify since we have already chosen 2K, the number of remaining dolls is N-2K, we need K of them to be >= the last B.

# Since they are the ones after the last chosen for pair, if we choose the 2K-th pair doll at index p, then there are N-p-1 dolls strictly larger or equal? Since sorted, all after p are >= S[p].

# So yes, we need N - p - 1 >= K.

# i.e. p <= N - K - 1.

# The condition is that the 2K-th chosen doll must be at position <= N-K-1.

# Now, the problem is to choose 2K positions 0 <= r1 < r2 < ... < r_{2K} <= N-K-1, and minimize sum_{m=0 to K-1} (S[r_{2m+1}] - S[r_{2m}]) ** 2

# This is choosing 2K increasing indices up to M = N-K, and minimize that sum.

# This looks like a min cost to pick 2K items with cost associated with every two consecutive picks.

# This is perfect for DP.

# Let dp[i][j] = minimum cost to choose j dolls for the pair slots, using up to doll i (last chosen is i or not).

# More precisely dp[i][j] = min cost to choose j pair-dolls from the first i+1 dolls (indices 0 to i), with the j-th doll being doll i.

# Then the transition depends on whether j is odd or even.

# If j is even (j%2==0), then this doll i is a B (since  j starts from 1? let's index from 1.

# Let’s say we have to pick 2K dolls, the 1st picked (smallest) is A1, 2nd is B1, 3rd A2, 4th B2, etc.

# When we pick the t-th doll in the chosen pair list, if t is even, it is a B, and the cost can be added from the previous A which is the (t-1)-th picked.

# So in DP, dp[i][t] = min cost to pick t pair-dolls, with the t-th being doll i (index i).

# To compute it, we need to minimize over the previous picked doll position prev < i, dp[prev][t-1] + cost if t even.

# If t is even, then we add (S[prev_for_A] - S[i])**2 but the A is not the immediate previous picked if t even? The immediate previous is the A for this pair.

# Yes! When t is even, the (t-1)-th picked is the A for this pair, and t-th is the B.

# So the previous state dp[prev][t-1], where prev is the position of the A, and we add (S[prev] - S[i])**2.

# If t is odd, then this is an A (except for t=1), and there is no cost to add, the previous is some B from previous pair.

# The transition is:

# For t odd: dp[i][t] = min over prev < i of dp[prev][t-1]   (no extra cost)

# For t even: dp[i][t] = min over prev < i of dp[prev][t-1] + (S[prev] - S[i])**2

# This is correct.

# The final answer is min over all i where i <= N-K-1, dp[i][2*K] 

# Because the last doll (the 2K-th, which is a B since 2K even) is at i, and we need i <= N - K -1.

# Now, the problem is how to compute this efficiently.

# N=10000, 2K <= 6000, if we do naive it would be O(N^2 * K) which is 1e4^2 * 3e3 = 3e11, way too slow.

# We need to optimize the transitions.

# Notice there are two types of transitions.

# This is a classic convex hull optimization or something because of the cost.

# Let's see the transitions separately for odd and even layers.

# Let’s number the picks from 1 to 2K.

# When transitioning to an odd t (meaning picking an A), the cost added is 0, so dp[i][t] = min_{prev < i} dp[prev][t-1]

# That is just the minimum of all dp[*][t-1] for prev < i. So we can maintain the running min.

# When transitioning to an even t (picking a B), dp[i][t] = min_{prev < i} ( dp[prev][t-1] + (S[prev] - S[i])**2 )

# Let's expand the cost: (S[prev] - S[i])**2 = S[prev]^2 - 2*S[prev]*S[i] + S[i]^2

# So dp[i][t] = S[i]**2 + min over prev < i of ( dp[prev][t-1] + S[prev]**2 - 2*S[prev]*S[i] )

# This is of the form min ( f(prev) + b(prev) * x(i) ) where x(i) = S[i], b(prev) = -2*S[prev], f(prev) = dp[prev][t-1] + S[prev]**2

# This looks like linear functions y = m * x + b, where each previous prev offers a line with slope m = -2 * S[prev], and intercept = dp[prev][t-1] + S[prev]**2

# Then for a query at x = S[i], we want the min m*x + intercept.

# Since S is sorted non-decreasing, the queries x = S[i] are non-decreasing.

# Also, the slopes m = -2*S[prev] are non-increasing because S[prev] is increasing as we add prev in order.

# Since we process i from left to right, and for each layer t, we compute dp[i][t] for i from 0 to N-1 in order.

# For a fixed t (even), when computing dp[*][t], the candidates prev are added in order of increasing prev (we can add them as we compute or after computing previous layer).

# Since slopes are added in decreasing order (because S increasing => m=-2S decreasing), and queries are in increasing order (S[i] increasing), this is perfect for Convex Hull Trick with deque (lower hull).

# We can maintain a deque of candidate lines, adding lines with decreasing slopes, querying with increasing x.

# This is standard CHT (Convex Hull Optimization).

# For the odd transitions, as said, it's just prefix min of the previous dp values.

# Now let's define the layers.

# We will use two arrays prev_dp and curr_dp, but since we have 2K layers, memory is ok but to save space we can iterate over the number of picked.

# But K=3000, 2K=6000, N=10000, dp[10001][6001] would be 60M * 8bytes ~ 480MB which is too much probably.

# We cannot store all layers.

# We must use two arrays: previous layer and current layer.

# Yes, standard.

# So we will have prev_dp[0..N] , curr_dp[0..N]

# But for each t from 1 to 2*K, we compute the dp for that t.

# Initialize: for t=0 (no dolls chosen), we can think dp[i][0] = 0 for all i, but since we require the last chosen, it's better to think dp[i][t] defined only when we choose i as the t-th.

# So let’s set:

# For t=1 (first A): there is no previous, cost=0, so for each possible i, dp[i][1] = 0, because choosing any doll as first A has cost 0.

# Then we need to process t from 2 to 2K.

# Also at the end we take min over allowable i of dp[i][2*K]

# Yes.

# Now, since we only need previous t's dp, we can loop over t.

# But for the odd t, we need prefix min.

# Let's implement it carefully.

# Let me outline the code:

import sys
# ... 

S = sorted(sizes)
M = N - K   # the max index for the last B is N-K-1, so 0-based <= N-K-1

# we will create dp[0..N-1], but only up to M for the last.

# Since for intermediate, the prev can be up to current i-1, and for last we restrict.

INF = 10**18
# we will use two lists

# At t=0, no choice, cost 0, but no last doll.

# For t = 1 (picking first A): for every possible position i=0 to N-1, if we pick it as first, cost = 0
# But later ones might not leave enough for C's but we will filter at the end.

prev_dp = [INF] * N
for i in range(N):
    prev_dp[i] = 0   # t=1, cost 0

current_t = 1

for t in range(2, 2*K + 1):
    curr_dp = [INF] * N
    if t % 2 == 0:  # even t: picking a B, add cost
        # we need to use CHT
        # each possible prev offers a line: slope = -2 * S[prev], intercept = prev_dp[prev] + S[prev]**2
        # query at x = S[i], get min, then add S[i]**2
        
        from collections import deque
        hull = deque()
        
        # we will add prev in order from small to large, and query in order
        j = 0  # pointer for prev
        for i in range(1, N):  # i must > prev, so start from 1
            # add all prev < i that are valid for t-1
            while j < i:
                # add the line for prev = j
                if prev_dp[j] != INF:
                    slope = -2 * S[j]
                    inter = prev_dp[j] + S[j] * S[j]
                    # add line slope*x + inter
                    # since slopes added decreasing, we maintain lower hull
                    def bad(l1, l2, l3):
                        # check if line l2 is bad between l1 and l3
                        # (inter3 - inter1)/(slope1 - slope3) <= (inter2 - inter1)/(slope1 - slope2) but careful with signs
                        # since we use cross
                        return (inter[l3] - inter[l1]) * (slope[l1] - slope[l2]) <= (inter[l2] - inter[l1]) * (slope[l1] - slope[l3])
                    
                    # better to define lines as list of (slope, inter, idx)
                    # but to avoid global, let's use a function
                    
                    # standard CHT for lines
                    # since slope decreasing, query x increasing, we pop from back when adding, pop from front when querying.
                    
                    # let's define a function to check if we need to pop
                    while len(hull) >= 2:
                        l1 = hull[-2]
                        l2 = hull[-1]
                        l3 = j
                        # (y3 - y1)/(x1 - x3) <= (y2 - y1)/(x1 - x2) but with x=slope, y=inter
                        if (inter[l3] - inter[l1]) * (slope[l1] - slope[l2]) <= (inter[l2] - inter[l1]) * (slope[l1] - slope[l3]):
                            hull.pop()
                        else:
                            break
                    hull.append(j)
                j += 1
            
            # now query for this i
            if not hull:
                curr_dp[i] = INF
            else:
                x = S[i]
                # remove from front if not optimal
                while len(hull) >= 2:
                    l1 = hull[0]
                    l2 = hull[1]
                    if (prev_dp[l1] + S[l1]**2 - 2*S[l1]*x) >= (prev_dp[l2] + S[l2]**2 - 2*S[l2]*x):
                        hull.popleft()
                    else:
                        break
                best_prev = hull[0]
                best_val = prev_dp[best_prev] + (S[best_prev] - S[i]) ** 2
                curr_dp[i] = best_val
    else:  # t odd: picking an A, no cost added, curr_dp[i] = min of prev_dp[0..i-1]
        running_min = INF
        for i in range(N):
            if i > 0:
                running_min = min(running_min, prev_dp[i-1])
            curr_dp[i] = running_min
    
    prev_dp = curr_dp
    current_t = t

# now prev_dp contains the dp for t=2K
# we need the min among all i where there are at least K dolls after i, i.e. N - i - 1 >= K => i <= N - K - 1
ans = INF
max_i_for_last = N - K - 1
for i in range(N):
    if i <= max_i_for_last:
        ans = min(ans, prev_dp[i])

print(ans if ans != INF else 0)  # though should not be inf

This is the structure but the CHT part has bugs in the code (variables not defined properly like inter and slope as lists).

I need to clean it up and make the CHT correct.

Let me rewrite the code properly.

First, for the even case, we need to process i from small to large, adding the possible prev =0,1,2,... as i increases.

Yes.

Here is the corrected version:

We need to define the hull with indices.

Let me write the full code.

Since slopes are negative and decreasing, and x positive increasing, it should work.

Let’s implement a standard CHT class or inline.

To make it fast in python, we must be careful.

Since N=1e4, K=3e3, number of layers is 6000, each layer is O(N) for odd, for even the CHT is amortized O(N) per layer because each line is added and removed at most once.

So total time is O(K * N) which is 3000*10000 = 3e7 operations, perfect.

Yes!

Now let's write the code correctly.

For t=1, prev_dp[i] = 0 for all i (meaning if we pick i as the first A).

For t=2 (even), we pick B, so for each possible i, min over prev < i of 0 + (S[prev]-S[i])**2

Yes.

Then for t=3 (odd), curr_dp[i] = min over all prev_dp[0 to i-1], which is min of all possible B1 positions before i.

Yes, correct.

Perfect.

Now, one issue: for the C phase, we don't pick any more for cost, but we need to ensure there are enough dolls after the last B for the K C's.

Since we have already restricted the last i <= N-K-1, and since we pick exactly 2K for pairs, there will be N - (number of pair dolls chosen before i +1) but since we don't care which ones after are chosen as long as there are K available after i, yes it's fine. We don't need to "pick" them in the DP, just check the count is enough.

Yes, because any K after i can be chosen as the C's.

If there are duplicates it still works because >= .

Now let's handle if 2K > N-K i.e. if 3K > N but constraint says 3K <=N so N-K-1 >= 2K-1 probably ok.

Constraint is 3K <= N so N >= 3K, so N - K >= 2K, so N-K-1 >= 2K-1, so there are enough positions for the 2K-th doll.

Good.

Now, implement the CHT carefully.

For the even t, the function to decide if three lines, the middle one is not needed.

Since slope added in decreasing order, we maintain the deque for lower envelope.

The condition for popping when adding a new line:

For lines y = m x + b, with m decreasing.

To see if line2 is not needed between line1 and line3:

We compute the intersection point.

The intersection of line1 and line3 is at x where m1x + b1 = m3x + b3 => x = (b3-b1)/(m1-m3)

Similarly for line1 and line2.

If intersection(line1,line3) <= intersection(line1,line2), then line2 is useless.

Since m1 > m2 > m3 (but in our case m are negative, but m1 > m2 since decreasing: wait m = -2*S, S increasing so m decreasing: m1 > m2 > m3 ? No:

S[prev] increasing as prev increases, m = -2*S[prev] is decreasing: so when we add later prev, slope is smaller (more negative).

So slopes are added in decreasing order. Good.

In the inequality, since denominators m1 - m3 >0 ? m1 > m3 since m1 is earlier, larger slope (less negative), m3 more negative so m1 > m3 yes (e.g. -2 > -10).

No: -2 > -10 is true, yes m1 > m3.

To avoid floating point we use cross multiplication.

The condition to pop line2 when adding line3 is:

(intersection l1 l3 <= intersection l1 l2)

(b3 - b1)/(m1 - m3) <= (b2 - b1)/(m1 - m2)

Since (m1 - m3) > 0 and (m1 - m2)>0, we can multiply both sides by them (positive):

(b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

Yes.

So in code, if (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3) then pop line2.

Yes.

For querying, since x increasing, we pop from front if the first two lines, the first is worse than second at current x.

That is if m1*x + b1 >= m2*x + b2 then pop first.

Which is (b2 - b1) <= (m1 - m2) * x

Yes.

Now let's code it.

Also to avoid large numbers, since S<=1e5, diff<=1e5, square <=1e10, K=3000, total cost <= 3000*1e10 = 3e13, so use 64-bit int, in python int is fine.

Let's write the code.

First the imports and reading.

```python
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
K = int(data[index])
index += 1
sizes = [int(data[index + i]) for i in range(N)]
sizes.sort()

if K == 0:
    print(0)
    sys.exit()

S = sizes
INF = 10**18

# dp[i]: min cost to reach this as the last pick for current t
prev_dp = [0] * N  # for t = 1, cost 0 for any starting A

for num in range(2, 2 * K + 1):
    curr_dp = [INF] * N
    if num % 2 == 1:
        # odd: picking A, cost = min of all previous dp values before i
        min_val = INF
        for i in range(N):
            curr_dp[i] = min_val
            if prev_dp[i] < min_val:
                min_val = prev_dp[i]
    else:
        # even: picking B, use CHT
        hull = deque()
        # we will iterate i, add all possible prev < i
        for i in range(N):
            # first, add all prev that can be added before querying i. But since we add sequentially, add prev = i if possible? No.
            # Actually since prev < i, we should add prev = i after querying? No.
            # We need to add the lines in order of increasing prev.
            # So we need a separate pointer or add before the loop for that i.
        
        # Better: use a pointer for which lines have been added
        add_idx = 0
        hull = deque()
        for i in range(N):
            # add all prev < i that have finite cost
            while add_idx < i:
                if prev_dp[add_idx] < INF:
                    m = -2 * S[add_idx]
                    b = prev_dp[add_idx] + S[add_idx] * S[add_idx]
                    # add line m, b, with idx add_idx
                    # remove previous lines that are dominated
                    while len(hull) >= 2:
                        l1 = hull[-2]
                        l2 = hull[-1]
                        m1 = -2 * S[l1]
                        b1 = prev_dp[l1] + S[l1]*S[l1]
                        m2 = -2 * S[l2]
                        b2 = prev_dp[l2] + S[l2]*S[l2]
                        m3 = m
                        b3 = b
                        if (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3):
                            hull.pop()
                        else:
                            break
                    hull.append(add_idx)
                add_idx += 1
            
            # now query the best for this i
            if not hull:
                curr_dp[i] = INF
            else:
                # remove from front lines that are not optimal
                x = S[i]
                while len(hull) >= 2:
                    l1 = hull[0]
                    l2 = hull[1]
                    m1 = -2 * S[l1]
                    b1 = prev_dp[l1] + S[l1] * S[l1]
                    m2 = -2 * S[l2]
                    b2 = prev_dp[l2] + S[l2] * S[l2]
                    if m1 * x + b1 >= m2 * x + b2:
                        hull.popleft()
                    else:
                        break
                best = hull[0]
                cost = prev_dp[best] + (S[best] - S[i]) * (S[best] - S[i])
                curr_dp[i] = cost
    prev_dp = curr_dp

# now prev_dp has costs for 2K picks, with last pick at i
ans = INF
max_last_idx = N - K - 1
for i in range(max_last_idx + 1):
    if prev_dp[i] < ans:
        ans = prev_dp[i]

print(ans)
```

This should work.

Let me test it mentally on the sample.

Sample 1: N=7, K=2, S = [1,5,7,8,11,15,16]

2K=4, N-K-1 = 7-2-1=4, so last B can be at index 4 (value 11)

So max i=4.

t=1: prev_dp = [0,0,0,0,0,0,0] for all positions 0 to 6.

Now num=2 (even, first B):

For i=0: no prev <0, curr[0]=INF

For i=1: add_idx goes to 0, add prev=0, hull=[0], then query at S[1]=5, cost = 0 + (1-5)**2 = 16, curr[1]=16

For i=2: add prev=1, add line for prev=1, S[1]=5, m=-10, b=0+25=25

Check with previous.

Then query at S[2]=7, will compute min of (1-7)^2=36 or (5-7)^2=4, so should take 4.

Yes.

Similarly it will compute for each i the min (S[p]-S[i])**2 for p<i.

Then curr_dp[2] = min over p<2 of (S[p]-7)**2 = min( (1-7)^2=36, (5-7)^2=4 ) =4

curr_dp[3] = min( (1-8)^2=49, (5-8)^2=9, (7-8)^2=1 ) =1

curr_dp[4] = min(..., (8-11)^2=9, (7-11)^2=16 ) the min will be 9 (from 8? but 8 is index 3)

Yes.

Then prev_dp becomes this for t=2: index0=INF,1=16,2=4,3=1,4=9,5=min previous with 15, smallest is (8-15)^2=49, but actually min is from closest like (11-15)^2 but 11 is index4 not yet added for t=2? For i=5, add_idx up to 4, so prev=0to4, costs from t=1 are all 0, so min (S[p]-15)**2 for p<5, the closest is p=4 S=11, (11-15)^2=16.

Yes.

Now next num=3, odd: picking second A.

So running min.

curr_dp[0] = INF (min_val=INF)

Then for i=0, curr[0]=INF, then min_val = min(INF, prev_dp[0]=INF)

for i=1, curr[1] = min_val which is INF, then update min_val = min(INF, prev_dp[1]=16) =16

for i=2, curr[2] =16, then min_val = min(16, prev[2]=4)=4

for i=3, curr[3]=4, min_val=min(4,1)=1

for i=4, curr[4]=1, min_val=min(1,9)=1

for i=5, curr[5]=1, etc.

So curr_dp roughly [INF, INF, 16, 4, 1, 1, 1]

This represents the min cost after picking 3 dolls: A1 B1 A2, cost is the cost of first pair only.

Yes, for example at i=4 (A2=11), the min cost is 1, which likely came from picking A1=7(index2), B1=8(index3) cost1, then A2=11.

Yes.

Now last num=4 even: picking second B.

Now we use CHT again on this prev_dp (which is t=3).

So for i=1, probably INF.

We expect at i=4 (11), what cost?

When picking B=11 at index4, the A would be the prev picked as A2, so the cost added is (A2 - 11)^2, and the previous cost.

From above, if A2 was at index 3 (8), then add (8-11)^2=9, previous cost was 1 (from first pair 7-8? In previous, when curr[3] for t=3 was 4? Let's not simulate fully.

But in optimal, one possible is first pair 5 and 7 cost 4, then A2=8, B2=11 cost 9, total 13.

Path: A1=index1(5), B1=index2(7) cost4, A2=index3(8), B2=index4(11) cost9, total 13.

In t=3, when i=3 (A2=8), the running min was 4, yes (from the first pair cost 4).

Then when t=4, i=4, prev=3, add (8-11)^2=9, total 4+9=13.

Is there better? For example if there is smaller.

Another possible A2=7 index2 for t=3 curr[2]=16, then + (7-11)^2=16, total 32 worse.

Or A2=5? But index1 for t=3 was INF.

So at i=4, should get 13.

Then since max_last_idx = 7-2-1=4, so i<=4, ans = min including this 13.

Is there smaller at i=4 or less? For i=3 as last B, that would be 4th pick at index3=8, then we would need K=2 C's after index3, N-i-1=7-3-1=3 >=2 yes but i=3 <=4.

What cost? To have 4 picks all <=3, meaning using first 4 dolls: 1,5,7,8.

Then pairs (1,5) and (7,8), costs (1-5)^2=16 + (7-8)^2=1 =17.

In DP, when i=3 for t=4, the prev A would be some A2 chosen before 3, with its cost.

From t=3, curr_dp[2] =16 (which is A2 at 7, with previous pair cost 16? From first pair (1,5) cost16, then A2=7.

Then add (7-8)^2=1, total 17. Yes.

So DP gets 17 and 13, takes min 13. Perfect.

For the second sample, many 1s and 2s, it should find cost 0 by pairing equals.

Yes.

If all equal, cost 0.

Great.

Now, in the code above, there is a small bug: in the odd case, the running min should be updated after setting curr_dp? In my code:

min_val = INF

for i in range(N):

    curr_dp[i] = min_val

    if prev_dp[i] < min_val:   # this updates using the prev_dp[i], but for next ones

        min_val = prev_dp[i]

For odd t, curr_dp[i] should be the min of prev_dp[0] to prev_dp[i-1].

So initially before i=0, min should be INF (no previous).

For i=0, no possible prev, curr[0] = INF

Then we should update the running_min with prev_dp[0] for future i.

So the code has:

min_val = INF

for i in range(N):

    curr_dp[i] = min_val   # for i=0: INF good

    if i < N and prev_dp[i] < min_val:  # update for next

        min_val = prev_dp[i]

No, it should update after assigning.

In the code I wrote earlier in the if num%2==1:

        min_val = INF

        for i in range(N):

            curr_dp[i] = min_val

            if prev_dp[i] < min_val:

                min_val = prev_dp[i]

For i=0: curr[0] = INF, then if prev_dp[0] < INF, min_val = prev_dp[0]

For i=1: curr[1] = prev_dp[0]  (good, min of prev[0..0])

then update min_val = min( that, prev_dp[1])

For i=2: curr[2] = min of prev[0],prev[1]  yes.

Perfect. It works.

In the even part, the code looks correct.

In the even loop, for i in range(N):

    while add_idx < i:

        ... add add_idx ...

        add_idx +=1

    then query for i.

For i=0, add_idx<0? no, hull empty, curr[0]=INF good.

For i=1, add while add_idx<1 i.e. add 0, then query. Good.

Also in the bad line check:

if (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3):

    hull.pop()

Yes, as derived earlier.

In the query:

if m1 * x + b1 >= m2 * x + b2:

    popleft

Yes, I wrote it with the variables.

In the code I have m1 = -2 * S[l1] etc. Yes.

One issue: since we compute b = prev_dp[add_idx] + S[add_idx]**2 every time, but it's ok.

To prevent overflow, but python int is arbitrary precision, though for speed with 3e7 it should be fine as N*K=3e7, but with constants in loops maybe around 1-2s but acceptable for most judges.

To make it faster we can precompute S2 = [s*s for s in S]

Yes.

Let's add that.

Also if K=0 but constraint K>=1? No, K>=1 since 1<=K but to be safe.

Constraint is 1 <= K <=3000.

No, looking back: 1 ≤ K ≤ 3 000 yes.

Good.

In the first odd transition it works.

I think this solves the problem.

One more: in the odd case, if all previous are INF, it stays INF.

At the end we take min up to max_last_idx.

If ans == INF: but shouldn't.

For the second test case:

8 2

2 1 2 2 2 1 2 2

Sorted: 1,1,2,2,2,2,2,2

Then it should find many ways with cost 0, by pairing 1-1, and 2-2.

Yes, when pairing two 1's cost 0, two 2's cost 0.

And N-K-1=8-2-1=5, plenty.

Yes.

Perfect.

So the code is ready.

In the CHT, when adding, we append the add_idx.

In the while len(hull)>=2 for adding, we use l1=hull[-2], l2=hull[-1], l3=add_idx, then compute m1,b1 for l1, etc.

In code I have:

m3 = m

b3 = b

But in the pasted code I used m = -2*S[add_idx], b= prev_dp[add_idx] + S[add_idx]*S[add_idx]

Yes.

I think it's correct.

To make it cleaner, we can precompute nothing more.

This is the solution. 

Since the instruction is to generate ONLY the code, here it is: 
```python
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
K = int(data[index])
index += 1
sizes = [int(data[index + i]) for i in range(N)]
sizes.sort()

S = sizes
INF = 10**18

prev_dp = [0] * N

for num in range(2, 2 * K + 1):
    curr_dp = [INF] * N
    if num % 2 == 1:
        min_val = INF
        for i in range(N):
            curr_dp[i] = min_val
            if prev_dp[i] < min_val:
                min_val = prev_dp[i]
    else:
        hull = deque()
        add_idx = 0
        for i in range(N):
            while add_idx < i:
                if prev_dp[add_idx] < INF:
                    m = -2 * S[add_idx]
                    b = prev_dp[add_idx] + S[add_idx] * S[add_idx]
                    while len(hull) >= 2:
                        l1 = hull[-2]
                        l2 = hull[-1]
                        m1 = -2 * S[l1]
                        b1 = prev_dp[l1] + S[l1] * S[l1]
                        m2 = -2 * S[l2]
                        b2 = prev_dp[l2] + S[l2] * S[l2]
                        m3 = m
                        b3 = b
                        if (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3):
                            hull.pop()
                        else:
                            break
                    hull.append(add_idx)
                add_idx += 1
            if hull:
                x = S[i]
                while len(hull) >= 2:
                    l1 = hull[0]
                    l2 = hull[1]
                    m1 = -2 * S[l1]
                    b1 = prev_dp[l1] + S[l1] * S[l1]
                    m2 = -2 * S[l2]
                    b2 = prev_dp[l2] + S[l2] * S[l2]
                    if m1 * x + b1 >= m2 * x + b2:
                        hull.popleft()
                    else:
                        break
                best = hull[0]
                cost = prev_dp[best] + (S[best] - S[i]) ** 2
                curr_dp[i] = cost
    prev_dp = curr_dp

ans = INF
max_last = N - K - 1
for i in range(max_last + 1):
    ans = min(ans, prev_dp[i])

print(ans)
