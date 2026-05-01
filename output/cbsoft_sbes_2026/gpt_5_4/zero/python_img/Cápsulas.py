import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, f = data[0], data[1]
    cycles = data[2:2+n]

    lo, hi = 0, 10**8
    while lo < hi:
        mid = (lo + hi) // 2
        total = 0
        for c in cycles:
            total += mid // c
            if total >= f:
                break
        if total >= f:
            hi = mid
        else:
            lo = mid + 1

    print(lo)

if __name__ == "__main__":
    main()
