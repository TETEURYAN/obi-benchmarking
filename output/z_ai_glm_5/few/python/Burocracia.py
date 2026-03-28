import sys

# Increase recursion depth just in case, though we use iterative approaches
sys.setrecursionlimit(200000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    # Read initial parents p[2]...p[N]
    # p[1] is 0 (root has no parent)
    parents = [0] * (N + 1)
    for i in range(2, N + 1):
        parents[i] = int(next(iterator))
        
    # Preprocessing for LCA and depth in the static tree T_0
    # LOGN = ceil(log2(N)) approx 17 for N=10^5
    LOGN = 17
    depth = [0] * (N + 1)
    up = [[0] * (LOGN) for _ in range(N + 1)]
    
    # Root is 1, depth 1
    depth[1] = 1
    for i in range(2, N + 1):
        p = parents[i]
        depth[i] = depth[p] + 1
        up[i][0] = p
        for j in range(1, LOGN):
            up[i][j] = up[up[i][j-1]][j-1]

    # Heavy-Light Decomposition for path queries
    # We need to query max timestamp on path u -> root
    size = [0] * (N + 1)
    son = [0] * (N + 1)
    
    # DFS 1: calculate size and heavy son
    # Since p[i] < i, we can process in reverse order (N down to 1)
    for i in range(N, 0, -1):
        size[i] = 1
        # i is a heavy son of parents[i]?
        # We need to iterate children. But we only have parent pointers.
        # We can build an adjacency list first.
    
    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        adj[parents[i]].append(i)
        
    # Iterative DFS stack for size and son
    # (node, state) state 0: enter, 1: exit
    stack = [(1, 0)]
    dfs_order = []
    
    while stack:
        u, state = stack.pop()
        if state == 0:
            stack.append((u, 1))
            # Push children
            for v in adj[u]:
                stack.append((v, 0))
        else:
            size[u] = 1
            max_s = 0
            for v in adj[u]:
                size[u] += size[v]
                if size[v] > max_s:
                    max_s = size[v]
                    son[u] = v
    
    # DFS 2: decompose and get top chain
    top = [0] * (N + 1)
    id_map = [0] * (N + 1) # node to base array index
    id_counter = 0
    
    stack = [(1, 1)] # (node, top_node)
    
    while stack:
        u, t = stack.pop()
        top[u] = t
        id_map[u] = id_counter
        id_counter += 1
        
        # Push light sons first so heavy son is processed first (stack LIFO)
        # Actually we want heavy son to be top of stack? No, we want to extend current chain.
        # So we push heavy son with same top.
        # Light sons start new chains.
        
        # Push light sons
        for v in adj[u]:
            if v != son[u]:
                stack.append((v, v))
        
        # Push heavy son
        if son[u]:
            stack.append((son[u], t))

    # Segment Tree for Max Timestamp
    # We need to store (timestamp, node_index)
    # Initially all 0
    class SegTree:
        def __init__(self, n):
            self.n = 1
            while self.n < n:
                self.n <<= 1
            self.data = [(0, 0)] * (2 * self.n)
        
        def update(self, pos, val):
            # val is (timestamp, node_index)
            pos += self.n
            self.data[pos] = val
            pos >>= 1
            while pos:
                # Max timestamp
                if self.data[pos<<1][0] >= self.data[pos<<1|1][0]:
                    self.data[pos] = self.data[pos<<1]
                else:
                    self.data[pos] = self.data[pos<<1|1]
                pos >>= 1
        
        def query(self, l, r):
            # query [l, r)
            res = (0, 0)
            l += self.n
            r += self.n
            while l < r:
                if l & 1:
                    if self.data[l][0] > res[0]:
                        res = self.data[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if self.data[r][0] > res[0]:
                        res = self.data[r]
                l >>= 1
                r >>= 1
            return res

    st = SegTree(N)
    
    # Binary Lifting for the Dynamic Tree (Restructured Tree)
    # m_up[u][i] is the 2^i-th ancestor in the restructured tree
    m_up = [[0] * LOGN for _ in range(N + 1)]
    
    # Process Operations
    Q = int(next(iterator))
    output = []
    time_counter = 0
    
    # Helper: climb k steps in T_0
    def climb_static(u, k):
        curr = u
        for j in range(LOGN - 1, -1, -1):
            if k >= (1 << j):
                curr = up[curr][j]
                k -= (1 << j)
        return curr

    # Helper: query max timestamp on path u -> root
    def query_path(u):
        res = (0, 0)
        while u > 0:
            t = top[u]
            # Query range [id_map[t], id_map[u]]
            # Note: id_map[t] <= id_map[u] because of DFS order
            # In our stack DFS, we pushed heavy son last, so heavy son gets smaller id?
            # Let's check.
            # Stack: push light, push heavy.
            # Pop heavy -> id[heavy] = current. Pop light -> id[light] = current + size[heavy]...
            # So heavy son has SMALLER id than light sons.
            # In a chain, top is the highest node.
            # id_map[top] should be smaller than id_map[u].
            # Yes.
            
            l = id_map[t]
            r = id_map[u] + 1
            q_res = st.query(l, r)
            if q_res[0] > res[0]:
                res = q_res
            u = parents[t]
        return res[1]

    for _ in range(Q):
        op = int(next(iterator))
        if op == 2:
            v = int(next(iterator))
            time_counter += 1
            
            # Find parent in restructured tree
            # It is the ancestor of v in T_0 with max timestamp
            # We query path parents[v] -> root
            p_marked = query_path(parents[v])
            
            # Update m_up for v
            m_up[v][0] = p_marked
            for j in range(1, LOGN):
                prev = m_up[v][j-1]
                if prev:
                    m_up[v][j] = m_up[prev][j-1]
                else:
                    m_up[v][j] = 0
            
            # Update Segment Tree
            st.update(id_map[v], (time_counter, v))
            
        else:
            v = int(next(iterator))
            k = int(next(iterator))
            
            # Find effective parent w
            w = query_path(v)
            
            if w == 0:
                # No restructuring ancestor, climb in T_0
                output.append(str(climb_static(v, k)))
            else:
                dist = depth[v] - depth[w]
                if k <= dist:
                    # Target is in T_0 segment
                    output.append(str(climb_static(v, k)))
                else:
                    # Reach w
                    k -= dist
                    curr = w
                    
                    # Climb in restructured tree
                    for j in range(LOGN - 1, -1, -1):
                        if k >= (1 << j) and m_up[curr][j] != 0:
                            curr = m_up[curr][j]
                            k -= (1 << j)
                    
                    if k == 0:
                        output.append(str(curr))
                    else:
                        # Reached top of restructured tree chain
                        # Next step is parents[curr] in T_0
                        curr = parents[curr]
                        output.append(str(climb_static(curr, k)))

    print('\n'.join(output))

solve()