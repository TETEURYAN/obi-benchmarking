
import sys
from itertools import permutations

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    expected = set(permutations(range(1, N+1)))
    given = []
    index = 1
    for _ in range(math.factorial(N) - 1):
        perm = tuple(map(int, data[index:index+N]))
        given.append(perm)
        index += N
    missing = expected - set(given)
    print(' '.join(map(str, missing.pop())))

if __name__ == "__main__":
    import math
    main()
