
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    F = float(data[1])
    X = list(map(int, data[2:2+N]))

    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + X[i]

    total = prefix[N]
    min_tax = float('inf')

    for k in range(N):
        current_sum = 0
        for i in range(N-1):
            left = (k - i) % N
            right = (k + i + 1) % N
            current_sum += X[right]
            remaining = total - current_sum
            tax = F * max(current_sum, remaining)
            if tax < min_tax:
                min_tax = tax
    print("{0:.2f}".format(min_tax))

if __name__ == "__main__":
    main()
