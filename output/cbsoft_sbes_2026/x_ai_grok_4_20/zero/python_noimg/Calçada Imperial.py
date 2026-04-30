
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
seq = [int(x) for x in data[1:]]

if N == 0:
    print(0)
    sys.exit()

# DP: dp[i][a][b][last] = max length using only a and b, ending with last (0=a,1=b)
# a and b from 0 to N (0 means not used)

INF = -1
dp = [[[[INF for _ in range(2)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

# Initialize for first position
v = seq[0]
dp[1][v][0][0] = 1
dp[1][0][v][1] = 1
dp[0][0][0][0] = 0  # dummy

ans = 1

for i in range(1, N):
    v = seq[i]
    for x in range(N+1):
        for y in range(N+1):
            for last in range(2):
                prev = dp[i][x][y][last]
                if prev == INF:
                    continue
                
                # skip current
                dp[i+1][x][y][last] = max(dp[i+1][x][y][last], prev)
                
                # take current
                if x == 0 and y == 0:
                    # first number
                    dp[i+1][v][0][0] = max(dp[i+1][v][0][0], prev + 1)
                    dp[i+1][0][v][1] = max(dp[i+1][0][v][1], prev + 1)
                elif x != 0 and y == 0:
                    # only one number so far: x
                    if v == x:
                        if last == 0:
                            continue  # cannot take same as last
                        dp[i+1][x][0][0] = max(dp[i+1][x][0][0], prev + 1)
                    else:
                        # introduce new number y = v
                        if last == 0:
                            dp[i+1][x][v][1] = max(dp[i+1][x][v][1], prev + 1)
                        else:
                            dp[i+1][x][v][0] = max(dp[i+1][x][v][0], prev + 1)
                else:
                    # two numbers: x and y
                    if v != x and v != y:
                        continue
                    if v == x:
                        if last == 0:
                            continue
                        dp[i+1][x][y][0] = max(dp[i+1][x][y][0], prev + 1)
                    else:  # v == y
                        if last == 1:
                            continue
                        dp[i+1][x][y][1] = max(dp[i+1][x][y][1], prev + 1)
                
                ans = max(ans, prev + 1)

# Also consider single number cases and empty
for x in range(N+1):
    for y in range(N+1):
        for last in range(2):
            if dp[N][x][y][last] != INF:
                ans = max(ans, dp[N][x][y][last])

print(ans)
