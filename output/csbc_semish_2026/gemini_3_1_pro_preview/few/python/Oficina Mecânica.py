import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    t = [int(x) for x in input_data[2:n+2]]
    f = [int(x) for x in input_data[n+2:n+2+m]]
    
    if n <= m:
        print(0)
        return
        
    t.sort(reverse=True)
    
    heap = [(x, x) for x in f]
    heapq.heapify(heap)
    
    total_wait = 0
    for i in range(m, n):
        val, step = heapq.heappop(heap)
        total_wait += val * t[i]
        heapq.heappush(heap, (val + step, step))
        
    print(total_wait)

if __name__ == '__main__':
    solve()