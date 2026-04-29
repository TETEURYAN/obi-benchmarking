import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    pos = {}
    for i, h in enumerate(a):
        pos.setdefault(h, []).append(i)

    ans = 0
    for v in pos.values():
        ans += len(v) // 2

    print(ans)

if __name__ == "__main__":
    main()
