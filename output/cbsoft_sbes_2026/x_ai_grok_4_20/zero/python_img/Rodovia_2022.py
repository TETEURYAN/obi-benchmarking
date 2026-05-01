
import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

def dfs(node, graph, visited, component):
    visited[node] = True
    component.append(node)
    for nei in graph[node]:
        if not visited[nei]:
            dfs(nei, graph, visited, component)

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    
    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    edges = set()
    
    for _ in range(M):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        graph[x].append(y)
        rev_graph[y].append(x)
        edges.add((x, y))
    
    visited = [False] * (N+1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(1, N+1):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (N+1)
    scc = [-1] * (N+1)
    component_id = 0
    components = []
    
    def dfs2(u, cid):
        visited[u] = True
        scc[u] = cid
        comp = [u]
        for v in rev_graph[u]:
            if not visited[v]:
                comp.extend(dfs2(v, cid))
        return comp
    
    for i in range(len(order)-1, -1, -1):
        u = order[i]
        if not visited[u]:
            comp = dfs2(u, component_id)
            components.append(comp)
            component_id += 1
    
    K = component_id
    if K == 1:
        print(-1)
        return
    
    scc_graph = [set() for _ in range(K)]
    for u in range(1, N+1):
        cu = scc[u]
        for v in graph[u]:
            cv = scc[v]
            if cu != cv:
                scc_graph[cu].add(cv)
    
    in_degree = [0] * K
    out_degree = [0] * K
    for u in range(K):
        for v in scc_graph[u]:
            out_degree[u] += 1
            in_degree[v] += 1
    
    sources = [i for i in range(K) if in_degree[i] == 0]
    sinks = [i for i in range(K) if out_degree[i] == 0]
    
    if len(sources) == 1 and len(sinks) == 1 and sources[0] == sinks[0]:
        print(-1)
        return
    
    if len(sources) > 1 or len(sinks) > 1:
        sink_comp = sinks[0]
        source_comp = sources[0]
        a = components[sink_comp][0]
        b = components[source_comp][0]
        if (a, b) not in edges and a != b:
            print(a, b)
            return
        a = components[sink_comp][-1]
        b = components[source_comp][0]
        if (a, b) not in edges and a != b:
            print(a, b)
            return
        a = components[sink_comp][0]
        b = components[source_comp][-1]
        if (a, b) not in edges and a != b:
            print(a, b)
            return
        print(-1)
        return
    
    if len(sources) == 1 and len(sinks) == 1:
        sink_id = sinks[0]
        source_id = sources[0]
        if sink_id == source_id:
            print(-1)
            return
        a = components[sink_id][0]
        b = components[source_id][0]
        if (a, b) not in edges:
            print(a, b)
            return
        a = components[sink_id][-1]
        b = components[source_id][0]
        if (a, b) not in edges:
            print(a, b)
            return
        print(-1)
        return
    
    print(-1)

if __name__ == "__main__":
    main()
