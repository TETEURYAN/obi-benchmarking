import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    S = int(input_data[0])
    T = int(input_data[1])
    
    adj = [[False] * (S + 1) for _ in range(S + 1)]
    
    idx = 2
    for _ in range(T):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u][v] = True
        adj[v][u] = True
        idx += 2
        
    P = int(input_data[idx])
    idx += 1
    
    possible_count = 0
    for _ in range(P):
        N = int(input_data[idx])
        idx += 1
        
        possible = True
        prev = int(input_data[idx])
        idx += 1
        for _ in range(1, N):
            curr = int(input_data[idx])
            idx += 1
            if not adj[prev][curr]:
                possible = False
            prev = curr
            
        if possible:
            possible_count += 1
            
    print(possible_count)

if __name__ == '__main__':
    solve()