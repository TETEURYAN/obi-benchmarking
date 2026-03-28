import sys, bisect

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    L = int(next(it))
    R = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    a.sort()
    def f(x):
        pos = bisect.bisect_left(a, x)
        res = 10**18
        if pos < n:
            res = min(res, abs(a[pos] - x))
        if pos > 0:
            res = min(res, abs(a[pos-1] - x))
        return res
    ans = max(f(L), f(R))
    for i in range(n-1):
        d = a[i+1] - a[i]
        cand = d // 2
        if cand > ans:
            low = a[i] + cand
            high = a[i+1] - cand
            if max(L, low) <= min(R, high):
                ans = cand
    print(ans)

if __name__ == "__main__":
    main()