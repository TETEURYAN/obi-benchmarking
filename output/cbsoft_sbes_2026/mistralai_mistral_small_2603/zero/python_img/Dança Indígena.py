
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    E = int(data[1])
    indices = []
    directions = []
    pos = 2
    for _ in range(E):
        v = int(data[pos])
        d = int(data[pos+1])
        indices.append(v)
        directions.append(d)
        pos += 2

    if E == 0:
        print(0)
        return

    visited_states = {}
    steps = 0
    state = (tuple(indices), tuple(directions))
    visited_states[state] = steps

    while True:
        new_indices = []
        new_directions = []
        changed = [False] * E

        for i in range(E):
            if changed[i]:
                continue
            current_pos = indices[i]
            current_dir = directions[i]
            next_pos = current_pos + current_dir
            if next_pos > N:
                next_pos = 1
            elif next_pos < 1:
                next_pos = N

            for j in range(i+1, E):
                if changed[j]:
                    continue
                if next_pos == indices[j]:
                    if current_dir != directions[j]:
                        changed[i] = True
                        changed[j] = True
                        directions[i] *= -1
                        directions[j] *= -1
                    else:
                        changed[i] = True
                        changed[j] = True
                        directions[i] *= -1
                        directions[j] *= -1

        for i in range(E):
            if changed[i]:
                new_indices.append(indices[i])
                new_directions.append(directions[i])
            else:
                new_indices.append(indices[i] + directions[i])
                if new_indices[-1] > N:
                    new_indices[-1] = 1
                elif new_indices[-1] < 1:
                    new_indices[-1] = N
                new_directions.append(directions[i])

        steps += 1
        new_state = (tuple(new_indices), tuple(new_directions))
        if new_state in visited_states:
            print(steps - visited_states[new_state])
            return
        visited_states[new_state] = steps

        indices = new_indices
        directions = new_directions

if __name__ == "__main__":
    main()
