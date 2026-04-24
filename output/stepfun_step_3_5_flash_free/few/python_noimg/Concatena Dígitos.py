import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    digits = [int(next(it)) for _ in range(n)]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + digits[i]
    out = []
    for _ in range(q):
        l = int(next(it))
        r = int(next(it))
        k = r - l + 1
        s = prefix[r] - prefix[l - 1]
        ans = 11 * (k - 1) * s
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()