import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    M = int(next(it))
    N = int(next(it))
    saldo = [0] * (N + 1)
    total = 0
    for _ in range(M):
        X = int(next(it))
        V = int(next(it))
        Y = int(next(it))
        saldo[X] -= V
        saldo[Y] += V
        total += V
    soma_pos = 0
    for i in range(1, N + 1):
        if saldo[i] > 0:
            soma_pos += saldo[i]
    print('S' if total > soma_pos else 'N')
    print(soma_pos)

if __name__ == '__main__':
    main()