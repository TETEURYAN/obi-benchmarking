import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    pos = {}
    for i, h in enumerate(a):
        pos.setdefault(h, []).append(i)

    ans = 0
    for v in pos.values():
        ans += len(v) // 2

    print(ans)

if __name__ == "__main__":
    main()
