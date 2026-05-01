
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2

    A = list(map(int, data[idx:idx + N]))
    idx += N

    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]

    output = []
    for _ in range(Q):
        event = data[idx]
        if event == '0':
            K = int(data[idx + 1])
            P = int(data[idx + 2])
            idx += 3
            delta = P - A[K - 1]
            A[K - 1] = P
            for i in range(K, N + 1):
                prefix[i] += delta
        else:
            K = int(data[idx + 1])
            idx += 2
            output.append(str(prefix[K]))

    print('\n'.join(output))

if __name__ == "__main__":
    main()
