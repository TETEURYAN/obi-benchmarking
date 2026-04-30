
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    piles = list(map(int, data[1:n+1]))

    total = sum(piles)
    k = n

    # The sum of the first k natural numbers is k*(k+1)//2
    # We need to find k such that k*(k+1)//2 <= total
    # and (k+1)*(k+2)//2 > total
    # But also, the sequence must be possible with the given piles

    # Binary search to find possible k
    low = 1
    high = 2 * 10**5  # A reasonable upper bound
    possible_k = -1
    for k in range(1, n + 1):
        required = k * (k + 1) // 2
        if required == total:
            possible_k = k
            break
        elif required > total:
            break

    if possible_k == -1:
        print(-1)
        return

    # Now, check if the sequence can be formed
    # The sequence should be [1, 2, ..., k-1, x], where x >= k
    # Or [1, 2, ..., k]
    # So the sum is k*(k+1)/2 = total
    # The sequence must be non-decreasing with differences of 1 between consecutive elements

    # The minimal sequence is 1, 2, ..., k
    # So the sum is k*(k+1)/2 = total
    # So the sequence must be exactly 1, 2, ..., k

    # Check if the multiset of piles can form 1, 2, ..., k
    # The sum must be k*(k+1)/2, which we already checked
    # The minimal element must be 1, and the maximal must be k
    # And all elements must be distinct and cover 1..k

    # But the problem allows for the sequence to be any permutation of 1..k
    # So we need to check if the multiset of piles is exactly {1, 2, ..., k}

    required_set = set(range(1, k + 1))
    if set(piles) == required_set:
        # The sequence is already a permutation of 1..k, so no moves needed
        print(0)
        return
    else:
        # We need to find the minimal moves to transform the piles into a permutation of 1..k
        # The minimal moves is the sum of the absolute differences between the sorted piles and the sorted target
        sorted_piles = sorted(piles)
        target = list(range(1, k + 1))
        moves = 0
        for i in range(k):
            moves += abs(sorted_piles[i] - target[i])
        print(moves)
        return

    print(-1)

if __name__ == "__main__":
    main()
