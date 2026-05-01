import sys

def main():
    input = sys.stdin.readline

    N, T = map(int, input().split())
    cima = list(map(int, input().split()))
    baixo = list(map(int, input().split()))

    diff = [0] * (N + 1)

    for _ in range(T):
        i, j = map(int, input().split())
        diff[i - 1] ^= 1
        diff[j] ^= 1

    cur = 0
    ans = [0] * N
    for k in range(N):
        cur ^= diff[k]
        ans[k] = baixo[k] if cur else cima[k]

    print(*ans)

if __name__ == "__main__":
    main()
