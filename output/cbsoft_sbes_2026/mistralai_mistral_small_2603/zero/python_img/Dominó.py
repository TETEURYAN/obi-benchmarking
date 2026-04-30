
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
        degrees = defaultdict(int)
        for _ in range(N):
            x = int(input[ptr])
            y = int(input[ptr+1])
            ptr += 2
            graph[(x, y)] += 1
            degrees[x] += 1
            degrees[y] += 1
        odd_degree = 0
        for degree in degrees.values():
            if degree % 2 != 0:
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
