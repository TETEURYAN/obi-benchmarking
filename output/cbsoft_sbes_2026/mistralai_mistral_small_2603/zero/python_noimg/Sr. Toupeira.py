
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    ptr = 0
    S = int(data[ptr])
    ptr += 1
    T = int(data[ptr])
    ptr += 1

    graph = defaultdict(set)
    for _ in range(T):
        x = int(data[ptr])
        ptr += 1
        y = int(data[ptr])
        ptr += 1
        graph[x].add(y)
        graph[y].add(x)

    P = int(data[ptr])
    ptr += 1
    count = 0

    for _ in range(P):
        N = int(data[ptr])
        ptr += 1
        valid = True
        for i in range(N - 1):
            u = int(data[ptr])
            ptr += 1
            v = int(data[ptr])
            ptr += 1
            if v not in graph[u]:
                valid = False
        if valid:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
