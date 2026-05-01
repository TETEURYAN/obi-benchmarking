import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    T = [int(next(it)) for _ in range(N)]
    F = [int(next(it)) for _ in range(M)]
    
    T.sort(reverse=True)
    
    heap = []
    k = [0] * M
    for j in range(M):
        heapq.heappush(heap, (0, j))
    
    total = 0
    for t in T:
        c, j = heapq.heappop(heap)
        total += c * t
        k[j] += 1
        new_c = F[j] * k[j]
        heapq.heappush(heap, (new_c, j))
    
    print(total)

if __name__ == "__main__":
    main()