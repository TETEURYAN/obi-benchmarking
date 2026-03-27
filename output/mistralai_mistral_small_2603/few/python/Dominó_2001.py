
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while ptr < len(data):
        N = int(data[ptr])
        ptr += 1
        if N == 0:
            break
        graph = defaultdict(int)
        degree = defaultdict(int)
        for _ in range(N):
            x = int(data[ptr])
            y = int(data[ptr + 1])
            ptr += 2
            if x > y:
                x, y = y, x
            graph[(x, y)] += 1
            degree[x] += 1
            degree[y] += 1

        odd_degree_vertices = 0
        for v in degree:
            if degree[v] % 2 != 0:
                odd_degree_vertices += 1

        if odd_degree_vertices == 0 or odd_degree_vertices == 2:
            print(f"Teste {test_num}")
            print("sim")
        else:
            print(f"Teste {test_num}")
            print("nao")
        print()
        test_num += 1

if __name__ == "__main__":
    main()
