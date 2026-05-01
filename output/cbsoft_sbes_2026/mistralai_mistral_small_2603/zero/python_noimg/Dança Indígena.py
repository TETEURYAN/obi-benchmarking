
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx])
    idx += 1
    E = int(data[idx])
    idx += 1
    
    positions = []
    directions = []
    for _ in range(E):
        v = int(data[idx])
        idx += 1
        d = int(data[idx])
        idx += 1
        positions.append(v)
        directions.append(d)
    
    initial_positions = set(positions)
    visited = set()
    visited.add(frozenset((p, d) for p, d in zip(positions, directions)))
    
    steps = 0
    while True:
        new_positions = []
        new_directions = []
        collisions = set()
        skip = set()
        
        for i in range(E):
            p = positions[i]
            d = directions[i]
            new_p = p + d
            if new_p > N:
                new_p = 1
            elif new_p < 1:
                new_p = N
            new_positions.append(new_p)
            new_directions.append(d)
        
        for i in range(E):
            p = positions[i]
            d = directions[i]
            new_p = new_positions[i]
            if (p, d) in skip:
                continue
            if (new_p, -d) in collisions:
                collisions.add((new_p, d))
                collisions.add((new_p, -d))
                skip.add((p, d))
                skip.add((new_p, -d))
            else:
                collisions.add((new_p, d))
        
        for i in range(E):
            if (positions[i], directions[i]) in skip:
                new_directions[i] = -new_directions[i]
        
        positions = new_positions
        directions = new_directions
        steps += 1
        
        current_state = frozenset((p, d) for p, d in zip(positions, directions))
        if current_state == visited:
            break
        visited.add(current_state)
    
    print(steps)

if __name__ == "__main__":
    main()
