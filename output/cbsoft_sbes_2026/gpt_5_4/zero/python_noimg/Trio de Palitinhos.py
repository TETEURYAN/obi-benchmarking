import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
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
