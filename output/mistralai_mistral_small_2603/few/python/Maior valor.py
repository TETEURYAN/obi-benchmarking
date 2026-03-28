
import sys

def sum_digits(x):
    return sum(int(d) for d in str(x))

def solve():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
    N = int(data[0])
    M = int(data[1])
    S = int(data[2])

    max_val = -1
    for num in range(M, N - 1, -1):
        if sum_digits(num) == S:
            max_val = num
            break
    print(max_val)

solve()
