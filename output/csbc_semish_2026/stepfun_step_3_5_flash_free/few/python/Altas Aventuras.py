import sys

def compute_max_floors(K, m, N):
    if K >= m:
        return (1 << m) - 1
    else:
        total = 0
        term = 1
        for i in range(1, K + 1):
            term = term * (m - i + 1) // i
            total += term
            if total >= N:
                return total
        return total

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    if K == 1:
        print(N)
        return
    if K >= 30:
        m = 1
        while (1 << m) - 1 < N:
            m += 1
        print(m)
        return
    low, high = 1, N
    while low < high:
        mid = (low + high) // 2
        if compute_max_floors(K, mid, N) >= N:
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    main()