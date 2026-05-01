
import sys
from collections import defaultdict
import heapq

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = int(input[ptr]), int(input[ptr+1])
    ptr += 2

    graph = defaultdict(list)
    for _ in range(M):
        P, Q, U = int(input[ptr]), int(input[ptr+1]), int(input[ptr+2])
        ptr += 3
        graph[P].append((Q, U))
        graph[Q].append((P, U))

    def prim():
        min_heap = []
        visited = set()
        total_cost = 0
        start_node = 0
        heapq.heappush(min_heap, (0, start_node))

        while min_heap and len(visited) < N:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost
            for v, c in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (c, v))
        return total_cost

    print(prim())

if __name__ == "__main__":
    main()
