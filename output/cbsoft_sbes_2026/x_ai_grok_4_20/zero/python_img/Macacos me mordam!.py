
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

for i in range(1, N):
    while stack and X[stack[-1]] + H[stack[-1]] < X[i] + H[i]:
        stack.pop()
    if stack:
        dp[i] = dp[stack[-1]] + 1
    else:
        dp[i] = 1
    stack.append(i)

print(dp[N-1])
