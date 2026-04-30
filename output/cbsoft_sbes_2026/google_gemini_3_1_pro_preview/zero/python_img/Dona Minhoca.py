
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    adj = [[] for _ in range(N + 1)]
    
    idx = 1
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    def bfs_farthest(start):
        q = deque([(start, 0, -1)])
        farthest_node = start
        max_dist = 0
        parent_map = [-1] * (N + 1)
        
        while q:
            curr, dist, parent = q.popleft()
            if dist > max_dist:
                max_dist = dist
                farthest_node = curr
            
            for nxt in adj[curr]:
                if nxt != parent:
                    parent_map[nxt] = curr
                    q.append((nxt, dist + 1, curr))
                    
        return farthest_node, max_dist, parent_map

    A, _, _ = bfs_farthest(1)
    B, D, parent_map = bfs_farthest(A)
    
    path = []
    curr = B
    while curr != -1:
        path.append(curr)
        curr = parent_map[curr]
        
    def count_at_distance(start, avoid, target_dist):
        if target_dist == 0:
            return 1
        q = deque([(start, 0, avoid)])
        count = 0
        while q:
            curr, dist, parent = q.popleft()
            if dist == target_dist:
                count += 1
                continue
            for nxt in adj[curr]:
                if nxt != parent:
                    q.append((nxt, dist + 1, curr))
        return count

    if D % 2 == 0:
        c = path[D // 2]
        L = []
        for nxt in adj[c]:
            cnt = count_at_distance(nxt, c, D // 2 - 1)
            if cnt > 0:
                L.append(cnt)
        
        total_pairs = 0
        sum_L = sum(L)
        for x in L:
            total_pairs += x * (sum_L - x)
        total_pairs //= 2
        
    else:
        c1 = path[D // 2]
        c2 = path[D // 2 + 1]
        cnt1 = count_at_distance(c1, c2, (D - 1) // 2)
        cnt2 = count_at_distance(c2, c1, (D - 1) // 2)
        total_pairs = cnt1 * cnt2
        
    print(D + 1)
    print(total_pairs)

if __name__ == '__main__':
    solve()
