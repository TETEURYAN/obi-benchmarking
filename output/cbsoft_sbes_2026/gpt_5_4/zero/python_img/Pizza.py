import sys

def kadane_max(arr):
    best = 0
    cur = 0
    for x in arr:
        cur = max(0, cur + x)
        if cur > best:
            best = cur
    return best

def kadane_min(arr):
    best = 10**18
    cur = 0
    for x in arr:
        cur = min(x, cur + x)
        if cur < best:
            best = cur
    return best

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    total = sum(a)
    max_normal = kadane_max(a)
    min_sub = kadane_min(a)

    if min_sub == total:
        ans = max_normal
    else:
        ans = max(max_normal, total - min_sub)

    if ans < 0:
        ans = 0
    print(ans)

if __name__ == "__main__":
    main()
