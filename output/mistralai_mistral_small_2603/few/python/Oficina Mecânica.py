
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    times = list(map(int, data[2:2+n]))
    factors = list(map(int, data[2+n:2+n+m]))

    times.sort(reverse=True)
    factors.sort()

    heap = []
    for f in factors:
        heapq.heappush(heap, 0)

    total_wait = 0
    for t in times:
        current = heapq.heappop(heap)
        total_wait += current
        heapq.heappush(heap, current + t * f)

    print(total_wait)

if __name__ == "__main__":
    main()
