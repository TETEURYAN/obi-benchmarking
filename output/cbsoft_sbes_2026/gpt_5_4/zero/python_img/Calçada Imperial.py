import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    v = data[1:1+n]

    ans = 1

    for a in range(1, n + 1):
        for b in range(a, n + 1):
            last = 0
            cnt = 0
            for x in v:
                if x == a or x == b:
                    if x != last:
                        cnt += 1
                        last = x
            if cnt > ans:
                ans = cnt

    print(ans)

if __name__ == "__main__":
    main()