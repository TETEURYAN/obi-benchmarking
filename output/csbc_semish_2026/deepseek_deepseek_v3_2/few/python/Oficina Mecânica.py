import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    T = [int(next(it)) for _ in range(N)]
    F = [int(next(it)) for _ in range(M)]

    T.sort(reverse=True)
    F.sort()

    if M > N:
        F = F[:N]
        M = N

    total_wait = 0
    prefix_sum = 0
    idx = 0

    for i in range(M):
        group_size = (N - i + M - 1) // M
        for _ in range(group_size):
            total_wait += prefix_sum
            prefix_sum += T[idx] * F[i]
            idx += 1

    print(total_wait)

if __name__ == "__main__":
    main()