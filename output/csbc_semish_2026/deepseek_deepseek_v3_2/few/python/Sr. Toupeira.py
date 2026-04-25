import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    S = int(data[idx]); T = int(data[idx+1]); idx += 2
    
    # matriz de adjacência (S <= 1000, ok)
    adj = [[False] * (S + 1) for _ in range(S + 1)]
    for _ in range(T):
        X = int(data[idx]); Y = int(data[idx+1]); idx += 2
        adj[X][Y] = True
        adj[Y][X] = True
    
    P = int(data[idx]); idx += 1
    possible_count = 0
    
    for _ in range(P):
        N = int(data[idx]); idx += 1
        seq = list(map(int, data[idx:idx+N])); idx += N
        
        ok = True
        for i in range(N - 1):
            a, b = seq[i], seq[i+1]
            if not adj[a][b]:
                ok = False
                break
        if ok:
            possible_count += 1
    
    print(possible_count)

if __name__ == "__main__":
    main()