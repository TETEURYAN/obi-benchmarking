import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
dice = []
idx = 1
for _ in range(n):
    dice.append([int(x) for x in input_data[idx:idx+6]])
    idx += 6

opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

max_total_sum = 0

for first_bottom_idx in range(6):
    current_sum = 0
    bottom_val = dice[0][first_bottom_idx]
    
    for i in range(n):
        b_idx = dice[i].index(bottom_val)
        t_idx = opposite[b_idx]
        top_val = dice[i][t_idx]
        
        max_side = 0
        for j in range(6):
            if j != b_idx and j != t_idx:
                if dice[i][j] > max_side:
                    max_side = dice[i][j]
        
        current_sum += max_side
        bottom_val = top_val
        
    if current_sum > max_total_sum:
        max_total_sum = current_sum

print(max_total_sum)