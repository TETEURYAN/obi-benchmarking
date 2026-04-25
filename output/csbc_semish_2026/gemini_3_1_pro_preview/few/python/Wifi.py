import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])

rooms = []
idx = 1
y_coords = set()
for i in range(N):
    x1 = int(input_data[idx])
    y1 = int(input_data[idx+1])
    x2 = int(input_data[idx+2])
    y2 = int(input_data[idx+3])
    idx += 4
    rooms.append((x1, y1, x2, y2))
    y_coords.add(y1)
    y_coords.add(y2)
    
y_sorted = sorted(list(y_coords))
y_map = {y: i + 1 for i, y in enumerate(y_sorted)}

events = []
for i in range(N):
    x1, y1, x2, y2 = rooms[i]
    events.append((x2, 0, y2, y1, i))
    events.append((x1, 1, y1, 0, i))
    events.append((x1, 2, y2, y1, i))
    
events.sort(key=lambda e: (e[0], e[1]))

MAX_Y = len(y_sorted) + 1
bit = [0] * MAX_Y

def add(i, delta):
    while i < MAX_Y:
        bit[i] += delta
        i += i & (-i)
        
def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

inside_count = [0] * N

for e in events:
    typ = e[1]
    if typ == 0:
        inside_count[e[4]] += query(y_map[e[3]]) - query(y_map[e[2]] - 1)
    elif typ == 1:
        add(y_map[e[2]], 1)
    else:
        inside_count[e[4]] -= query(y_map[e[3]]) - query(y_map[e[2]] - 1)
        
leaves = sum(1 for c in inside_count if c == 0)
print(leaves)