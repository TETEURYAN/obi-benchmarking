
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])

    a = list(map(int, data[2:2+N]))
    b = list(map(int, data[2+N:2+2*N]))

    upper = [i for i in range(N) if a[i] == 1]
    lower = [i for i in range(N) if b[i] == 1]

    upper.sort()
    lower.sort()

    def compute_cost(positions):
        cost = 0
        median_pos = positions[K//2]
        for i in range(K):
            cost += abs(positions[i] - (median_pos - K//2 + i))
        return cost

    cost_upper = compute_cost(upper)
    cost_lower = compute_cost(lower)

    print(cost_upper + cost_lower)

if __name__ == "__main__":
    main()
