
import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    A = [int(x) for x in data[1:N+1]]
    
    compressed = []
    for x in A:
        if not compressed or compressed[-1] != x:
            compressed.append(x)
            
    compressed = [0] + compressed + [0]
    M = len(compressed)
    
    changes = defaultdict(int)
    
    for i in range(1, M - 1):
        if compressed[i] > compressed[i-1] and compressed[i] > compressed[i+1]:
            changes[compressed[i]] += 1
        elif compressed[i] < compressed[i-1] and compressed[i] < compressed[i+1]:
            changes[compressed[i]] -= 1
            
    sorted_heights = sorted(changes.keys(), reverse=True)
    
    max_comp = 0
    current_comp = 0
    
    for h in sorted_heights:
        current_comp += changes[h]
        if current_comp > max_comp:
            max_comp = current_comp
            
    print(max_comp + 1)

if __name__ == '__main__':
    solve()
