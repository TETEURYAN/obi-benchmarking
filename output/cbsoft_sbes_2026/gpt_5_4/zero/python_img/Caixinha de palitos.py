import sys

def c2(x):
    if x < 2:
        return 0
    return x * (x - 1) // 2

def main():
    data = sys.stdin.readline().split()
    N, M = map(int, data)

    S = N - 3
    U = M - 1

    total = c2(S + 2)
    bad1 = c2(S - U + 1) if S - U >= 0 else 0
    bad2 = c2(S - 2 * (U + 1) + 2) if S - 2 * (U + 1) >= 0 else 0
    bad3 = c2(S - 3 * (U + 1) + 3) if S - 3 * (U + 1) >= 0 else 0

    ans = total - 3 * bad1 + 3 * bad2 - bad3
    print(ans)

if __name__ == "__main__":
    main()
