import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

left_boots = [0] * 61
right_boots = [0] * 61

idx = 1
for _ in range(n):
    m = int(input_data[idx])
    l = input_data[idx+1]
    idx += 2
    
    if l == 'E':
        left_boots[m] += 1
    elif l == 'D':
        right_boots[m] += 1

total_pairs = 0
for i in range(30, 61):
    total_pairs += min(left_boots[i], right_boots[i])

print(total_pairs)