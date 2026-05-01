import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    piles = list(map(int, input_data[1:n+1]))
    
    total = sum(piles)
    
    # A perfect staircase with n piles has heights: a, a+1, a+2, ..., a+n-1
    # Total = n*a + n*(n-1)/2
    # So n*a = total - n*(n-1)/2
    # a = (total - n*(n-1)/2) / n
    
    triangle = n * (n - 1) // 2
    remainder = total - triangle
    
    if remainder <= 0 or remainder % n != 0:
        print(-1)
        return
    
    a = remainder // n
    
    if a <= 0:
        print(-1)
        return
    
    # Target staircase: a, a+1, ..., a+n-1 (left to right, lowest on left)
    target = [a + i for i in range(n)]
    
    # We need to find the minimum number of moves
    # A move is moving one cube from one pile to another
    # The number of moves = number of cubes that need to be moved
    # Since total is conserved, moves = sum of (pile - target) for all piles where pile > target
    # = sum of (target - pile) for all piles where pile < target
    # Both are equal since total is conserved
    
    # But wait - we can rearrange the piles? Or do the piles stay in their positions?
    # Re-reading: "mover alguns cubos para formar os degraus das escadas"
    # The piles are in fixed positions, we move cubes between piles
    # The staircase must have lowest step on the left
    # So the target is fixed: position i gets height a+i
    
    # Number of moves = sum of max(0, piles[i] - target[i]) for all i
    # (cubes moved out = cubes moved in, both equal this sum)
    
    moves = sum(max(0, piles[i] - target[i]) for i in range(n))
    
    print(moves)

solve()