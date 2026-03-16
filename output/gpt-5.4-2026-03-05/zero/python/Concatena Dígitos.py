import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    d = data[2:2+n]

    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + d[i]

    out = []
    idx = 2 + n
    for _ in range(q):
        l = data[idx]
        r = data[idx + 1]
        idx += 2

        m = r - l + 1
        if m <= 1:
            out.append("0")
            continue

        s = pref[r] - pref[l - 1]
        ans = 11 * (m - 1) * s
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
