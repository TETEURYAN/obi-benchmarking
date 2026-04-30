from itertools import product
from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    Xe = int(input_data[idx])-1; idx+=1
    Ye = int(input_data[idx])-1; idx+=1
    Xs = int(input_data[idx])-1; idx+=1
    Ys = int(input_data[idx])-1; idx+=1
    
    # Armários estão em células (i,j) onde i+1 e j+1 são pares (0-indexed: i e j são ímpares)
    # i.e., i%2==1 and j%2==1 in 0-indexed
    
    # Each cabinet at (i,j) (0-indexed, i odd, j odd) can fall in 4 directions
    # We need to choose a direction for each cabinet (or not fall? - problem says "derrubar armários")
    # Actually re-reading: they choose WHICH cabinets to knock down and in which direction
    # Cabinets not knocked down stay in place (1 cell blocked)
    # Cabinets knocked down block 2 cells
    # We want to maximize shortest path from entry to exit
    
    # Find all cabinet positions
    cabinets = []
    for i in range(N):
        for j in range(M):
            if i%2==1 and j%2==1:
                cabinets.append((i,j))
    
    num_cabinets = len(cabinets)
    
    # For each cabinet, possible states:
    # 0: standing (blocks only (i,j))
    # 1: fall right -> blocks (i,j) and (i,j+1)
    # 2: fall left -> blocks (i,j) and (i,j-1)
    # 3: fall down -> blocks (i,j) and (i+1,j)
    # 4: fall up -> blocks (i,j) and (i-1,j)
    
    def get_blocked(cabinet_states):
        blocked = set()
        for idx2, (i,j) in enumerate(cabinets):
            state = cabinet_states[idx2]
            blocked.add((i,j))
            if state == 1 and j+1 < M:
                blocked.add((i,j+1))
            elif state == 2 and j-1 >= 0:
                blocked.add((i,j-1))
            elif state == 3 and i+1 < N:
                blocked.add((i+1,j))
            elif state == 4 and i-1 >= 0:
                blocked.add((i-1,j))
        return blocked
    
    def bfs(blocked):
        if (Xe,Ye) in blocked or (Xs,Ys) in blocked:
            return -1
        dist = {(Xe,Ye): 1}
        q = deque([(Xe,Ye)])
        while q:
            x,y = q.popleft()
            if x==Xs and y==Ys:
                return dist[(x,y)]
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<M and (nx,ny) not in blocked and (nx,ny) not in dist:
                    dist[(nx,ny)] = dist[(x,y)]+1
                    q.append((nx,ny))
        return -1
    
    best = 0
    
    # Each cabinet has 5 choices but falling outside bounds is invalid -> treat as standing
    # With up to 25 cabinets (11x11 grid has ~25 cabinets), 5^25 is too large
    # But N,M <= 11, so max cabinets = 5*5 = 25... too many
    # Need smarter approach
    # Actually cabinets at odd i, odd j in 0-indexed: floor(N/2)*floor(M/2)
    # For N=M=11: 5*5=25 cabinets, 5^25 way too large
    
    # Key insight: cabinets only fall into adjacent cells which are even-indexed
    # The grid has a structure. Let's use backtracking with pruning.
    
    def backtrack(idx2, cabinet_states, blocked):
        nonlocal best
        if idx2 == num_cabinets:
            d = bfs(blocked)
            if d > best:
                best = d
            return
        i,j = cabinets[idx2]
        options = [(i,j)]  # standing: just (i,j) already in blocked
        extras = []
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<M and (ni,nj) not in blocked:
                extras.append((ni,nj))
        
        # Try standing
        backtrack(idx2+1, cabinet_states+[0], blocked)
        
        # Try each fall direction
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<M and (ni,nj) not in blocked:
                blocked.add((ni,nj))
                backtrack(idx2+1, cabinet_states, blocked)
                blocked.remove((ni,nj))
    
    initial_blocked = set()
    for (i,j) in cabinets:
        initial_blocked.add((i,j))
    
    backtrack(0, [], initial_blocked)
    print(best)

solve()