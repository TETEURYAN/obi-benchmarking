import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    while idx < len(data) and data[idx].strip() == '':
        idx += 1
    n = int(data[idx].strip())
    idx += 1
    
    files = []
    for i in range(n):
        while idx < len(data) and data[idx].strip() == '':
            idx += 1
        if idx < len(data):
            files.append(data[idx].strip())
            idx += 1
    
    # Parse each file into path components
    # path[:-1] = folders, path[-1] = filename
    parsed = []
    for f in files:
        parts = f.split('/')
        parsed.append(parts)
    
    # Build tree of all folder nodes
    # Each node: id, parent, children, depth
    # Root is node 0
    
    # We need to find the optimal reference folder (node) that minimizes total catalog length
    # For a given reference folder at depth d with path [r0, r1, ..., rd] (0-indexed, r0 is root child):
    # For each file with path [f0, f1, ..., fk] (fk is filename):
    #   - Find LCA of reference folder and file's parent folder
    #   - Let lca_depth = depth of LCA (root = depth 0, root's children = depth 1, etc.)
    #   - ref_depth = depth of reference folder (number of folders deep, root = 0)
    #   - file_folder_depth = len(parts) - 1 (number of folder components)
    #   - ups = ref_depth - lca_depth  (number of '../' needed)
    #   - downs = path from lca to file (excluding lca itself)
    #   - description length = ups * 3 + sum of (len(folder_name)+1) for folders below lca to file's folder + len(filename)
    
    # Build trie of folders
    # Node structure: children dict, depth, node_id
    
    node_parent = [-1]  # root has no parent
    node_depth = [0]    # root depth = 0
    node_name = ['']    # root name
    node_children = [{}]
    node_count = [1]
    
    # For each file, store (folder_node_id, filename)
    file_info = []
    
    for parts in parsed:
        # parts[-1] is filename, parts[:-1] are folders
        folders = parts[:-1]
        filename = parts[-1]
        cur = 0  # start at root
        for folder in folders:
            if folder not in node_children[cur]:
                new_id = len(node_parent)
                node_parent.append(cur)
                node_depth.append(node_depth[cur] + 1)
                node_name.append(folder)
                node_children.append({})
                node_children[cur][folder] = new_id
                node_count[0] += 1
            cur = node_children[cur][folder]
        file_info.append((cur, filename))
    
    total_nodes = len(node_parent)
    
    # For each folder node, precompute ancestors list (path from root to node)
    # But with up to 1e5 nodes and depth potentially large, we need efficient LCA
    
    # Build euler tour / binary lifting for LCA
    import math
    LOG = 17
    up = [[-1] * total_nodes for _ in range(LOG)]
    up[0] = node_parent[:]
    up[0][0] = 0  # root's parent is itself for LCA purposes
    
    for k in range(1, LOG):
        for v in range(total_nodes):
            if up[k-1][v] == -1:
                up[k][v] = -1
            else:
                up[k][v] = up[k-1][up[k-1][v]]
    
    def lca(u, v):
        du, dv = node_depth[u], node_depth[v]
        if du < dv:
            u, v = v, u
            du, dv = dv, du
        diff = du - dv
        for k in range(LOG):
            if (diff >> k) & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]
    
    # Precompute for each folder node: sum of (len(name)+1) from root to node (cumulative path length)
    # cum_len[v] = sum of len(name_i)+1 for all ancestors from root's child down to v
    cum_len = [0] * total_nodes
    # BFS from root
    from collections import deque
    q = deque([0])
    while q:
        v = q.popleft()
        for child_id in node_children[v].values():
            cum_len[child_id] = cum_len[v] + len(node_name[child_id]) + 1
            q.append(child_id)
    
    # For a reference node r, cost of file (folder_node f, filename fn):
    #   l = lca(r, f)
    #   ups = node_depth[r] - node_depth[l]
    #   path_down_len = cum_len[f] - cum_len[l]  (length of path from l's child to f, each with '/')
    #   if f == l: path_down_len = 0, and no trailing slash before filename
    #   cost = ups * 3 + path_down_len + len(fn)
    #   But if ups == 0 and f == r: cost = len(fn)
    #   if ups == 0 and f != r: cost = path_down_len + len(fn)  (path_down_len already includes '/')
    #   if ups > 0: cost = ups*3 + path_down_len + len(fn)
    
    # Total cost for reference r = sum over all files of cost(r, file)
    
    # We need to find r that minimizes total cost
    # Brute force over all folder nodes: O(total_nodes * N) which could be 1e10 - too slow
    
    # Better approach: tree DP
    # Let's think about what changes when we move reference from parent to child
    
    # For reference at root (node 0):
    # cost of file (f, fn) = cum_len[f] + len(fn)
    # (since ups=0, path_down = cum_len[f] - cum_len[0] = cum_len[f], and cum_len[0]=0)
    
    # When we move reference from node r to child c of r:
    # For files where f is in subtree of c: ups decreases by 1 (save 3), but we remove one folder name from path
    #   Actually: lca(c, f) = c (since f in subtree of c)
    #   old cost (ref=r): lca(r,f)=r, ups=0, path_down = cum_len[f]-cum_len[r]
    #   new cost (ref=c): lca(c,f)=c, ups=0, path_down = cum_len[f]-cum_len[c]
    #   change = (cum_len[f]-cum_len[c]) - (cum_len[f]-cum_len[r]) = cum_len[r]-cum_len[c] = -(len(name_c)+1)
    #   So each file in subtree of c saves (len(name_c)+1) characters
    
    # For files NOT in subtree of c:
    #   old cost (ref=r): lca(r,f) depends on f
    #   new cost (ref=c): ups increases by 1 (add 3 chars), lca(c,f) = lca(r,f) since f not in subtree of c
    #   change = +3 for each file not in subtree of c
    
    # So: cost(c) = cost(r) - (len(name_c)+1)*subtree_size(c) + 3*(N - subtree_size(c))
    # where subtree_size(c) = number of files in subtree of c
    
    # This is a standard tree rerooting DP!
    
    # First compute cost at root, then do DFS to compute cost at each node
    
    # Compute subtree file counts
    subtree_files = [0] * total_nodes
    for (f, fn) in file_info:
        subtree_files[f] += 1
    
    # Propagate up
    # Process nodes in reverse BFS order (leaves first)
    order = []
    q = deque([0])
    while q:
        v = q.popleft()
        order.append(v)
        for child_id in node_children[v].values():
            q.append(child_id)
    
    for v in reversed(order):
        p = node_parent[v]
        if v != 0:
            subtree_files[p] += subtree_files[v]
    
    # Cost at root
    base_cost = 0
    for (f, fn) in file_info:
        base_cost += cum_len[f] + len(fn)
    
    # Now do DFS/BFS to compute cost at each node
    node_cost = [0] * total_nodes
    node_cost[0] = base_cost
    
    best = base_cost
    
    for v in order:
        for child_id in node_children[v].values():
            sc = subtree_files[child_id]
            name_len_plus1 = len(node_name[child_id]) + 1
            node_cost[child_id] = node_cost[v] - name_len_plus1 * sc + 3 * (n - sc)
            if node_cost[child_id] < best:
                best = node_cost[child_id]
    
    print(best)

solve()