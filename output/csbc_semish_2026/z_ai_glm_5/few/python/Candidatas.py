import sys
import math

# Increase recursion depth just in case, though iterative is safer/faster
sys.setrecursionlimit(200000)

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

    S = []
    for _ in range(N):
        S.append(int(next(iterator)))
    
    # Node structure for Segment Tree
    # We store:
    # pref: list of (gcd, count) for prefixes starting at left bound
    # suff: list of (gcd, count) for suffixes ending at right bound
    # cnt: total number of valid subarrays in the segment
    # size: length of the segment
    
    # Using lists for pref/suff is efficient because the number of distinct GCDs is small (log(max_val))
    
    class Node:
        __slots__ = 'pref', 'suff', 'cnt', 'size'
        def __init__(self, pref=None, suff=None, cnt=0, size=0):
            self.pref = pref if pref is not None else []
            self.suff = suff if suff is not None else []
            self.cnt = cnt
            self.size = size

    def merge_nodes(left: Node, right: Node) -> Node:
        if left.size == 0: return right
        if right.size == 0: return left
        
        new_cnt = left.cnt + right.cnt
        
        # Calculate crossing subarrays
        # Iterate all pairs of suffixes from left and prefixes from right
        # Optimization: If GCD is 1, it stays 1. We can stop early if lists are sorted by GCD descending?
        # Actually, GCDs are non-increasing in value as length increases.
        # But we can just iterate.
        # Further optimization: If gcd(g1, g2) == 1, then for fixed g1, if g2 decreases, gcd stays 1?
        # Not necessarily. gcd(6, 4)=2, gcd(6, 2)=2. gcd(6, 3)=3.
        # However, if we hit 1, we can stop.
        
        # To speed up, we rely on the lists being small.
        # We can also pre-calculate if the entire segment GCD > 1.
        # If gcd(left_total_gcd, right_total_gcd) > 1, then all pairs are valid.
        # left_total_gcd is left.pref[0][0] (GCD of entire left segment)
        # right_total_gcd is right.suff[0][0] (GCD of entire right segment)
        # Wait, pref[0] is the GCD of the whole segment starting from left.
        # suff[0] is the GCD of the whole segment ending at right.
        # Actually, for prefixes, the first element is the GCD of the whole segment.
        # For suffixes, the first element is the GCD of the whole segment.
        
        # Let's verify:
        # pref: starts with whole segment GCD, then splits.
        # suff: starts with whole segment GCD, then splits.
        # So left.pref[0][0] is GCD of all elements in left.
        # right.suff[0][0] is GCD of all elements in right.
        
        # Optimization:
        total_left_gcd = left.pref[0][0]
        total_right_gcd = right.suff[0][0]
        
        if math.gcd(total_left_gcd, total_right_gcd) > 1:
            new_cnt += left.size * right.size
        else:
            # We must iterate.
            # Lists are sorted by GCD "stages".
            # We can truncate lists at 1 to save time.
            # But let's just iterate.
            for g1, c1 in left.suff:
                if g1 == 1: break # Further suffixes will also have GCD 1
                for g2, c2 in right.pref:
                    if g2 == 1: break
                    if math.gcd(g1, g2) > 1:
                        new_cnt += c1 * c2
        
        # Merge prefixes
        # Start with left.pref
        new_pref = list(left.pref)
        # Extend with right.pref
        # The GCDs are calculated against the total GCD of the left segment
        # Because prefixes extending into right must include ALL of left.
        # Actually, prefixes of (Left + Right) are:
        # 1. Prefixes of Left.
        # 2. Left + Prefixes of Right.
        # For type 2, the GCD is gcd(total_left_gcd, g_right).
        
        base_g = total_left_gcd
        for g, c in right.pref:
            new_g = math.gcd(base_g, g)
            if new_g == new_pref[-1][0]:
                new_pref[-1] = (new_g, new_pref[-1][1] + c)
            else:
                new_pref.append((new_g, c))
                
        # Merge suffixes
        # Start with right.suff
        new_suff = list(right.suff)
        # Extend with left.suff
        # Suffixes of (Left + Right) ending in Right are just suffixes of Right.
        # Suffixes ending in Left are Left + Right. Wait.
        # Suffixes of (Left + Right):
        # 1. Suffixes of Right.
        # 2. Suffixes of Left + ALL of Right.
        # For type 2, GCD is gcd(g_left, total_right_gcd).
        
        base_g = total_right_gcd
        for g, c in left.suff:
            new_g = math.gcd(g, base_g)
            if new_g == new_suff[-1][0]:
                new_suff[-1] = (new_g, new_suff[-1][1] + c)
            else:
                new_suff.append((new_g, c))
                
        return Node(new_pref, new_suff, new_cnt, left.size + right.size)

    # Build Segment Tree
    # Size N up to 10^5. 1-based indexing easier for problem statement? Problem uses 1-based.
    # We will use 0-based internally and adjust input.
    
    size = 1
    while size < N:
        size <<= 1
    
    tree = [None] * (2 * size)
    
    # Initialize leaves
    for i in range(N):
        val = S[i]
        cnt = 1 if val > 1 else 0
        # Store (gcd, count). For a single element, count is 1.
        node_data = [(val, 1)]
        tree[size + i] = Node(node_data, node_data, cnt, 1)
    
    # Initialize remaining leaves (empty nodes)
    for i in range(N, size):
        tree[size + i] = Node([], [], 0, 0)
        
    # Build
    for i in range(size - 1, 0, -1):
        tree[i] = merge_nodes(tree[2 * i], tree[2 * i + 1])
        
    # Process Operations
    output = []
    for _ in range(M):
        T = int(next(iterator))
        if T == 1:
            I = int(next(iterator)) - 1 # 0-based index
            V = int(next(iterator))
            
            # Update leaf
            val = V
            cnt = 1 if val > 1 else 0
            node_data = [(val, 1)]
            tree[size + I] = Node(node_data, node_data, cnt, 1)
            
            # Update ancestors
            idx = (size + I) // 2
            while idx >= 1:
                tree[idx] = merge_nodes(tree[2 * idx], tree[2 * idx + 1])
                idx //= 2
                
        else: # T == 2
            E = int(next(iterator)) - 1 # 0-based
            D = int(next(iterator)) - 1 # 0-based inclusive
            
            # Query range [E, D]
            l = E + size
            r = D + size + 1 # exclusive r for standard loop
            
            # Standard segment tree query
            # We collect nodes and merge them in order
            # Since merge is not commutative, we need left and right accumulators
            
            left_res = Node([], [], 0, 0)
            right_res = Node([], [], 0, 0)
            
            while l < r:
                if l % 2 == 1:
                    left_res = merge_nodes(left_res, tree[l])
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    right_res = merge_nodes(tree[r], right_res)
                l //= 2
                r //= 2
            
            final_res = merge_nodes(left_res, right_res)
            output.append(str(final_res.cnt))
            
    print('\n'.join(output))

if __name__ == '__main__':
    solve()