
s = input().strip()
count = [0] * 26
for c in s:
    count[ord(c) - ord('A')] += 1
print(sum(count[i] for i in range(26) if count[i] > 0 or True) - sum(1 for i in range(26) if count[i] == 0) + sum(count))
```

Wait, let me reconsider.

A "cadeia crescente" means non-decreasing sequence of letters. So we want the longest subsequence where letters are non-decreasing.

The optimal strategy: for each letter we can include, we pick all occurrences of letters that form a non-decreasing sequence. The best approach is to pick all occurrences of some subset of letters that appear in non-decreasing order - meaning we pick a contiguous range of letters (or any subset where we take all occurrences).

Actually, we want to pick a set of letters {l1 ≤ l2 ≤ ... } and take all their occurrences from S in order. The result is non-decreasing iff we pick letters from a contiguous range (since all A's come before all B's requirement isn't needed - we just need the subsequence to be non-decreasing).

We can pick any subset of letters and take all their occurrences. The subsequence will be non-decreasing as long as... no, we need to be careful. If we pick A and C but not B, occurrences of A and C interleaved are fine as long as we take them in order - but a C before an A in the string would require us to skip that C or that A.

The simplest observation: if we pick a contiguous range of letters [a..b], we take ALL occurrences of each letter in that range, and arrange them in the order they appear in S. This gives a non-decreasing sequence because... no it doesn't necessarily.

Let me think again with the example: BANANAS, answer is 4 (ANNS or AANS etc.)

The key insight: we want longest non-decreasing subsequence. Since alphabet is only 26 letters, we can use DP with 26 states.

```python
s = input().strip()
dp = [0] * 26
for c in s:
    i = ord(c) - ord('A')
    dp[i] = max(dp[i] + 1, max(dp[:i+1]) + 0 if i > 0 else dp[i])
    best = max(dp[:i+1])
    dp[i] = best + (1 if dp[i] <= best else 0)
```

Let me just do it cleanly:

```python
s = input().strip()
dp = [0] * 26
for c in s:
    i = ord(c) - ord('A')
    best = max(dp[:i+1]) if i >= 0 else 0
    dp[i] = max(dp[i], best) + 1
    # but dp[i] already contains best from previous, so:
print(max(dp))
```

```python
s = input().strip()
dp = [0] * 26
for c in s:
    i = ord(c) - ord('A')
    # dp[i] = longest non-decreasing subseq ending with letter i
    # can extend any subseq ending with letter <= i
    best = max(dp[:i+1])
    dp[i] = best + 1
print(max(dp))
