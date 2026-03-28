import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    S = int(next(it))
    T = int(next(it))
    
    adj = [[False] * (S + 1) for _ in range(S + 1)]
    
    for _ in range(T):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
    
    P = int(next(it))
    possible_count = 0
    
    for _ in range(P):
        N = int(next(it))
        seq = [int(next(it)) for _ in range(N)]
        valid = True
        for i in range(N - 1):
            if not adj[seq[i]][seq[i + 1]]:
                valid = False
                break
        if valid:
            possible_count += 1
    
    print(possible_count)

if __name__ == "__main__":
    main()