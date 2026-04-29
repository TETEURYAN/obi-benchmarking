import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    trees = [tuple(map(int, input().split())) for _ in range(n)]
    trees.sort()
    x = [p for p, h in trees]
    h = [hh for p, hh in trees]

    if n == 2:
        print(1)
        return

    left = [i - 1 for i in range(n)]
    right = [i + 1 for i in range(n)]

    stack = []
    for i in range(n):
        while len(stack) >= 2:
            j = stack[-1]
            k = stack[-2]
            if (h[j] - h[k]) * (x[i] - x[j]) <= (h[i] - h[j]) * (x[j] - x[k]):
                stack.pop()
            else:
                break
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while len(stack) >= 2:
            j = stack[-1]
            k = stack[-2]
            if (h[j] - h[k]) * (x[j] - x[i]) >= (h[i] - h[j]) * (x[k] - x[j]):
                stack.pop()
            else:
                break
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    INF = 10**18
    dp = [INF] * n
    dp[0] = 0

    q = [0]
    head = 0
    inq = [False] * n
    inq[0] = True

    while head < len(q):
        u = q[head]
        head += 1
        du = dp[u] + 1

        v = left[u]
        if v >= 0 and dp[v] > du:
            dp[v] = du
            if not inq[v]:
                inq[v] = True
                q.append(v)

        v = right[u]
        if v < n and dp[v] > du:
            dp[v] = du
            if not inq[v]:
                inq[v] = True
                q.append(v)

        inq[u] = False

    print(dp[n - 1])

if __name__ == "__main__":
    main()
