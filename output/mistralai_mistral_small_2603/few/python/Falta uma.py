
import sys
from math import factorial

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total_perms = factorial(n)
    perms = data[1:total_perms]
    expected_sum = sum(range(1, n + 1))
    missing = []
    for i in range(n):
        col_sum = 0
        for perm in perms:
            num = int(perm.split()[i])
            col_sum += num
        target = expected_sum * (total_perms - 1) // n
        missing_num = target - col_sum
        missing.append(str(missing_num))
    print(' '.join(missing))

if __name__ == "__main__":
    main()
