
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    # Remove adjacent duplicates to simplify local extrema detection
    A_clean = [A[0]]
    for i in range(1, N):
        if A[i] != A_clean[-1]:
            A_clean.append(A[i])
            
    M = len(A_clean)
    
    # Group indices by their heights
    positions = defaultdict(list)
    for i, h in enumerate(A_clean):
        positions[h].append(i)
        
    # Sort unique heights in descending order
    unique_heights = sorted(positions.keys(), reverse=True)
    
    current_segments = 0
    max_segments = 0
    
    # Sweep line from top to bottom
    for h in unique_heights:
        for i in positions[h]:
            # Check if neighbors are strictly greater (meaning they are already active)
            left_active = (i > 0 and A_clean[i-1] > A_clean[i])
            right_active = (i < M - 1 and A_clean[i+1] > A_clean[i])
            
            if left_active and right_active:
                # Connects two existing segments
                current_segments -= 1
            elif not left_active and not right_active:
                # Forms a new segment
                current_segments += 1
            # If exactly one is active, it just extends an existing segment (no change in count)
            
        # Update max_segments after processing all elements of the same height
        if current_segments > max_segments:
            max_segments = current_segments
            
    # The total number of pieces is the number of segments above the cut + 1 (the base piece)
    print(max_segments + 1)

if __name__ == '__main__':
    solve()
