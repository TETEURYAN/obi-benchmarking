
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
E = int(data[1])

positions = []
directions = []
pos_to_dir = {}

index = 2
for i in range(E):
    V = int(data[index])
    D = int(data[index + 1])
    positions.append(V)
    directions.append(D)
    pos_to_dir[V] = D
    index += 2

initial_state = tuple(sorted(positions))

def simulate():
    global positions, directions, pos_to_dir
    new_pos = [0] * E
    new_dir = [0] * E
    events = {}
    
    for i in range(E):
        p = positions[i]
        d = directions[i]
        target = (p + d - 1) % N + 1
        new_pos[i] = target
        if target not in events:
            events[target] = []
        events[target].append((i, d))
    
    for target, lst in events.items():
        if len(lst) >= 2:
            for idx, orig_d in lst:
                new_dir[idx] = -orig_d
        else:
            idx, orig_d = lst[0]
            prev_pos = (target - orig_d - 1) % N + 1
            if prev_pos in pos_to_dir and pos_to_dir[prev_pos] == -orig_d:
                new_dir[idx] = -orig_d
            else:
                new_dir[idx] = orig_d
    
    new_positions = []
    new_pos_to_dir = {}
    for i in range(E):
        p = new_pos[i]
        d = new_dir[i]
        new_positions.append(p)
        new_pos_to_dir[p] = d
    
    positions = new_positions
    directions = new_dir
    pos_to_dir = new_pos_to_dir
    return tuple(sorted(new_positions))

time = 0
seen = {}
current = initial_state
seen[current] = 0

while True:
    time += 1
    current = simulate()
    if current in seen:
        cycle_start = seen[current]
        cycle_length = time - cycle_start
        if cycle_start == 0:
            print(cycle_length)
            sys.exit(0)
        else:
            print(cycle_length)
            sys.exit(0)
    seen[current] = time
