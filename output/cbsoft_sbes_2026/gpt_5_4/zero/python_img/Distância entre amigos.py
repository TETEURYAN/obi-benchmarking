import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1+n]

    best = 0
    pref = a[0] - 0

    for j in range(1, n):
        val = pref + a[j] + j
        if val > best:
            best = val
        cur = a[j] - j
        if cur > pref:
            pref = cur

    print(best)

if __name__ == "__main__":
    main()
