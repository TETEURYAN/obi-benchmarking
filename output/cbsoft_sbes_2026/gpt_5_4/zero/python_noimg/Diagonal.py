import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    A = data[1:1+n]

    freq = {}
    ans = 0

    for j, a in enumerate(A, start=1):
        if a > 0:
            key = a - j
            v = freq.get(key, 0) + 1
            freq[key] = v
            if v > ans:
                ans = v

    print(ans)

if __name__ == "__main__":
    main()
