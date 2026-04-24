
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    K = int(data[ptr])
    ptr += 1
    C = int(data[ptr])
    ptr += 1
    A = list(map(int, data[ptr:ptr+N]))

    total_sum = sum(A)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]

    min_covered = float('inf')
    for i in range(N - C + 1):
        current = prefix[i+C] - prefix[i]
        if current < min_covered:
            min_covered = current

    max_uncovered = total_sum - min_covered * K
    print(max_uncovered)

if __name__ == "__main__":
    main()
