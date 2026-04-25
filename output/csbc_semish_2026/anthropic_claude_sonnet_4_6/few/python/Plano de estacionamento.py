import sys
from sortedcontainers import SortedList

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    # Available spots stored in a sorted structure
    available = SortedList(range(1, N + 1))
    
    count = 0
    for i in range(M):
        V = int(data[idx]); idx += 1
        # Find the largest available spot <= V
        pos = available.bisect_right(V) - 1
        if pos < 0:
            break
        spot = available[pos]
        available.remove(spot)
        count += 1
    
    print(count)

main()