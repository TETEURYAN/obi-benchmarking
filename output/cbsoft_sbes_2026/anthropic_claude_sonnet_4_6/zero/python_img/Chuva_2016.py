import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    h = [int(input_data[i+1]) for i in range(n)]
    
    # For each section, water level = min(max_left, max_right)
    # Water depth = water_level - h[i]
    # Section is covered if water_depth >= 1
    
    # Compute max from left
    max_left = [0] * n
    max_left[0] = h[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], h[i])
    
    # Compute max from right
    max_right = [0] * n
    max_right[n-1] = h[n-1]
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], h[i])
    
    count = 0
    for i in range(n):
        water_level = min(max_left[i], max_right[i])
        depth = water_level - h[i]
        if depth >= 1:
            count += 1
    
    print(count)

solve()