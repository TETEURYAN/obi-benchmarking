
import sys

# Define a large value for infinity to handle minimum queries
INF = 2000000000

def merge_nodes(L, R):
    """
    Merge two segment tree nodes.
    Each node stores:
    - Top 2 maximum values and their bucket indices.
    - Top 2 minimum values and their bucket indices.
    Format: (max1, idx1, max2, idx2, min1, idy1, min2, idy2)
    """
    
    # --- Merge Maximums ---
    # Collect candidates from left and right children
    # Valid maximum values are >= 1. We use -1 for invalid entries.
    m_cands = []
    
    # Unpack Left Maxs
    m1, i1, m2, i2 = L[0], L[1], L[2], L[3]
    # Unpack Right Maxs
    m3, i3, m4, i4 = R[0], R[1], R[2], R[3]
    
    if m1 != -1: m_cands.append((m1, i1))
    if m2 != -1: m_cands.append((m2, i2))
    if m3 != -1: m_cands.append((m3, i3))
    if m4 != -1: m_cands.append((m4, i4))
    
    # Sort descending by value
    m_cands.sort(key=lambda x: -x[0])
    
    res_m1, res_i1 = -1, -1
    res_m2, res_i2 = -1, -1
    
    if len(m_cands) > 0:
        res_m1, res_i1 = m_cands[0]
    if len(m_cands) > 1:
        res_m2, res_i2 = m_cands[1]
        
    # --- Merge Minimums ---
    # Collect candidates
    # Valid minimum values are >= 1. We use INF for invalid entries.
    n_cands = []
    
    # Unpack Left Mins
    n1, j1, n2, j2 = L[4], L[5], L[6], L[7]
    # Unpack Right Mins
    n3, j3, n4, j4 = R[4], R[5], R[6], R[7]
    
    if n1 != INF: n_cands.append((n1, j1))
    if n2 != INF: n_cands.append((n2, j2))
    if n3 != INF: n_cands.append((n3, j3))
    if n4 != INF: n_cands.append((n4, j4))
    
    # Sort ascending by value
    n_cands.sort(key=lambda x: x[0])
    
    res_n1, res_j1 = INF, -1
    res_n2, res_j2 = INF, -1
    
    if len(n_cands) > 0:
        res_n1, res_j1 = n_cands[0]
    if len(n_cands) > 1:
        res_n2, res_j2 = n_cands[1]
        
    return (res_m1, res_i1, res_m2, res_i2, res_n1, res_j1, res_n2, res_j2)

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    initial_weights = []
    for _ in range(N):
        initial_weights.append(int(next(iterator)))

    # Current state of buckets
    current_max = initial_weights[:]
    current_min = initial_weights[:]

    # Segment Tree initialization
    size = 1
    while size < N:
        size <<= 1
    
    # Node: (max1, idx1, max2, idx2, min1, idy1, min2, idy2)
    empty_node = (-1, -1, -1, -1, INF, -1, INF, -1)
    tree = [empty_node] * (2 * size)

    # Set leaves
    for i in range(N):
        val = initial_weights[i]
        # Indices are 0-based
        tree[size + i] = (val, i, -1, -1, val, i, INF, -1)

    # Build internal nodes
    for i in range(size - 1, 0, -1):
        tree[i] = merge_nodes(tree[2*i], tree[2*i+1])

    output = []

    for _ in range(M):
        op = int(next(iterator))
        if op == 1:
            p = int(next(iterator))
            idx = int(next(iterator)) - 1 # 0-based index
            
            # Update bucket state
            if p > current_max[idx]:
                current_max[idx] = p
            if p < current_min[idx]:
                current_min[idx] = p
            
            # Update segment tree
            pos = size + idx
            tree[pos] = (current_max[idx], idx, -1, -1, current_min[idx], idx, INF, -1)
            pos //= 2
            while pos >= 1:
                tree[pos] = merge_nodes(tree[2*pos], tree[2*pos+1])
                pos //= 2
        else:
            a = int(next(iterator)) - 1 # 0-based
            b = int(next(iterator)) - 1 # 0-based
            
            # Query range [a, b]
            l = a + size
            r = b + size
            
            res_left = empty_node
            res_right = empty_node
            
            while l <= r:
                if l % 2 == 1:
                    res_left = merge_nodes(res_left, tree[l])
                    l += 1
                if r % 2 == 0:
                    res_right = merge_nodes(tree[r], res_right)
                    r -= 1
                l //= 2
                r //= 2
            
            res = merge_nodes(res_left, res_right)
            
            m1, i1, m2, i2, n1, j1, n2, j2 = res
            
            # Calculate result
            # If global max and global min are from different buckets
            if i1 != j1:
                ans = m1 - n1
            else:
                # If from same bucket, we must use second best max or second best min
                # Since range size >= 2, valid candidates exist
                ans = max(m1 - n2, m2 - n1)
            
            output.append(str(ans))

    print('\n'.join(output))

if __name__ == '__main__':
    solve()
