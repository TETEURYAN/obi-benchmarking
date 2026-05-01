
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    I = int(next(it))

    ages = [0] * (N + 1)
    for i in range(1, N + 1):
        ages[i] = int(next(it))

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for _ in range(M):
        X = int(next(it))
        Y = int(next(it))
        graph[X].append(Y)
        in_degree[Y] += 1

    instructions = []
    for _ in range(I):
        cmd = next(it)
        if cmd == 'T':
            A = int(next(it))
            B = int(next(it))
            instructions.append(('T', A, B))
        else:
            E = int(next(it))
            instructions.append(('P', E))

    def find_youngest_manager(employee):
        visited = [False] * (N + 1)
        q = deque()
        q.append(employee)
        visited[employee] = True
        youngest = None

        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if youngest is None or ages[neighbor] < youngest:
                        youngest = ages[neighbor]
                    q.append(neighbor)
        return youngest

    def process_swap(A, B):
        if A == B:
            return
        if not graph[A] and not graph[B]:
            return

        if graph[A] and graph[B]:
            if len(graph[A]) != len(graph[B]):
                if len(graph[A]) > len(graph[B]):
                    A, B = B, A
            else:
                if in_degree[A] > in_degree[B]:
                    A, B = B, A
                elif in_degree[A] == in_degree[B]:
                    if ages[A] > ages[B]:
                        A, B = B, A

        if not graph[A]:
            A, B = B, A

        if not graph[A]:
            return

        if not graph[B]:
            for node in graph[A]:
                in_degree[node] -= 1
            graph[B] = graph[A]
            graph[A] = []
            for node in graph[B]:
                in_degree[node] += 1
        else:
            for node in graph[A]:
                in_degree[node] -= 1
            for node in graph[B]:
                in_degree[node] -= 1

            graph[A], graph[B] = graph[B], graph[A]

            for node in graph[A]:
                in_degree[node] += 1
            for node in graph[B]:
                in_degree[node] += 1

    for instruction in instructions:
        if instruction[0] == 'T':
            A, B = instruction[1], instruction[2]
            process_swap(A, B)
        else:
            E = instruction[1]
            res = find_youngest_manager(E)
            if res is None:
                print('*')
            else:
                print(res)

if __name__ == '__main__':
    main()
