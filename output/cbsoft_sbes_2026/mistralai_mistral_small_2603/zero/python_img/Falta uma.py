 sys
from itertools import permutations

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total = 1
    for i in range(1, n+1):
        total *= i
    expected = set(permutations(range(1, n+1)))
    found = set()
    index = 1
    for _ in range(total - 1):
        perm = tuple(map(int, data[index:index+n]))
        index += n
        found.add(perm)
    missing = expected - found
    print(' '.join(map(str, missing.pop())))

if __name__ == "__main__":
    main()
