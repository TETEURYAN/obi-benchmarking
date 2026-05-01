from collections import deque
import sys

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    
    observed = [[False] * N for _ in range(M)]
    
    for _ in range(K):
        c, l, d = input().split()
        c = int(c) - 1
        l = int(l) - 1
        
        if d == 'N':
            for r in range(l, -1, -1):
                observed[r][c] = True
        elif d == 'S':
            for r in range(l, M):
                observed[r][c] = True
        elif d == 'L':
            for col in range(c, N):
                observed[l][col] = True
        else:  # 'O'
            for col in range(c, -1, -1):
                observed[l][col] = True
    
    if observed[0][0] or observed[M-1][N-1]:
        print('N')
        return
    
    visited = [[False] * N for _ in range(M)]
    q = deque([(0, 0)])
    visited[0][0] = True
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        r, c = q.popleft()
        if r == M - 1 and c == N - 1:
            print('S')
            return
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and not observed[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))
    
    print('N')

if __name__ == "__main__":
    main()