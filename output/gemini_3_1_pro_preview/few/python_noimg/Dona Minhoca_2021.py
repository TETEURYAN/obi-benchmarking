import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    def bfs(start):
        dist = [-1] * (n + 1)
        parent = [-1] * (n + 1)
        q = [start]
        dist[start] = 0
        for u in q:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
        return dist, parent, q[-1]

    dist1, parent1, A = bfs(1)
    distA, parentA, B = bfs(A)
    
    D = distA[B]
    
    if D % 2 == 0:
        curr = B
        for _ in range(D // 2):
            curr = parentA[curr]
        C = curr
        
        dist_from_C = [-1] * (n + 1)
        dist_from_C[C] = 0
        counts = []
        for nxt in adj[C]:
            q = [nxt]
            dist_from_C[nxt] = 1
            count = 0
            for u in q:
                if dist_from_C[u] == D // 2:
                    count += 1
                if dist_from_C[u] < D // 2:
                    for v in adj[u]:
                        if dist_from_C[v] == -1:
                            dist_from_C[v] = dist_from_C[u] + 1
                            q.append(v)
            if count > 0:
                counts.append(count)
                
        ans_pairs = 0
        sum_counts = sum(counts)
        for c in counts:
            ans_pairs += c * (sum_counts - c)
        ans_pairs //= 2
        ans_len = D + 1
    else:
        curr = B
        for _ in range(D // 2):
            curr = parentA[curr]
        C1 = curr
        C2 = parentA[curr]
        
        def count_at_dist(start, avoid, target_dist):
            q = [start]
            dist_arr = [-1] * (n + 1)
            dist_arr[start] = 0
            dist_arr[avoid] = -2
            count = 0
            for u in q:
                if dist_arr[u] == target_dist:
                    count += 1
                if dist_arr[u] < target_dist:
                    for v in adj[u]:
                        if dist_arr[v] == -1:
                            dist_arr[v] = dist_arr[u] + 1
                            q.append(v)
            return count

        count1 = count_at_dist(C1, C2, (D - 1) // 2)
        count2 = count_at_dist(C2, C1, (D - 1) // 2)
        ans_pairs = count1 * count2
        ans_len = D + 1

    print(ans_len)
    print(ans_pairs)

if __name__ == '__main__':
    solve()