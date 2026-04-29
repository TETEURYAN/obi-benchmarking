import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]
    a.sort()

    ans = 0
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            if a[i] + a[j] > a[k]:
                ans += j - i
                j -= 1
            else:
                i += 1

    print(ans)

if __name__ == "__main__":
    main()
