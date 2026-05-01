N, M = map(int, input().split())

# Count triples (a, b, c) where:
# a + b + c = N
# 1 <= a, b, c <= M
# 
# Substitute x = a-1, y = b-1, z = c-1
# x + y + z = N - 3
# 0 <= x, y, z <= M - 1
#
# Using inclusion-exclusion:
# Total without upper bound: C(N-3+2, 2) = C(N-1, 2)
# Subtract cases where x > M-1 (i.e., x >= M):
#   Let x' = x - M, x' + y + z = N - 3 - M
#   Count: C(N-3-M+2, 2) = C(N-M-1, 2) if N-3-M >= 0
# By symmetry, same for y and z (multiply by 3)
# Add back cases where two variables exceed M-1:
#   x >= M and y >= M: x' + y' + z = N - 3 - 2M
#   Count: C(N-3-2M+2, 2) = C(N-2M-1, 2) if N-3-2M >= 0
# By symmetry, multiply by 3
# Subtract cases where all three exceed M-1:
#   x >= M, y >= M, z >= M: sum >= 3M, but sum = N-3
#   Need N-3 >= 3M, i.e., N >= 3M+3
#   Count: C(N-3-3M+2, 2) = C(N-3M-1, 2) if N-3-3M >= 0

def C2(n):
    # C(n, 2) = n*(n-1)//2 for n >= 2, else 0
    if n < 2:
        return 0
    return n * (n - 1) // 2

result = C2(N - 1) - 3 * C2(N - M - 1) + 3 * C2(N - 2 * M - 1) - C2(N - 3 * M - 1)

print(result)