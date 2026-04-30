
```python
import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    piles = list(map(int, input_data[1:n+1]))
    
    total = sum(piles)
    
    # A perfect staircase with n steps has heights: k, k+1, k+2, ..., k+n-1
    # Sum = n*k + (0+1+2+...+(n-1)) = n*k + n*(n-1)/2
    # So total = n*k + n*(n-1)/2
    # k = (total - n*(n-1)/2) / n
    
    triangle = n * (n - 1) // 2
    
    # Check if (total - triangle) is divisible by n and >= 1
    remainder = total - triangle
    
    if remainder <= 0 or remainder % n != 0:
        print(-1)
        return
    
    k = remainder // n
    
    # Target staircase: k, k+1, k+2, ..., k+n-1
    target = [k + i for i in range(n)]
    
    # We need to find the minimum number of moves
    # A "move" means taking a cube from one pile and placing it in another
    # The number of moves = number of cubes that need to be moved
    # Since total is conserved, moves = sum of (piles[i] - target[i]) for piles[i] > target[i]
    # = sum of (target[i] - piles[i]) for target[i] > piles[i]
    # Both are equal since total is same
    
    # But wait - the target arrangement can be any permutation of the staircase?
    # No - the problem says "degrau mais baixo da escada deve sempre estar do lado esquerdo"
    # So the staircase must be in ascending order from left to right
    # The target is fixed: k, k+1, ..., k+n-1
    
    moves = sum(abs(piles[i] - target[i]) for i in range(n)) // 2
    
    # Wait, let me reconsider. Each "move" moves one cube from one pile to another.
    # So the number of moves = sum of excess cubes = sum of deficit cubes
    # = (sum of |piles[i] - target[i]|) / 2
    
    # Actually no. If we move a cube from pile A to pile B, that's 1 move.
    # The number of moves = total cubes that need to be relocated
    # = sum of (piles[i] - target[i]) for all i where piles[i] > target[i]
    
    excess = sum(max(0, piles[i] - target[i]) for i in range(n))
    print(excess)

solve()
```