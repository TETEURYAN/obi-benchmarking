import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    edges = []
    adj = defaultdict(list)
    radj = defaultdict(list)
    
    for _ in range(M):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        edges.append((x, y))
        adj[x].append(y)
        radj[y].append(x)
    
    # Kosaraju's algorithm for SCCs
    visited = [False] * (N + 1)
    order = []
    
    def dfs1(start):
        stack = [(start, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for nb in adj[node]:
                    if not visited[nb]:
                        stack.append((nb, 0))
            else:
                order.append(node)
    
    for i in range(1, N + 1):
        if not visited[i]:
            dfs1(i)
    
    comp = [0] * (N + 1)
    num_comp = 0
    visited2 = [False] * (N + 1)
    
    def dfs2(start, c):
        stack = [start]
        while stack:
            node = stack.pop()
            if visited2[node]:
                continue
            visited2[node] = True
            comp[node] = c
            for nb in radj[node]:
                if not visited2[nb]:
                    stack.append(nb)
    
    for node in reversed(order):
        if not visited2[node]:
            dfs2(node, num_comp)
            num_comp += 1
    
    # Build condensation DAG
    # comp_size
    comp_size = [0] * num_comp
    for i in range(1, N + 1):
        comp_size[comp[i]] += 1
    
    # Edges in condensation
    dag_adj = defaultdict(set)
    dag_radj = defaultdict(set)
    
    edge_set = set()
    for x, y in edges:
        cx, cy = comp[x], comp[y]
        if cx != cy:
            if (cx, cy) not in edge_set:
                edge_set.add((cx, cy))
                dag_adj[cx].add(cy)
                dag_radj[cy].add(cx)
    
    # Topological sort of DAG
    in_degree = [0] * num_comp
    for c in range(num_comp):
        for nb in dag_adj[c]:
            in_degree[nb] += 1
    
    from collections import deque
    topo = []
    q = deque()
    for c in range(num_comp):
        if in_degree[c] == 0:
            q.append(c)
    
    while q:
        node = q.popleft()
        topo.append(node)
        for nb in dag_adj[node]:
            in_degree[nb] -= 1
            if in_degree[nb] == 0:
                q.append(nb)
    
    # For each node in condensation, compute reachable set size
    # Use bitsets via integers for reachability
    # N up to 200000, num_comp up to 200000 - bitset approach too slow
    # Instead, check if DAG is a simple path (chain)
    # If DAG is a chain, adding any edge that's already implied is redundant
    # The connectivity doesn't change iff the new edge (A,B) is already reachable
    # We need: exists (A,B) not in original edges, A!=B, comp[A]->comp[B] already reachable OR comp[A]==comp[B]
    
    # Check if condensation is a simple chain
    # In a chain: each node has at most 1 successor and 1 predecessor
    is_chain = True
    for c in range(num_comp):
        if len(dag_adj[c]) > 1 or len(dag_radj[c]) > 1:
            is_chain = False
            break
    
    if not is_chain:
        # Find two nodes in condensation that are not connected (neither direction)
        # and adding edge between them won't increase connectivity
        # Actually if not a chain, there exist two SCCs not reachable from each other
        # We need to find A,B in same SCC (size>=2) or A can reach B already
        # Easiest: find SCC with size >= 2
        for c in range(num_comp):
            if comp_size[c] >= 2:
                # Find two nodes in this SCC
                nodes_in_c = []
                for i in range(1, N + 1):
                    if comp[i] == c:
                        nodes_in_c.append(i)
                        if len(nodes_in_c) == 2:
                            break
                a, b = nodes_in_c[0], nodes_in_c[1]
                # Check if edge (a,b) exists
                if b not in set(adj[a]):
                    print(a, b)
                else:
                    print(b, a)
                return
        # All SCCs size 1, but not a chain - find pair where one can reach other
        # and there's no direct edge
        # Find in topo order consecutive that have path but no direct edge
        # Actually find any redundant edge
        # Do reachability with small bitsets won't work for large N
        # For now find two nodes u,v where u->v reachable but no direct edge
        # Check topo pairs
        for i in range(len(topo)):
            u = topo[i]
            for v in dag_adj[u]:
                # Check if there's another path u->v
                # BFS from u avoiding direct edge to v
                visited_bfs = {u}
                q2 = deque([u])
                found = False
                while q2:
                    cur = q2.popleft()
                    for nb in dag_adj[cur]:
                        if nb == v and cur == u:
                            continue
                        if nb not in visited_bfs:
                            visited_bfs.add(nb)
                            if nb == v:
                                found = True
                                break
                            q2.append(nb)
                    if found:
                        break
                if found:
                    # edge (u,v) is redundant in DAG
                    # find actual nodes
                    nu = next(i for i in range(1, N+1) if comp[i] == u)
                    nv = next(i for i in range(1, N+1) if comp[i] == v)
                    print(nu, nv)
                    return
        print(-1)
    else:
        # It's a chain - connectivity is fixed, adding any edge within chain is redundant
        # But we need edge not already existing
        # In chain of length >= 3, there's a skip edge
        if len(topo) >= 3:
            # topo[0] -> topo[1] -> topo[2]
            # edge topo[0]->topo[2] is redundant
            u = topo[0]
            v = topo[2]
            nu = next(i for i in range(1, N+1) if comp[i] == u)
            nv = next(i for i in range(1, N+1) if comp[i] == v)
            print(nu, nv)
        elif num_comp == 1 and comp_size[0] >= 2:
            nodes_in_c = []
            for i in range(1, N + 1):
                nodes_in_c.append(i)
                if len(nodes_in_c) == 2:
                    break
            a, b = nodes_in_c[0], nodes_in_c[1]
            if b not in set(adj[a]):
                print(a, b)
            else:
                print(b, a)
        else:
            print(-1)

main()