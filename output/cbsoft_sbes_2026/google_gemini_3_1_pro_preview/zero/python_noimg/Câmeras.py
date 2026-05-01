import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    K = int(input_data[2])
    
    observed = [[False] * (M + 1) for _ in range(N + 1)]
    
    idx = 3
    for _ in range(K):
        C = int(input_data[idx])
        L = int(input_data[idx+1])
        D = input_data[idx+2]
        idx += 3
        
        if D == 'N':
            for l in range(L, 0, -1):
                observed[C][l] = True
        elif D == 'S':
            for l in range(L, M + 1):
                observed[C][l] = True
        elif D == 'L':
            for c in range(C, N + 1):
                observed[c][L] = True
        elif D == 'O':
            for c in range(C, 0, -1):
                observed[c][L] = True
                
    if observed[1][1] or observed[N][M]:
        print('N')
        return
        
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    queue = deque([(1, 1)])
    visited[1][1] = True
    
    while queue:
        c, l = queue.popleft()
        
        if c == N and l == M:
            print('S')
            return
            
        for dc, dl in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nc, nl = c + dc, l + dl
            if 1 <= nc <= N and 1 <= nl <= M:
                if not observed[nc][nl] and not visited[nc][nl]:
                    visited[nc][nl] = True
                    queue.append((nc, nl))
                    
    print('N')

if __name__ == '__main__':
    solve()