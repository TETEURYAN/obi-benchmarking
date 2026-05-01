import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
p = int(input_data[2])

stones = set()
idx = 3
for _ in range(p):
    c = int(input_data[idx])
    l = int(input_data[idx+1])
    stones.add((c, l))
    idx += 2

sc = int(input_data[idx])
sl = int(input_data[idx+1])
idx += 2
rc = int(input_data[idx])
rl = int(input_data[idx+1])

start = (sc, sl)
end = (rc, rl)

q = deque([start])
visited = {start}

while q:
    curr_c, curr_l = q.popleft()
    
    if (curr_c, curr_l) == end:
        print('S')
        exit()
        
    for dc, dl in [(-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0),
                   (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3)]:
        nc, nl = curr_c + dc, curr_l + dl
        if (nc, nl) in stones and (nc, nl) not in visited:
            visited.add((nc, nl))
            q.append((nc, nl))
            
print('N')