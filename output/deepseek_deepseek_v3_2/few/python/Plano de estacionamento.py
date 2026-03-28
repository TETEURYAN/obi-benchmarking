import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    V = [int(next(it)) for _ in range(M)]

    # Binary search on the answer
    def can_serve(k):
        # We need to check if we can serve first k customers
        # Greedy: assign each customer to the largest available spot <= V[i]
        # Use a min-heap of available spots? Actually we can simulate with a sorted list.
        # But N, M up to 100000 -> O(N log N) is fine.
        # We'll use a Fenwick Tree (Binary Indexed Tree) to track available spots
        # and binary search for the largest available <= V[i].
        # However, simpler: sort the first k V's, then assign smallest available spot to each.
        # This is a classic "matching" problem: we have k customers with max spot V[i],
        # we need to assign distinct spots from 1..N.
        # Greedy: sort V's, iterate, keep a pointer to next available spot.
        # If next_available <= V[i], assign it, else fail.
        sorted_V = sorted(V[:k])
        next_spot = 1
        for v in sorted_V:
            if next_spot <= v:
                next_spot += 1
            else:
                return False
        return True

    lo, hi = 0, M
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_serve(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)

if __name__ == "__main__":
    main()