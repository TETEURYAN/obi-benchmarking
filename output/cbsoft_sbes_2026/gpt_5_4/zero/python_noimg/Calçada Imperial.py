import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    v = data[1:1+n]

    ans = 1

    values = sorted(set(v))
    m = len(values)

    for i in range(m):
        a = values[i]
        for j in range(i + 1, m):
            b = values[j]
            ca = 0
            cb = 0
            for x in v:
                if x == a:
                    ca += 1
                elif x == b:
                    cb += 1
            cur = 2 * min(ca, cb) + (1 if ca != cb else 0)
            if cur > ans:
                ans = cur

    print(ans)

if __name__ == "__main__":
    main()
