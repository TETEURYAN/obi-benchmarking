N, T = map(int, input().split())

if T == 0:
    # Only 1 king and N-1 pawns
    # King can be in any of N positions
    print(N)

elif T == 1:
    # 1 king, 1 tower, N-2 pawns
    # No restriction between king and tower
    # Choose 2 positions from N for king and tower, then arrange them: N*(N-1)
    print(N * (N - 1))

else:
    # T == 2
    # 1 king, 2 towers, N-3 pawns
    # King must be between the two towers
    # Choose 3 positions from N for king and 2 towers
    # For each set of 3 positions, there's exactly 1 valid arrangement (towers at extremes, king in middle)
    # Number of ways = C(N, 3)
    from math import comb
    print(comb(N, 3))