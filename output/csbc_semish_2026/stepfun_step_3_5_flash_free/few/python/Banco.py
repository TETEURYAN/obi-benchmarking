import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    C = int(data[0])
    N = int(data[1])
    
    heap = [0] * C
    heapq.heapify(heap)
    
    count = 0
    idx = 2
    for _ in range(N):
        T = int(data[idx])
        D = int(data[idx+1])
        idx += 2
        
        available = heapq.heappop(heap)
        start = max(T, available)
        wait = start - T
        if wait > 20:
            count += 1
        heapq.heappush(heap, start + D)
    
    print(count)

if __name__ == "__main__":
    main()