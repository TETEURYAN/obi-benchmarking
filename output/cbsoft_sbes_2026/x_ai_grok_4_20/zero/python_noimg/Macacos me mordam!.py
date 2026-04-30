
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
trees = []
index = 1
for i in range(N):
    X = int(data[index])
    H = int(data[index + 1])
    trees.append((X, H))
    index += 2

trees.sort()
X = [0] * N
H = [0] * N
for i in range(N):
    X[i] = trees[i][0]
    H[i] = trees[i][1]

if N == 2:
    print(1)
    sys.exit()

dp = [0] * N
dp[0] = 0
dp[1] = 1

stack = [0]

for i in range(2, N):
    while stack and X[stack[-1]] + H[stack[-1]] < X[i] + H[i]:
        stack.pop()
    if stack and X[stack[-1]] + H[stack[-1]] >= X[i] + H[i]:
        dp[i] = dp[stack[-1]] + 1
    else:
        dp[i] = i
    stack.append(i)

ans = dp[N - 1]
j = N - 1
while j > 0:
    max_reach = X[j] - H[j]
    prev = -1
    for k in range(j - 1, -1, -1):
        if X[k] + H[k] >= X[j]:
            if X[k] >= max_reach:
                prev = k
                break
            else:
                max_reach = max(max_reach, X[k] - H[k])
    if prev == -1:
        ans = j
        break
    j = prev

print(ans)
