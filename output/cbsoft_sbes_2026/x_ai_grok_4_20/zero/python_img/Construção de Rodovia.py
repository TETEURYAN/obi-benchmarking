
import sys
sys.setrecursionlimit(10**6)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.rank[px] += 1
        return True

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    
    edges = []
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        x = int(data[index])
        index += 1
        y = int(data[index])
        index += 1
        edges.append((x, y))
        adj[x].append(y)
        adj[y].append(x)
    
    dsu = DSU(N)
    components = []
    for i in range(1, N + 1):
        if dsu.find(i) == i:
            components.append(i)
    
    for x, y in edges:
        dsu.union(x, y)
    
    comp_id = {}
    comp_list = []
    cid = 0
    for i in range(1, N + 1):
        p = dsu.find(i)
        if p not in comp_id:
            comp_id[p] = cid
            comp_list.append([])
            cid += 1
        comp_list[comp_id[p]].append(i)
    
    num_comp = len(comp_list)
    if num_comp == 1:
        print(-1)
        return
    
    total_pairs = 0
    for comp in comp_list:
        s = len(comp)
        total_pairs += s * (s - 1) // 2
    
    original_connectivity = total_pairs
    
    bridge_edges = []
    discovery = [-1] * (N + 1)
    low = [-1] * (N + 1)
    parent = [-1] * (N + 1)
    time = 0
    bridges = []
    
    def dfs(u):
        nonlocal time
        discovery[u] = low[u] = time
        time += 1
        for v in adj[u]:
            if discovery[v] == -1:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > discovery[u]:
                    bridges.append((min(u, v), max(u, v)))
            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])
    
    for i in range(1, N + 1):
        if discovery[i] == -1:
            dfs(i)
    
    bridge_set = set(bridges)
    
    comp_dsu = DSU(num_comp)
    for u, v in edges:
        if (min(u, v), max(u, v)) not in bridge_set:
            cu = comp_id[dsu.find(u)]
            cv = comp_id[dsu.find(v)]
            comp_dsu.union(cu, cv)
    
    super_components = {}
    for i in range(num_comp):
        p = comp_dsu.find(i)
        if p not in super_components:
            super_components[p] = []
        super_components[p].append(i)
    
    if len(super_components) == 1:
        print(-1)
        return
    
    super_list = list(super_components.values())
    super_sizes = []
    for group in super_list:
        total_size = 0
        for cidx in group:
            total_size += len(comp_list[cidx])
        super_sizes.append(total_size)
    
    found = False
    for i in range(len(super_list)):
        if len(super_list[i]) >= 2:
            c1 = super_list[i][0]
            c2 = super_list[i][1]
            u = comp_list[c1][0]
            v = comp_list[c2][0]
            print(u, v)
            found = True
            break
    
    if not found:
        for i, group in enumerate(super_list):
            if len(group) == 1:
                for j in range(i + 1, len(super_list)):
                    if len(super_list[j]) == 1:
                        c1 = group[0]
                        c2 = super_list[j][0]
                        u = comp_list[c1][0]
                        v = comp_list[c2][0]
                        print(u, v)
                        found = True
                        break
                if found:
                    break
    
    if not found:
        print(-1)

if __name__ == "__main__":
    main()
