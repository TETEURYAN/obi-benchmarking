
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    ptr = 0
    N = int(data[ptr])
    M = int(data[ptr+1])
    I = int(data[ptr+2])
    ptr += 3

    ages = list(map(int, data[ptr:ptr+N]))
    ptr += N

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        X = int(data[ptr])
        Y = int(data[ptr+1])
        adj[X].append(Y)
        ptr += 2

    instructions = []
    for _ in range(I):
        t = data[ptr]
        if t == 'T':
            A = int(data[ptr+1])
            B = int(data[ptr+2])
            instructions.append(('T', A, B))
            ptr += 3
        else:
            E = int(data[ptr+1])
            instructions.append(('P', E))
            ptr += 2

    parent = [0] * (N + 1)
    for u in range(1, N + 1):
        if adj[u]:
            parent[u] = adj[u][0]

    def find_root(u):
        while parent[u] != 0:
            u = parent[u]
        return u

    def get_ancestors(u):
        ancestors = []
        while u != 0:
            ancestors.append(u)
            u = parent[u]
        return ancestors

    for instr in instructions:
        if instr[0] == 'T':
            A, B = instr[1], instr[2]
            if parent[A] == B:
                parent[A] = parent[B]
            elif parent[B] == A:
                parent[B] = parent[A]
            else:
                root_A = find_root(A)
                root_B = find_root(B)
                if root_A != root_B:
                    parent[A] = B
                    parent[B] = A
                else:
                    ancestors_A = get_ancestors(A)
                    ancestors_B = get_ancestors(B)
                    common_ancestor = None
                    for a in ancestors_A:
                        if a in ancestors_B:
                            common_ancestor = a
                            break
                    if common_ancestor is not None:
                        parent[A] = B
                        parent[B] = A
        else:
            E = instr[1]
            if parent[E] == 0:
                print('*')
            else:
                min_age = float('inf')
                current = E
                while current != 0:
                    if ages[current-1] < min_age:
                        min_age = ages[current-1]
                    current = parent[current]
                print(min_age)

if __name__ == "__main__":
    main()
