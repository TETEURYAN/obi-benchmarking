
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    S = int(data[ptr])
    ptr += 1
    T = int(data[ptr])
    ptr += 1

    graph = [[False] * (S + 1) for _ in range(S + 1)]
    for _ in range(T):
        x = int(data[ptr])
        ptr += 1
        y = int(data[ptr])
        ptr += 1
        graph[x][y] = True
        graph[y][x] = True

    P = int(data[ptr])
    ptr += 1

    count = 0
    for _ in range(P):
        N = int(data[ptr])
        ptr += 1
        valid = True
        path = list(map(int, data[ptr:ptr + N]))
        ptr += N

        for i in range(N - 1):
            u = path[i]
            v = path[i + 1]
            if not graph[u][v]:
                valid = False
                break

        if valid:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
