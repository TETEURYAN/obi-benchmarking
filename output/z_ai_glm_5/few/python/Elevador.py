
import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = list(map(int, data[1:1+n]))
    weights.sort()
    
    if weights[0] > 8:
        print("N")
        return
    
    for i in range(1, n):
        if weights[i] - weights[i-1] > 8:
            print("N")
            return
    
    print("S")

solve()
