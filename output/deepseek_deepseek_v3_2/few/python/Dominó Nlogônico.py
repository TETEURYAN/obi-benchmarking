import sys
sys.setrecursionlimit(1_000_000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    X = [int(next(it)) for _ in range(n)]
    H = [int(next(it)) for _ in range(n)]

    reach = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        limit = X[i] + H[i]
        cnt = 1
        while stack and X[stack[-1]] <= limit:
            j = stack.pop()
            cnt += reach[j]
            limit = max(limit, X[j] + H[j])
        reach[i] = cnt
        stack.append(i)

    print(' '.join(map(str, reach)))

if __name__ == "__main__":
    solve()