import sys

# Increase recursion depth to handle trees with up to 300,000 nodes
sys.setrecursionlimit(500000)

def solve():
    # Use fast I/O by reading all input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list for the tree
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Binary search for the minimum radius R
    # Lower bound: 0 (radars at the nodes themselves)
    # Upper bound: N (worst case diameter)
    low = 0
    high = N
    ans = N

    # Check function: determines if K radars of radius R can cover the tree
    def check(R):
        # radar_count keeps track of the number of radars placed
        radar_count = 0
        
        # DFS returns a tuple: (max_uncovered, min_radar)
        # max_uncovered: distance to the furthest uncovered node in the subtree.
        #                -inf if the subtree is fully covered.
        # min_radar: distance to the closest radar in the subtree.
        #            inf if there is no radar in the subtree.
        def dfs(u, parent):
            nonlocal radar_count
            
            min_radar = float('inf')
            max_uncovered = -float('inf')
            
            for v in adj[u]:
                if v == parent:
                    continue
                
                # Recursively process children
                child_uncovered, child_radar = dfs(v, u)
                
                # Increment distances by 1 to account for the edge u-v
                child_uncovered += 1
                child_radar += 1
                
                # Aggregate results from children
                if child_radar < min_radar:
                    min_radar = child_radar
                if child_uncovered > max_uncovered:
                    max_uncovered = child_uncovered
            
            # Logic to decide coverage status at node u
            
            # Case 1: There is a radar in the subtree that covers u
            if min_radar <= R:
                # Check if this radar also covers the furthest uncovered node
                # Note: if max_uncovered is -inf, the condition holds
                if min_radar + max_uncovered <= R:
                    # The subtree is fully covered
                    return (-float('inf'), min_radar)
                else:
                    # u is covered, but some nodes in the subtree are not
                    # We cannot rely on the subtree radar to cover everything
                    # Check if we must place a radar at u
                    if max_uncovered == R:
                        radar_count += 1
                        return (-float('inf'), 0)
                    else:
                        # Pass the uncovered requirement upwards
                        return (max_uncovered, min_radar)
            
            # Case 2: u is NOT covered by any radar in its subtree
            else:
                # u itself is an uncovered node (distance 0)
                # If children had uncovered nodes, max_uncovered is already set
                # If not, max_uncovered is -inf, so we take max(0, -inf) = 0
                current_uncovered = max(0, max_uncovered)
                
                if current_uncovered == R:
                    # We must place a radar at u to cover the nodes below
                    radar_count += 1
                    return (-float('inf'), 0)
                else:
                    # Pass the requirement upwards
                    return (current_uncovered, float('inf'))

        # Start DFS from root (node 1)
        final_uncovered, _ = dfs(1, 0)
        
        # If the root returns an uncovered status, we must place a radar at the root
        if final_uncovered >= 0:
            radar_count += 1
            
        return radar_count <= K

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()