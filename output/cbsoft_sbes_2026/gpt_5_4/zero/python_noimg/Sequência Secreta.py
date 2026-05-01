import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    v = data[1:1+n]

    dp1 = 0
    dp2 = 0

    for x in v:
        if x == 1:
            dp1 = max(dp1, dp2 + 1)
        else:
            dp2 = max(dp2, dp1 + 1)

    print(max(dp1, dp2))

if __name__ == "__main__":
    main()
