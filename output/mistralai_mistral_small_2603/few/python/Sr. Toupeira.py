
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    S = int(data[idx])
    T = int(data[idx+1])
    idx += 2

    adj = [set() for _ in range(S + 1)]
    for _ in range(T):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2

    P = int(data[idx])
    idx += 1

    count = 0
    for _ in range(P):
        N = int(data[idx])
        idx += 1
        path = list(map(int, data[idx:idx+N]))
        idx += N

        valid = True
        for i in range(N - 1):
            u = path[i]
            v = path[i+1]
            if v not in adj[u]:
                valid = False
                break

        if valid:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
