import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    A = data[1:1+n]

    best = 0
    freq = {}

    for j, aj in enumerate(A, start=1):
        if aj <= 0:
            continue
        L = j - aj
        R = j - 1
        freq[L] = freq.get(L, 0) + 1
        freq[R + 1] = freq.get(R + 1, 0) - 1

    cur = 0
    for x in sorted(freq):
        cur += freq[x]
        if cur > best:
            best = cur

    print(best)

if __name__ == "__main__":
    main()
