
import sys
from collections import defaultdict

def main():
    sys.setrecursionlimit(100000)
    N = int(sys.stdin.readline())
    graph = defaultdict(list)
    for _ in range(N):
        I, J = map(int, sys.stdin.readline().split())
        graph[J].append(I)

    balanced = True

    def dfs(node):
        nonlocal balanced
        if not graph[node]:
            return 1
        sizes = []
        for child in graph[node]:
            sizes.append(dfs(child))
        if len(set(sizes)) != 1:
            balanced = False
        return sum(sizes) + 1

    dfs(0)
    print('bem' if balanced else 'mal')

if __name__ == '__main__':
    main()
