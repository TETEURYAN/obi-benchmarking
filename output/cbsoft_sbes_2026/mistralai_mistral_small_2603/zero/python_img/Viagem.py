
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    V = int(data[0])
    N = int(data[1])
    M = int(data[2])
    index = 3
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a = int(data[index])
        b = int(data[index+1])
        t = int(data[index+2])
        p = int(data[index+3])
        index += 4
        graph[a].append((b, t, p))
        graph[b].append((a, t, p))
    
    X = int(data[index])
    Y = int(data[index+1])
    
    if X == Y:
        print(0)
        return
        
    INF = float('inf')
    max_p = V
    dist = [[INF] * (max_p + 1) for _ in range(N+1)]
    dist[X][0] = 0
    heap = []
    heapq.heappush(heap, (0, X, 0))
    
    while heap:
        current_dist, u, current_p = heapq.heappop(heap)
        if u == Y:
            print(current_dist)
            return
        if current_dist > dist[u][current_p]:
            continue
        for v, t, p in graph[u]:
            new_p = current_p + p
            if new_p > max_p:
                continue
            new_dist = current_dist + t
            if new_dist < dist[v][new_p]:
                dist[v][new_p] = new_dist
                heapq.heappush(heap, (new_dist, v, new_p))
    
    min_time = INF
    for p in range(max_p + 1):
        if dist[Y][p] < min_time:
            min_time = dist[Y][p]
    
    print(min_time if min_time != INF else -1)

if __name__ == "__main__":
    main()
