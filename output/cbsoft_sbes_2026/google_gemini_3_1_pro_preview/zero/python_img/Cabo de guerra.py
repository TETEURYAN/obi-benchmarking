import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    forces = [int(x) for x in input_data]
    
    total_sum = sum(forces)
    if total_sum % 2 != 0:
        print('N')
        return
    
    target = total_sum // 2
    for comb in combinations(forces, 3):
        if sum(comb) == target:
            print('S')
            return
            
    print('N')

if __name__ == '__main__':
    solve()