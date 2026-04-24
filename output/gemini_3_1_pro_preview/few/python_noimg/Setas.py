import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
grid = input_data[1:]

unsafe = [[False] * N for _ in range(N)]
Q = deque()
unsafe_count = 0

for r in range(N):
    for c in range(N):
        ch = grid[r][c]
        if (r == 0 and ch == 'A') or \
           (r == N - 1 and ch == 'V') or \
           (c == 0 and ch == '<') or \
           (c == N - 1 and ch == '>'):
            unsafe[r][c] = True
            Q.append((r, c))
            unsafe_count += 1

while Q:
    r, c = Q.popleft()
    
    if r < N - 1 and not unsafe[r + 1][c] and grid[r + 1][c] == 'A':
        unsafe[r + 1][c] = True
        Q.append((r + 1, c))
        unsafe_count += 1
        
    if r > 0 and not unsafe[r - 1][c] and grid[r - 1][c] == 'V':
        unsafe[r - 1][c] = True
        Q.append((r - 1, c))
        unsafe_count += 1
        
    if c < N - 1 and not unsafe[r][c + 1] and grid[r][c + 1] == '<':
        unsafe[r][c + 1] = True
        Q.append((r, c + 1))
        unsafe_count += 1
        
    if c > 0 and not unsafe[r][c - 1] and grid[r][c - 1] == '>':
        unsafe[r][c - 1] = True
        Q.append((r, c - 1))
        unsafe_count += 1

print(N * N - unsafe_count)