import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    forces = [int(x) for x in input_data]
    
    total_force = sum(forces)
    
    if total_force % 2 != 0:
        print('N')
        return
        
    target = total_force // 2
    
    for combo in combinations(forces, 3):
        if sum(combo) == target:
            print('S')
            return
            
    print('N')

if __name__ == '__main__':
    solve()