import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        F = int(next(iterator))
        R = int(next(iterator))
    except StopIteration:
        return

    positions = []
    for _ in range(R):
        try:
            positions.append(int(next(iterator)))
        except StopIteration:
            break
            
    # The positions are given in increasing order, but sorting ensures correctness
    # and is O(R log R), which is negligible.
    positions.sort()
    
    max_days = 0
    
    # Calculate days to cover the left edge (position 1 to first seed)
    # Distance is positions[0] - 1
    max_days = max(max_days, positions[0] - 1)
    
    # Calculate days to cover the right edge (last seed to position F)
    # Distance is F - positions[-1]
    max_days = max(max_days, F - positions[-1])
    
    # Calculate days to cover gaps between seeds
    for i in range(R - 1):
        dist = positions[i+1] - positions[i]
        # The time to cover the gap between two seeds is the distance divided by 2 (integer division)
        max_days = max(max_days, dist // 2)
        
    print(max_days)

if __name__ == '__main__':
    solve()