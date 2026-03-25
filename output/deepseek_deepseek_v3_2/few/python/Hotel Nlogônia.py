import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    D = int(next(it))
    W = int(next(it))
    prices = [int(next(it)) for _ in range(N)]

    # Prefix sums for fast range sum queries
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + prices[i]

    max_days = 0
    # Try every possible start of the free D‑day block
    for start_free in range(N - D + 1):
        end_free = start_free + D - 1
        # Extend left
        left = start_free
        while left > 0:
            cost_left = prefix[start_free] - prefix[left - 1]
            if cost_left <= W:
                left -= 1
            else:
                break
        # Extend right
        right = end_free
        while right < N - 1:
            cost_right = prefix[right + 2] - prefix[end_free + 1]
            if cost_right <= W:
                right += 1
            else:
                break
        total_days = (right - left + 1)
        if total_days > max_days:
            max_days = total_days

    print(max_days)

if __name__ == "__main__":
    main()