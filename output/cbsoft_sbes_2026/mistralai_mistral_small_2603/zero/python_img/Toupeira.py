
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
        if N == 1:
            count += 1
            continue
        for i in range(N - 1):
            a = int(data[ptr])
            ptr += 1
            b = int(data[ptr])
            ptr += 1
            if not graph[a][b]:
                valid = False
        if valid:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
