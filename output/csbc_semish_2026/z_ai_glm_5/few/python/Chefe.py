import sys

sys.setrecursionlimit(200000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        I = int(next(iterator))
    except StopIteration:
        return

    ages = [0] * (N + 1)
    for i in range(1, N + 1):
        ages[i] = int(next(iterator))

    # parents[v] contains list of u such that u manages v
    parents = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u = int(next(iterator))
        v = int(next(iterator))
        parents[v].append(u)

    # Precompute ancestors for all positions
    memo_ancestors = [None] * (N + 1)

    def get_ancestors(v):
        if memo_ancestors[v] is not None:
            return memo_ancestors[v]
        
        anc_set = set()
        for p in parents[v]:
            anc_set.add(p)
            anc_set.update(get_ancestors(p))
        
        memo_ancestors[v] = anc_set
        return anc_set

    for i in range(1, N + 1):
        get_ancestors(i)

    # Mapping positions to IDs and vice versa
    pos_to_id = list(range(N + 1))
    id_to_pos = list(range(N + 1))

    output = []

    for _ in range(I):
        cmd = next(iterator)
        if cmd == 'T':
            a = int(next(iterator))
            b = int(next(iterator))
            
            pos_a = id_to_pos[a]
            pos_b = id_to_pos[b]
            
            pos_to_id[pos_a], pos_to_id[pos_b] = pos_to_id[pos_b], pos_to_id[pos_a]
            
            id_to_pos[a] = pos_b
            id_to_pos[b] = pos_a
            
        elif cmd == 'P':
            e = int(next(iterator))
            
            pos_e = id_to_pos[e]
            anc_positions = memo_ancestors[pos_e]
            
            if not anc_positions:
                output.append('*')
            else:
                min_age = float('inf')
                for p in anc_positions:
                    emp_id = pos_to_id[p]
                    age = ages[emp_id]
                    if age < min_age:
                        min_age = age
                output.append(str(min_age))

    print('\n'.join(output))

if __name__ == '__main__':
    main()