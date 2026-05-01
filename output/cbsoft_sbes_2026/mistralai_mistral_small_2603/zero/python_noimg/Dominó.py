
import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while True:
        N = int(input[ptr])
        ptr += 1
        if N == 0:
            break
        graph = defaultdict(int)
        degree = defaultdict(int)
        edges = []
        for _ in range(N):
            x = int(input[ptr])
            y = int(input[ptr+1])
            ptr += 2
            edges.append((x, y))
            graph[x] += 1
            graph[y] += 1
            degree[x] += 1
            degree[y] += 1
        odd_degree = 0
        for node in degree:
            if degree[node] % 2 != 0:
                odd_degree += 1
        if odd_degree == 0 or odd_degree == 2:
            print(f"Teste {test_num}")
            print("sim")
            print()
        else:
            print(f"Teste {test_num}")
            print("nao")
            print()
        test_num += 1

solve()
