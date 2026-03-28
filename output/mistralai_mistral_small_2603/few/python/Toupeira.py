
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    S = int(data[ptr])
    ptr += 1
    T = int(data[ptr])
    ptr += 1

    adj = [[] for _ in range(S + 1)]
    for _ in range(T):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    P = int(data[ptr])
    ptr += 1

    valid = 0
    for _ in range(P):
        N = int(data[ptr])
        ptr += 1
        sequence = list(map(int, data[ptr:ptr + N]))
        ptr += N

        possible = True
        for i in range(N - 1):
            u = sequence[i]
            v = sequence[i + 1]
            if v not in adj[u]:
                possible = False
                break

        if possible:
            valid += 1

    print(valid)

if __name__ == "__main__":
    main()
