import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    nxt = {}
    for _ in range(n):
        e, c, d = input().split()
        nxt[int(e)] = (c, int(d))
    cur = 0
    ans = []
    for _ in range(n):
        c, cur = nxt[cur]
        ans.append(c)
    sys.stdout.write(''.join(ans))

if __name__ == "__main__":
    main()
