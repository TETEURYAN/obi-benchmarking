
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 0:
    print(0)
    sys.exit()

ans = 0
for i in range(N):
    if A[i] > 0:
        ans = 1
        break
if ans == 0:
    print(0)
    sys.exit()

max_val = 0
for i in range(N):
    if A[i] == 0:
        continue
    max_val = max(max_val, 1)

from collections import defaultdict
diag = defaultdict(int)

for j in range(N):
    if A[j] == 0:
        continue
    for a in range(1, A[j] + 1):
        d = a - j
        diag[d] = max(diag[d], a)

for cnt in diag.values():
    max_val = max(max_val, cnt)

print(max_val)
``` 

Wait, this is wrong. Let me think again.

The condition is: sound from apartment i in building j is heard in apartment a in building b (b < j) if a - i == j - b, and a <= A[b], and implicitly a > i? The problem says "em um andar mais alto", so a > i.

In the description: "em um andar mais alto" which means higher floor, so a > i.

And "na mesma diagonal".

The relation: a - i = j - b, which is a + b = i + j.

So constant sum a + b.

No: a - i = j - b ⇒ a + b = i + j.

Yes.

And b < j, a > i (since higher floor), and a <= A[b].

The example: if emitted at apartment 2 of building 4 (i=2, j=4), then heard at apartment 4 of building 2 (a=4, b=2).

Check: 4 - 2 = 4 - 2 ⇒ 2=2, yes. And 4 > 2, 2 < 4.

Not heard at 1 of building 3: a=1, b=3. 1-2 = 4-3 ⇒ -1=1? No.

And apartment 4 of building 6: b=6 >4, not to the left.

The task is, for each possible starting apartment (i,j) with 1<=i<=A[j], count how many apartments hear it, including itself. That is, number of (a,b) with b<=j, such that if b==j then a==i, else b<j, a<=A[b], a>i, and a-i == j-b.

And find the maximum such count over all possible starting positions.

Constraints: N<=3e5, A_i<=1e9, so we cannot simulate per apartment.

We need an efficient way.

For a fixed starting (i, j), the positions that hear it are all (a, b) where b < j, a = i + (j - b), a > i (which is automatic since j>b), and a <= A[b].

So a = i + j - b, and 1 <= a <= A[b], but since a = i+j-b > i >=1, ok.

But a must be at least 1, but since i>=1, j-b>=1, a>=2.

For each possible b < j, if i + j - b <= A[b], then it is heard.

So the count is 1 + number of b < j with A[b] >= i + j - b.

We need max over all possible i,j (with i<=A[j]) of that value.

This seems tricky.

Let k = j - b, then k =1 to j-1, b= j-k, and a = i + k, and we need a <= A[b] i.e. i+k <= A[j-k].

For fixed starting j and i, count = 1 + number of k>=1, b=j-k>=0, such that i+k <= A[j-k].

To maximize this over i<=A[j].

Notice that for a fixed starting building j, and for each possible "diagonal distance" or something.

The apartments that can hear the sound from (i,j) are exactly the apartments on the diagonal going up-left from (i,j).

The chain is determined by the diagonal.

The diagonal is defined by a + b = constant? Since a + b = i + j, yes, all points with same s = a + b = i+j, and b <=j, a = s - b <= A[b], and for the starting one a=i, b=j.

But the "hearing" is only to the left and higher, so from the starting point, all points to the left on the same diagonal that exist (a <=A[b]).

But the count includes all such points to the left plus itself.

But is it only direct? The problem says "é ouvido em todos os apartamentos que estão em algum prédio à esquerda, em um andar mais alto e que estejam na mesma diagonal que o apartamento inicial."

It seems it's direct: all that satisfy the condition with the initial one.

It's not propagating further; it's all on the same diagonal to the left and above.

Yes.

So for a fixed diagonal s = i + j, the possible apartments on that diagonal are all b where max(1, s - A[b]) something wait.

For a fixed s = i + j, the possible b's for which there is an apartment a=s-b with 1<=a<=A[b], i.e. s - A[b] <= b <= s-1.

But anyway.

For a fixed s, the buildings b where the diagonal s intersects the building b, i.e. if A[b] >= s - b, and s-b >=1 i.e. b <= s-1.

Then the apartments on that diagonal are at positions b where b < s and A[b] >= s-b.

These positions can be ordered by b increasing or decreasing.

Since left means smaller b.

If I fix the diagonal s, then all valid b's that have A[b] >= s-b, let's say the valid positions on this diagonal are b1 < b2 < ... < bm, with corresponding a_k = s - b_k.

Then, if I emit from the rightmost one, say from bm, then all the previous ones b1 to b{m-1} are to the left, higher (since smaller b, a =s-b larger), so all of them will hear it, plus itself, so count = m.

If I emit from b{m-1}, then only those to the left of it, i.e. 1 to m-2, count=m-1, which is smaller.

So, for each diagonal, the maximum count achievable on that diagonal is exactly the number of buildings that the diagonal intersects, i.e. the maximum chain length on that diagonal.

And since when you emit from the rightmost intersection on that diagonal, you reach all to the left on same diagonal.

And different diagonals are independent.

The overall answer is the maximum, over all possible diagonals s, of the number of buildings b where the diagonal s intersects building b, i.e. 1 <= s-b <= A[b].

That is, max over s of |{ b | 1 <= s-b <= A[b] }|  (and b from 1 to N, assuming 1-indexed).

Yes!

And since the starting apartment must exist, s-b <=A[b] and >=1.

Also if a building has A[b]=0, it doesn't intersect any.

This matches the sample.

First sample: N=9, A = [8,7,0,2,4,5,0,0,3] (0-index or 1? buildings 1 to 9: A1=8,A2=7,A3=0,A4=2,A5=4,A6=5,A7=0,A8=0,A9=3)

In the figure it's probably showing some.

The output is 4.

So some diagonal intersects 4 buildings.

Yes.

Second sample output 7.

Third: one building with 0, answer 0.

If all zero, 0. If one building with some apartments, then max is 1, since no left.

Perfect.

So the problem reduces to: find the maximum number of buildings intersected by any single diagonal s, where a diagonal s intersects building b (1<=b<=N) if s-b >=1 and s-b <= A[b], i.e. b+1 <= s <= b + A[b].

For each building b (let's 0-index or 1-index, I'll use 0-index: buildings 0 to N-1, A[0..N-1])

For building j (0-based), it intersects diagonals s where s = a + j for a=1 to A[j], so s from 1+j to A[j]+j.

Yes, s \in [j+1, j + A[j]]

We need, for each possible s, how many j have s in [j+1, j+A[j]], i.e. j+1 <= s <= j + A[j], i.e. s - A[j] <= j <= s-1.

But since N=3e5, A[j]<=1e9, s can be up to 3e5 + 1e9 ~ 1e9, cannot array.

We need the maximum frequency over all s of how many intervals [L_j, R_j] cover s, where for each j, L_j = j+1, R_j = j + A[j].

Yes! Classic problem: given N intervals [L_j, R_j] on the number line (though up to 1e9+3e5), find the maximum number of intervals covering any point.

Since N=3e5, we use sweep line.

We can collect all left and right endpoints, sort events: +1 at L_j, -1 at R_j+1.

Then sort all events by position, scan left to right, keep counter, track max.

But since coordinates up to 1e9 + 3e5 < 2^30 *2 ok, but in python sorting 6e5 events is acceptable, since time limit usually 2s, python can sort 6e5 easily.

N=3e5, 2 events per interval, 6e5, sort is fine.

Need to be careful with large coordinates, but in python int is fine.

If A[j]=0, then L=j+1 > j+0=R, so empty interval, we can skip them.

Yes.

So, plan:

- Read N, A list of size N (0-based)

- Create list of events: for each j in 0..N-1:

  if A[j] > 0:

    L = j + 1

    R = j + A[j]

    events.append( (L, 1) )   # start

    events.append( (R+1, -1) ) # end

- Sort events by position asc, if tie, process +1 before -1? Actually since at exact point, if start at s, it covers s, if end at s means R+1=s so R=s-1, does not cover s.

So when sorting, if same position, we should process +1 (starts) before -1 (ends), so that at the exact start point we count it.

In python, if we put (pos, delta), and delta=1 for start, -1 for end, since  -1 < 1, if we sort normally, at same pos, -1 comes before 1, which would be wrong: it would first subtract then add, so at that point we miss the starting ones? 

Suppose at position x, there is a start (L=x, +1), and an end (R+1=x so previous ended at x-1).

The end should not affect coverage at x, the start should include at x.

If we process -1 first, current count decreases first, then increases, so during that we might record a lower value, but if we track max after each addition, it depends.

To do correctly, we should process all events at same position together, but order: typically process starts before ends at the same point.

To make sort do that, we can use (pos, type, delta), where type=0 for start, type=1 for end, so starts come first.

Or since delta +1 and -1, we can sort by pos, then by delta descending, so +1 before -1.

Yes.

In python: events.sort(key=lambda x: (x[0], -x[1]))

Since for +1, -(+1)= -1, for -1, -(-1)=+1, so -1 < +1? No:

We want +1 to come before -1, so for same pos, the one with smaller second key first.

If I do key = (pos, -delta), then for delta=1, -1; for delta=-1, +1. So -1 < 1, thus +1 event comes before -1 event. Perfect.

Yes.

Then:

current = 0

max_count = 0

for pos, delta in events:

    current += delta

    if current > max_count:

        max_count = current

But if at same pos multiple, since we sorted starts first, current will first add all starts, then subtract ends, and we check after each, so after adding starts, before subtracting, we will see the high value, which is correct for that point.

Yes, perfect. Because the point pos is covered by the starting intervals, but not by the ones that ended at pos-1.

Yes.

If there is an end at pos (meaning R+1=pos, R=pos-1), it should not cover pos, so subtracting after we have recorded the max is good.

Yes.

Also, if A[j]=0 we skip.

If all zero, max_count remains 0, good.

Single building A[0]=5, then L=1, R=5, events (1,1), (6,-1), current goes to 1, max=1, good.

Now, about indexing: buildings from left to right, assume building 0 is leftmost? In problem, left is smaller index I think.

In problem: b < j means to the left, assuming smaller index is left.

In input: A1 A2 ... AN from left to right.

So if we index j from 0 to N-1 as left to right, then left has smaller j, so b < j yes.

And s = a + j , with j from 0, a>=1, s>=1.

If j from 1 to N, L=j+1? If j=1 leftmost, a=1,s=2; but doesn't matter as long as consistent.

In my 0-based: for j=0, s from 1 to A[0].

For j=1, s from 2 to 1+A[1], etc.

In the condition a - i = j - b, with j>b, since b left.

If j is 0-based, b < j numerical smaller is left, yes.

The difference j-b is positive integer.

Yes, it works.

Now, sample 1:

N=9, A=[8,7,0,2,4,5,0,0,3], j=0..8

For j=0, A=8, s=1 to 8

j=1,A=7,s=2 to 8

j=3,A=2,s=4 to 5

j=4,A=4,s=5 to 8

j=5,A=5,s=6 to 10

j=8,A=3,s=9 to 11

Let's see for s=5: which cover?

j=0:1-8 yes

j=1:2-8 yes

j=3:4-5 yes

j=4:5-8 yes

j=5:6-10 no

So 4 buildings: 0,1,3,4. Yes, count 4, matches sample.

Perfect.

Another s=8: j=0,1,4,5? j=5:6-10 yes, j=8 no. So also 4.

Yes.

Great.

For implementation, since pos up to 3e5 + 1e9 = about 1e9+3e5, python int fine.

Events list with 6e5 elements, each tuple (int, int), memory should be ok.

Time: sorting 6e5 log(6e5) ~ 20*6e5 ~1.2e7 operations, python fine.

We need to handle N=3e5, A_i=1e9, yes.

If A[j] very large, R = j + A[j] could be up to 3e5 + 1e9 ~ 1000000300000, which is 10^12, but python int handles arbitrary size, but for dict or whatever no, but here just in tuple, and comparison is fine.

In python3, comparing large ints is ok, though slightly slower but for 6e5 log n it's negligible.

To make it faster, perhaps we don't need to, it's acceptable.

I think this solves it.

One case: if two intervals touch, etc. But seems correct.

If A[j]=0, skipped, good.

If N=1, A=0, max=0.

If N=1, A=10, max=1.

Yes.

So now, write the code.

Must read from stdin, write to stdout.

Efficient.

In code, to make faster input, since N=3e5, use sys.stdin.read().

Y