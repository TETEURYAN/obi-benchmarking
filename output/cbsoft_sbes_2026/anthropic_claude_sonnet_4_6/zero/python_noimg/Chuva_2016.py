import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    h = [int(input_data[i+1]) for i in range(n)]
    
    # For each section, water level = min(max_left, max_right)
    # Water depth = water_level - h[i]
    # Section is covered if water depth >= 1, i.e., water_level - h[i] >= 1
    
    # Compute prefix max (max from left)
    left_max = [0] * n
    left_max[0] = h[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], h[i])
    
    # Compute suffix max (max from right)
    right_max = [0] * n
    right_max[n-1] = h[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], h[i])
    
    count = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level - h[i] >= 1:
            count += 1
    
    print(count)

solve()