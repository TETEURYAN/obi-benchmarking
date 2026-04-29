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
        if j < N:
            diff[j] ^= 1

    flip = 0
    res = []
    for k in range(N):
        flip ^= diff[k]
        res.append(str(baixo[k] if flip else cima[k]))

    sys.stdout.write(" ".join(res))

if __name__ == "__main__":
    main()
