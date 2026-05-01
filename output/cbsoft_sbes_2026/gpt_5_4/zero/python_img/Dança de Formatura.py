import sys

def main():
    input = sys.stdin.readline
    N, M, P = map(int, input().split())

    rows = list(range(1, N + 1))
    cols = list(range(1, M + 1))

    for _ in range(P):
        op, a, b = input().split()
        a = int(a) - 1
        b = int(b) - 1
        if op == 'L':
            rows[a], rows[b] = rows[b], rows[a]
        else:
            cols[a], cols[b] = cols[b], cols[a]

    out = []
    for i in range(N):
        base = (rows[i] - 1) * M
        line = [str(base + cols[j]) for j in range(M)]
        out.append(' '.join(line))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
