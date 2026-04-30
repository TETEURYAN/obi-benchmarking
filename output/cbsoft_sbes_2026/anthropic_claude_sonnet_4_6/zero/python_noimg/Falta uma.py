from itertools import permutations
import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    given = set()
    for _ in range(1, __import__('math').factorial(n)):
        perm = tuple(int(input_data[idx+i]) for i in range(n))
        idx += n
        given.add(perm)
    
    for perm in permutations(range(1, n+1)):
        if perm not in given:
            print(*perm)
            return

main()