
import sys

def main():
    teste = 1
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        if not line:
            continue
        E, L = map(int, line.split())
        if E == 0 and L == 0:
            break

        graph = [[] for _ in range(E+1)]
        for _ in range(L):
            X, Y = map(int, sys.stdin.readline().split())
            graph[X].append(Y)
            graph[Y].append(X)

        visited = [False] * (E+1)
        stack = [1]
        visited[1] = True
        count = 1

        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    stack.append(neighbor)

        print(f"Teste {teste}")
        if count == E:
            print("normal")
        else:
            print("falha")
        print()
        teste += 1

if __name__ == "__main__":
    main()
