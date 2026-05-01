import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        mi = int(next(it))
        for _ in range(mi):
            x = int(next(it))
            adj[i].append(x)
    
    color = [-1] * (n+1)
    color[1] = 0
    
    def dfs(v):
        for u in adj[v]:
            if color[u] == -1:
                color[u] = 1 - color[v]
                dfs(u)
            elif color[u] == color[v]:
                return False
        return True
    
    dfs(1)
    
    team0 = []
    team1 = []
    for i in range(1, n+1):
        if color[i] == 0:
            team0.append(i)
        else:
            team1.append(i)
    
    sys.stdout.write(" ".join(map(str, team0)) + "\n")
    sys.stdout.write(" ".join(map(str, team1)) + "\n")

if __name__ == "__main__":
    main()