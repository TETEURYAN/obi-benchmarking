from math import comb

N, T = map(int, input().split())

if T == 0:
    # Only 1 king and N-1 pawns
    # King can be in any of N positions
    print(N)

elif T == 1:
    # 1 king, 1 tower, N-2 pawns
    # No restriction between king and tower
    # Choose 2 positions from N for king and tower, then arrange them: 2 ways
    # Total = N * (N-1)
    print(N * (N - 1))

else:
    # T == 2
    # 1 king, 2 towers, N-3 pawns
    # King must be between the two towers
    # Choose 3 positions from N for king and 2 towers
    # For each choice of 3 positions, king must be in the middle
    # So exactly 1 valid arrangement per combination of 3 positions
    # Total = C(N, 3)
    print(comb(N, 3))