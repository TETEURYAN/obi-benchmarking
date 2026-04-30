
import sys
from heapq import heappush, heappop

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    F = float(data[1])
    areas = list(map(int, data[2:2+N]))

    if N == 1:
        print("0.00")
        return

    total_tax = 0.0
    heap = []
    for area in areas:
        heappush(heap, area)

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        tax = (a + b) * F
        total_tax += tax
        heappush(heap, a + b)

    print("{0:.2f}".format(total_tax))

if __name__ == "__main__":
    main()
