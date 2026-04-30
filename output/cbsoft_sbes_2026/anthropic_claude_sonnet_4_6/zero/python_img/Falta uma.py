from itertools import permutations
import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    
    present = set()
    for _ in range(1, N):  # N! - 1 lines... but let's just read all remaining
        pass
    
    # Reset and read properly
    # Already consumed N, now read N!-1 permutations
    cards = []
    total = 1
    for i in range(1, N+1):
        total *= i
    
    for _ in range(total - 1):
        perm = tuple(int(input_data[idx+i]) for i in range(N))
        idx += N
        cards.append(perm)
    
    present = set(cards)
    
    all_perms = set(permutations(range(1, N+1)))
    
    missing = all_perms - present
    result = list(missing)[0]
    
    print(' '.join(map(str, result)))

main()