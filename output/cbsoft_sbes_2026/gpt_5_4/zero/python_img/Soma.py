import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k = data[0], data[1]
    arr = data[2:2 + n]

    freq = {0: 1}
    s = 0
    ans = 0

    for x in arr:
        s += x
        ans += freq.get(s - k, 0)
        freq[s] = freq.get(s, 0) + 1

    print(ans)

if __name__ == "__main__":
    main()
