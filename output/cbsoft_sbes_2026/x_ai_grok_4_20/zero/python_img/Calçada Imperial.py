
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
seq = [int(x) for x in data[1:]]

if N == 0:
    print(0)
    sys.exit()

# Find all unique values
vals = sorted(list(set(seq)))

# Case 1: single number
ans = 1
for v in vals:
    cnt = 0
    for x in seq:
        if x == v:
            cnt += 1
    ans = max(ans, cnt)

# Case 2: two distinct numbers a < b
for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        a = vals[i]
        b = vals[j]
        
        # Build sequence of only a and b, mapping to 0 and 1
        s = []
        for x in seq:
            if x == a:
                s.append(0)
            elif x == b:
                s.append(1)
        
        if not s:
            continue
        
        # DP: max length ending with 0 or 1, with last value
        # dp[i][last][cnt] but since N=500 we use O(N)
        # We track the maximum length for subsequences using only these two
        # with no two identical consecutive in the chosen subsequence
        
        # We can use a simple DP for this pair
        dp0 = 0  # max len ending with a (0)
        dp1 = 0  # max len ending with b (1)
        
        for val in s:
            if val == 0:
                # can append to previous 1 or start new
                new_dp0 = max(dp0, dp1 + 1, 1)
                dp0 = new_dp0
            else:
                new_dp1 = max(dp1, dp0 + 1, 1)
                dp1 = new_dp1
        
        best_for_pair = max(dp0, dp1)
        ans = max(ans, best_for_pair)

print(ans)
