
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    X = list(map(int, data[1:n+1]))
    H = list(map(int, data[n+1:2*n+1]))

    dominoes = list(zip(X, H, range(n)))
    dominoes.sort()

    X_sorted = [x for x, _, _ in dominoes]
    H_sorted = [h for _, h, _ in dominoes]
    indices = [idx for _, _, idx in dominoes]

    res = [0] * n
    stack = []

    for i in range(n-1, -1, -1):
        x, h, original_idx = dominoes[i]
        right = x + h
        count = 1

        while stack and stack[-1][0] < right:
            _, cnt = stack.pop()
            count += cnt

        stack.append((right, count))
        res[original_idx] = count

    print(' '.join(map(str, res)))

if __name__ == '__main__':
    main()
