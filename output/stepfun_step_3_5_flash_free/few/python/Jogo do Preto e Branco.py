import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    P = int(next(it))
    pretas = set()
    for _ in range(P):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        pretas.add((x, y))
    
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    cand = []
    for i in range(L):
        for j in range(C):
            if (i,j) in pretas:
                continue
            tem_preta = False
            for dx,dy in dirs:
                ni, nj = i+dx, j+dy
                if 0 <= ni < L and 0 <= nj < C and (ni,nj) in pretas:
                    tem_preta = True
                    break
            if tem_preta:
                cand.append((i,j))
    
    n = len(cand)
    if n == 0:
        print(0)
        return
    
    left = []
    right = []
    for pos in cand:
        i,j = pos
        if (i+j) % 2 == 1:
            left.append(pos)
        else:
            right.append(pos)
    
    left_idx = {pos: i for i, pos in enumerate(left)}
    right_idx = {pos: i for i, pos in enumerate(right)}
    
    adj = [[] for _ in range(len(left))]
    for i, (x,y) in enumerate(left):
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if (nx,ny) in right_idx:
                adj[i].append(right_idx[(nx,ny)])
    
    matchR = [-1] * len(right)
    
    def dfs(u, seen):
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or dfs(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False
    
    matching = 0
    for u in range(len(left)):
        seen = [False] * len(right)
        if dfs(u, seen):
            matching += 1
    
    print(n - matching)

if __name__ == "__main__":
    main()