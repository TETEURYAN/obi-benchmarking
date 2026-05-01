
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    I = int(data[idx]); idx += 1

    ages = [0] * (N + 1)
    for i in range(1, N + 1):
        ages[i] = int(data[idx]); idx += 1

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        X = int(data[idx]); idx += 1
        Y = int(data[idx]; idx += 1
        adj[X].append(Y)

    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        for child in adj[i]:
            parent[child] = i

    def find_youngest_manager(E):
        if E == 0 or E > N:
            return '*'
        visited = set()
        queue = deque()
        if parent[E] != 0:
            queue.append(parent[E])
        else:
            return '*'

        min_age = float('inf')
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            if ages[current] < min_age:
                min_age = ages[current]
            for manager in adj[current]:
                if manager not in visited:
                    queue.append(manager)
            if parent[current] != 0 and parent[current] not in visited:
                queue.append(parent[current])
        if min_age == float('inf'):
            return '*'
        else:
            return min_age

    def swap_positions(A, B):
        if A == B or A > N or B > N or A == 0 or B == 0:
            return

        if parent[A] == B:
            parent[A] = parent[B]
            parent[B] = A
        elif parent[B] == A:
            parent[B] = parent[A]
            parent[A] = B
        else:
            temp = parent[A]
            parent[A] = parent[B]
            parent[B] = temp

        for i in range(1, N + 1):
            if A in adj[i]:
                adj[i].remove(A)
                adj[i].append(B)
            elif B in adj[i]:
                adj[i].remove(B)
                adj[i].append(A)

            if parent[i] == A:
                parent[i] = B
            elif parent[i] == B:
                parent[i] = A

    output = []
    for _ in range(I):
        cmd = data[idx]; idx += 1
        if cmd == 'T':
            A = int(data[idx]); idx += 1
            B = int(data[idx]); idx += 1
            swap_positions(A, B)
        elif cmd == 'P':
            E = int(data[idx]); idx += 1
            result = find_youngest_manager(E)
            if result == '*':
                output.append('*')
            else:
                output.append(str(result))

    print('\n'.join(output))

if __name__ == '__main__':
    main()
