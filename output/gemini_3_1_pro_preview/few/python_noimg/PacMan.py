import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
grid = input_data[1:n+1]

max_food = 0
current_food = 0

for i in range(n):
    row = grid[i]
    if i % 2 == 1:
        row = row[::-1]
        
    for cell in row:
        if cell == 'o':
            current_food += 1
            if current_food > max_food:
                max_food = current_food
        elif cell == 'A':
            current_food = 0

print(max_food)