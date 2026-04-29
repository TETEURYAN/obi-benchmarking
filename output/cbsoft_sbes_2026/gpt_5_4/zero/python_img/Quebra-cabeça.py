import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    nxt = {}
    chars = {}

    for _ in range(n):
        e, c, d = input().split()
        e = int(e)
        d = int(d)
        nxt[e] = d
        chars[e] = c

    cur = 0
    res = []
    for _ in range(n):
        res.append(chars[cur])
        cur = nxt[cur]

    sys.stdout.write(''.join(res))

if __name__ == "__main__":
    main()
