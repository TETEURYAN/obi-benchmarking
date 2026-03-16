import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    max_h = max(a)
    ans = 0

    for h in range(max_h):
        i = 0
        while i < n:
            if a[i] <= h:
                ans += 1
                while i < n and a[i] <= h:
                    i += 1
            else:
                i += 1

    print(ans)

if __name__ == "__main__":
    main()