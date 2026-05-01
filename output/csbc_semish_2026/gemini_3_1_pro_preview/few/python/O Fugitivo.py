import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
m_sq = m * m

x = 0
y = 0
exceeded = 0

idx = 2
for _ in range(n):
    direction = input_data[idx]
    dist = int(input_data[idx+1])
    idx += 2
    
    if direction == 'N':
        y += dist
    elif direction == 'S':
        y -= dist
    elif direction == 'L':
        x += dist
    elif direction == 'O':
        x -= dist
        
    if x * x + y * y > m_sq:
        exceeded = 1
        break

print(exceeded)