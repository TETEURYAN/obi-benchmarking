
import math

def count_arrangements(N):
    if N == 1:
        return 0
    count = 0
    max_x = int(math.isqrt(N)) + 1
    for x in range(1, max_x + 1):
        if N % x == 0:
            y = N // x
            if (x - 1) * (y - 1) >= 1:
                count += 1
    return count

N = int(input())
print(count_arrangements(N))
