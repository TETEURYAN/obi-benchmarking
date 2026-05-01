import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    E = int(input_data[idx]); idx += 1
    
    initial_positions = set()
    indios = []
    
    for _ in range(E):
        v = int(input_data[idx]); idx += 1
        d = int(input_data[idx]); idx += 1
        indios.append([v - 1, d])  # 0-indexed
        initial_positions.add(v - 1)
    
    beat = 0
    
    while True:
        # Compute next positions
        # For each indio, compute where they want to go
        next_pos = []
        for i in range(E):
            pos, d = indios[i]
            np = (pos + d) % N
            next_pos.append(np)
        
        # Check collision type 2: two indios in consecutive toras jumping toward each other
        # Indio A at pos p with direction 1 wants to go to p+1
        # Indio B at pos p+1 with direction -1 wants to go to p
        # They are jumping toward each other
        
        # Build current position map
        pos_to_indio = {}
        for i in range(E):
            pos_to_indio[indios[i][0]] = i
        
        # Find type 2 collisions first
        blocked = set()
        for i in range(E):
            pos, d = indios[i]
            np = next_pos[i]
            # Check if there's an indio at np going in direction -d (toward pos)
            if np in pos_to_indio:
                j = pos_to_indio[np]
                if indios[j][1] == -d:
                    # They are jumping toward each other
                    blocked.add(i)
                    blocked.add(j)
        
        # For blocked indios, they don't move and reverse direction
        # But we need to handle: if a blocked indio stays, and another indio lands on it
        # First, apply blocking: blocked indios stay and reverse
        
        # Compute actual next positions
        actual_next = []
        for i in range(E):
            if i in blocked:
                actual_next.append(indios[i][0])  # stays
            else:
                actual_next.append(next_pos[i])
        
        # Find type 1 collisions: two indios land on same tora with opposite directions
        # Group by next position
        pos_groups = defaultdict(list)
        for i in range(E):
            pos_groups[actual_next[i]].append(i)
        
        # Apply moves and handle collisions
        new_indios = []
        for i in range(E):
            new_indios.append([actual_next[i], indios[i][1]])
        
        # Handle blocked: reverse direction
        for i in blocked:
            new_indios[i][1] = -indios[i][1]
        
        # Handle type 1 collisions
        for pos, group in pos_groups.items():
            if len(group) == 2:
                i, j = group
                # Check if they have opposite directions
                if new_indios[i][1] == -new_indios[j][1]:
                    new_indios[i][1] = -new_indios[i][1]
                    new_indios[j][1] = -new_indios[j][1]
            # More than 2 shouldn't happen given constraints
        
        beat += 1
        indios = new_indios
        
        # Check if current occupied positions match initial
        current_positions = set(indios[i][0] for i in range(E))
        if current_positions == initial_positions:
            print(beat)
            return

solve()