import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    grid = input_data[1:n+1]
    
    current_food = 0
    max_food = 0
    
    for i in range(n):
        row = grid[i]
        # Determine direction: Left to Right for even rows, Right to Left for odd rows
        if i % 2 == 0:
            col_indices = range(n)
        else:
            col_indices = range(n - 1, -1, -1)
            
        for j in col_indices:
            char = row[j]
            if char == 'o':
                current_food += 1
            elif char == 'A':
                current_food = 0
            
            if current_food > max_food:
                max_food = current_food
                
    print(max_food)

if __name__ == '__main__':
    solve()