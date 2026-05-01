import sys
from collections import deque

def solve():
    sys.setrecursionlimit(300010)
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj[a].append(b)
        adj[b].append(a)
    
    # Binary search on R
    # For a given R, check if K radars suffice to cover all N nodes
    # Greedy: find the deepest uncovered leaf, place radar at its ancestor R levels up,
    # mark all nodes within R of that ancestor as covered
    
    # We need BFS/DFS order (Euler tour) for efficient ancestor finding
    # Use iterative DFS to get parent and depth arrays
    
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    order = []  # BFS order
    
    # BFS from node 1
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(1)
    visited[1] = True
    parent[1] = 0
    depth[1] = 0
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    # For a given R, greedy check
    # Process nodes in reverse BFS order (leaves first)
    # covered[v] = distance from nearest radar ancestor (or -1 if none)
    # We track for each node: the closest radar placed in its subtree going up
    
    def check(R):
        # covered[v]: how many levels up from v is the nearest radar placed in subtree of v
        # If no radar in subtree, covered[v] = infinity
        # We process in reverse BFS order
        # For each node, after processing children, if any child has covered value,
        # we take min(child_covered + 1)
        # If that value > R, we must place a radar at ancestor R levels up from this node
        
        INF = float('inf')
        # dist_up[v] = distance from v to the nearest radar placed "below or at" v
        # meaning in v's subtree
        dist_up = [INF] * (N + 1)
        radars = 0
        
        # We also need to propagate coverage downward when a radar is placed
        # Let's use a different approach:
        # covered[v] = True/False
        # Process in reverse BFS order
        # For each node v (leaf to root):
        #   if v is not covered and dist_up[v] == INF (no radar in subtree covers v)
        #   Actually we need to track: what's the shallowest uncovered node in subtree
        
        # Standard greedy for tree cover with radius R:
        # Process leaves to root in reverse BFS order
        # For each node v, track the "deepest uncovered descendant" distance
        # If that distance == R, place radar at v, mark coverage
        
        # Let deep[v] = max depth of uncovered node in subtree of v, relative to v
        # If deep[v] == R, place radar at v (covers all nodes within R of v)
        # After placing radar at v, we need to tell parent that v is covered up to R levels
        
        deep = [-1] * (N + 1)  # -1 means all covered
        radar_dist = [INF] * (N + 1)  # distance to nearest radar placed in subtree
        
        count = 0
        
        for v in reversed(order):
            # Gather children info
            max_deep = -1
            min_radar = INF
            for u in adj[v]:
                if u == parent[v]:
                    continue
                # u is child
                if deep[u] != -1:
                    max_deep = max(max_deep, deep[u] + 1)
                if radar_dist[u] != INF:
                    min_radar = min(min_radar, radar_dist[u] + 1)
            
            # Check if v itself is covered by a radar from subtree
            # A radar at distance d from v covers v if d <= R
            if min_radar <= R:
                # v is covered by a radar in subtree
                # But we still need to check if all nodes in subtree are covered
                # deep[v] already accounts for uncovered nodes
                # If max_deep == -1, all subtree covered
                deep[v] = max_deep  # could be -1
                radar_dist[v] = min_radar
            else:
                # v not covered by subtree radar
                if max_deep == -1:
                    # No uncovered nodes in subtree, but v itself uncovered
                    deep[v] = 0
                else:
                    deep[v] = max_deep
                radar_dist[v] = min_radar
            
            # If deep[v] == R, must place radar at v
            if deep[v] == R:
                count += 1
                if count > K:
                    return False
                # Place radar at v: covers all within R
                deep[v] = -1
                radar_dist[v] = 0
            
        # After processing root, check if root is covered
        if deep[1] != -1:
            # Need one more radar
            count += 1
        
        return count <= K
    
    lo, hi = 0, N - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()